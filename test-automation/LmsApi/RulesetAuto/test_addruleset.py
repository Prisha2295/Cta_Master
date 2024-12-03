import requests
import random
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from faker import Faker
import pandas as pd
import logging
import time

# Load environment variables from .env file
load_dotenv()

# Configure logging to always create fresh logs
logging.basicConfig(
    filename='filter_ruleset.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'  # Overwrite the log file each time the script runs
)

# Load environment variables
lms_host_preprod = os.getenv("lms_host_preprod")
lms_username_preprod = os.getenv("lms_username_preprod")
lms_pass_preprod = os.getenv('lms_pass_preprod')
lms_databasename_preprod = os.getenv('lms_databasename_preprod')

# Initialize Faker for generating random data
fake = Faker()

# Function to generate a random mobile number starting with 6, 7, 8, or 9
def generate_random_user():
    name = fake.name()
    email = fake.email()
    first_digit = random.choice(['6', '7', '8', '9'])
    remaining_digits = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    mobile = first_digit + remaining_digits
    return name, email, mobile

# Generate random user data
name, email, mobile = generate_random_user()

# Log the generated user data
logging.info(f"Generated User: Name: {name}, Email: {email}, Mobile: {mobile}")

# Define the payload with random data
payload = {
    "institute_shortlists": [],
    "is_active": True,
    "name": name,
    "email": email,
    "phone_no": mobile,
    "source": 8,
    "preferences": {
        "preferred_level": 2,
        "preferred_stream": [7],
    },
    "extra_details": {
        "dob": "1996-01-01",
        "parent_guardain_phone_no": "null"
    },
    "city": None,
    "country": None,
    "state": None,
    "ip_city": None
}

# API URL
# api_url = "https://dev-lms-lmshz.collegedekho.com/1/lead/create-lead/"
api_url = "https://lms-pre.collegedekho.com/1/lead/create-lead/"
# Make the POST request
response = requests.post(api_url, json=payload,verify=False)

# Save the response data
response_data = response.json()
response_status_code = response.status_code

# Log the response from the API
logging.info(f"API Response Status Code: {response_status_code}")
logging.info(f"API Response Data: {response_data}")

# Check if the API request was successful
if response_status_code != 201:
    logging.error("API request failed")
    raise ValueError("API request failed")

# Create a database connection
engine_nf = create_engine(f'postgresql+psycopg2://{lms_username_preprod}:{lms_pass_preprod}@{lms_host_preprod}/{lms_databasename_preprod}')
logging.info("Database connection established")

# SQL Query (Using parameterized query to prevent SQL injection)
query = """
SELECT ulp.id,
ulp.lead_qualified_status,
string_agg(DISTINCT pstr.stream_id::text, ',') AS "preferred_stream",
string_agg(DISTINCT log.id::text, ',') AS "passed_ruleset",
string_agg(DISTINCT iis.institute_id::text, ',') AS "shortlisted_institutes",
string_agg(DISTINCT iis.product_stage_id::text, ',') AS "shortlisted_institutes_product_stage",
pref.preferred_level_id,
pref.preferred_study_mode,
ulp.source_id,
ulp.ip_city_id,
ulp.city_id,
ulp.state_id,
string_agg(DISTINCT pst.state_id::text, ',') AS "preferred_state",
string_agg(DISTINCT pc.city_id::text, ',') AS "preferred_city",
string_agg(DISTINCT psp.specialization_id::text, ',') AS "preferred_specialization",
string_agg(DISTINCT pd.degree_id::text, ',') AS "preferred_degree",
ulp.first_source_url
FROM collegedekho.users_leadprofile ulp
LEFT JOIN collegedekho.users_leadpreferences pref ON pref.lead_id=ulp.id
LEFT JOIN collegedekho.users_preferredstream pstr ON pref.id=pstr.preferrence_id
LEFT JOIN collegedekho.assignment_rulesets_assignmentrulesetlog log ON log.lead_id=ulp.id
LEFT JOIN collegedekho.institutes_instituteshortlist iis ON iis.lead_id=ulp.id
LEFT JOIN collegedekho.users_preferredstate pst ON pref.id=pst.preferrence_id
LEFT JOIN collegedekho.users_preferredcity pc ON pref.id=pc.preferrence_id
LEFT JOIN collegedekho.users_preferredspecialization psp ON pref.id=psp.preferrence_id
LEFT JOIN collegedekho.users_preferreddegree pd ON pref.id=pd.preferrence_id
WHERE ulp.phone_no = %s
GROUP BY ulp.id,
ulp.lead_qualified_status,
pref.preferred_level_id,
pref.preferred_study_mode,
ulp.source_id,
ulp.ip_city_id,
ulp.city_id,
ulp.state_id,
ulp.first_source_url
"""

try:
    # Execute the query with the mobile number as a parameter
    sql_read = pd.read_sql(query, engine_nf, params=(mobile,))
    logging.info(f"SQL Query executed successfully with shape: {sql_read.shape}")

    if sql_read.empty:
        logging.error("The SQL query returned an empty DataFrame.")
        raise ValueError("No data returned from the SQL query for the given mobile number.")

    # Save the query result to a CSV file with headers
    output_csv_path = "lead_profile_data.csv"
    sql_read.to_csv(output_csv_path, index=False)
    logging.info(f"Data saved to {output_csv_path}")

except Exception as e:
    logging.error(f"Error while executing SQL query: {e}")
    raise

# Function to filter data based on conditions
def filter_data(lead_profile, ruleset_data):
    filtered_ruleset = ruleset_data.copy()
    logging.info(f"Initial ruleset_data shape: {filtered_ruleset.shape}")

    # Convert all numeric values in lead_profile to integers to avoid .0 issues
    lead_profile = lead_profile.apply(lambda x: int(x) if isinstance(x, float) and x.is_integer() else x)

    # Dynamically identify relations
    relations = {}
    for column in lead_profile.index:  # Use index to get column names from lead_profile
        relation_column = f'relation_{column}'
        if relation_column in ruleset_data.columns:
            relations[column] = relation_column
            logging.info(f"Found relation column: {relation_column} for {column}")

    # Filter based on relations
    for column, relation_column in relations.items():
        lead_value = lead_profile[column]
        relation_values = filtered_ruleset[relation_column]

        if relation_column in filtered_ruleset.columns:
            # Handle 'are' and 'is' conditions
            if 'are' in relation_values.values:
                before_filter_shape = filtered_ruleset.shape
                filtered_ruleset = filtered_ruleset[filtered_ruleset[column] == lead_value]
                after_filter_shape = filtered_ruleset.shape
                logging.info(f"Filtered {column} based on relation {relation_column}. "
                             f"Shape before: {before_filter_shape}, after: {after_filter_shape}")
            elif 'is' in relation_values.values:
                before_filter_shape = filtered_ruleset.shape
                filtered_ruleset = filtered_ruleset[filtered_ruleset[column] == lead_value]
                after_filter_shape = filtered_ruleset.shape
                logging.info(f"Filtered {column} based on relation {relation_column} (is). "
                             f"Shape before: {before_filter_shape}, after: {after_filter_shape}")
            elif 'not in' in relation_values.values:
                before_filter_shape = filtered_ruleset.shape
                filtered_ruleset = filtered_ruleset[~filtered_ruleset[column].isin(lead_value)]
                after_filter_shape = filtered_ruleset.shape
                logging.info(f"Filtered {column} based on relation {relation_column} (not in). "
                             f"Shape before: {before_filter_shape}, after: {after_filter_shape}")
            elif 'is null' in relation_values.values:
                before_filter_shape = filtered_ruleset.shape
                filtered_ruleset = filtered_ruleset[filtered_ruleset[column].isna()]
                after_filter_shape = filtered_ruleset.shape
                logging.info(f"Filtered {column} based on relation {relation_column} (is null). "
                             f"Shape before: {before_filter_shape}, after: {after_filter_shape}")

    # Direct match filtering for columns without relations
    for column in lead_profile.index:  # Use index to get column names from lead_profile
        if column not in relations:
            lead_value = lead_profile[column]
            if column in filtered_ruleset.columns and not pd.isnull(lead_value):
                filtered_ruleset[column] = filtered_ruleset[column].apply(lambda x: int(x) if pd.notnull(x) and isinstance(x, float) and x.is_integer() else x)
                before_filter_shape = filtered_ruleset.shape
                filtered_ruleset = filtered_ruleset[filtered_ruleset[column] == lead_value]
                after_filter_shape = filtered_ruleset.shape
                logging.info(f"Filtered {column}. Shape before: {before_filter_shape}, after: {after_filter_shape}")

    # Combine data from both queries to understand how the filter works
    combined_data = pd.merge(sql_read, sql_read_ruleset, left_on='preferred_stream', right_on='preferred_stream', how='inner')

    # Log the combined data to show how the filter works
    logging.info(f"Combined Data (Filter Logic): {combined_data}")

    # Save the filtered ruleset to a CSV
    output_csv_path_filtered = "filtered_ruleset.csv"
    filtered_ruleset.to_csv(output_csv_path_filtered, index=False)
    logging.info(f"Filtered ruleset saved to {output_csv_path_filtered}")

    # Save the combined data to a CSV file with headers
    combined_csv_path = "combined_filter_data.csv"
    combined_data.to_csv(combined_csv_path, index=False)
    logging.info(f"Combined data saved to {combined_csv_path}")

# Fetching the ruleset data
query2 = """
WITH rules_expanded AS (
  SELECT id,
         ruleset_type,
         region_id,
         jsonb_build_array(NULL) AS rule_set
  FROM collegedekho.assignment_rulesets_assignmentruleset
  WHERE is_active=TRUE
    AND object_status=1
    AND status='Activated'
    AND ruleset_type IN ('CSL', 'CLL', 'CS', 'CC', 'L1', 'PRODUCT')
    AND jsonb_array_length(rules::jsonb) = 0

  UNION ALL

  SELECT id,
         ruleset_type,
         region_id,
         jsonb_array_elements(rules::jsonb) AS rule_set
  FROM collegedekho.assignment_rulesets_assignmentruleset
  WHERE is_active=TRUE
    AND object_status=1
    AND status='Activated'
    AND ruleset_type IN ('CSL', 'CLL', 'CS', 'CC', 'L1', 'PRODUCT')
    AND jsonb_array_length(rules::jsonb) > 0
),
rule_sets_expanded AS (
  SELECT id,
         ruleset_type,
         region_id,
         rule_set AS RULE
  FROM rules_expanded
),
detailed_rules AS (
  SELECT id,
         ruleset_type,
         region_id,
         RULE -> 'relation' ->> 'label' AS relation_label,
         RULE -> 'key' ->> 'label' AS key_label,
         RULE -> 'value' AS value_field
  FROM rule_sets_expanded
),
value_labels AS (
  SELECT id,
         ruleset_type,
         region_id,
         relation_label,
         key_label,
         CASE
           WHEN jsonb_typeof(value_field) = 'array' THEN
             (SELECT string_agg(value->>'value', ', ')
              FROM jsonb_array_elements(value_field) AS arr(value))
           WHEN value_field -> 'value' IS NOT NULL THEN value_field ->> 'value'
           ELSE value_field ->> 'value'
         END AS value_label
  FROM detailed_rules
)
SELECT l.id AS "ruleset_id",
       l.ruleset_type AS "ruleset_type",
       r.id AS "ruleset_region",
       string_agg(DISTINCT st.id::text,',') AS "preferred_stream",
       string_agg(DISTINCT ii.institute_id::text,',') AS "shortlisted_institutes",
       string_agg(DISTINCT ps.stage_id::text,',') AS "shortlisted_institutes_product_stage",
       MAX(CASE
               WHEN key_label = 'Preferred Level' THEN relation_label
           END) AS "relation_preferred_level_id",
       MAX(CASE
               WHEN key_label = 'Preferred Level' THEN value_label
           END) AS "preferred_level_id",
       MAX(CASE
               WHEN key_label = 'Source' THEN relation_label
           END) AS "relation_source_id",
       MAX(CASE
               WHEN key_label = 'Source' THEN value_label
           END) AS "source_id",
       MAX(CASE
               WHEN key_label = 'Lead Qualified Status' THEN relation_label
           END) AS "relation_lqs",
       MAX(CASE
               WHEN key_label = 'Lead Qualified Status' THEN value_label
           END) AS "lqs_values",
       MAX(CASE
               WHEN key_label = 'Lead Stage' THEN relation_label
           END) AS "relation_lead_stge",
       MAX(CASE
               WHEN key_label = 'Lead Stage' THEN value_label
           END) AS "lead_stage_values",
       MAX(CASE
               WHEN key_label = 'Lead Sub Stage' THEN relation_label
           END) AS "relation_lead_substage",
       MAX(CASE
               WHEN key_label = 'Lead Sub Stage' THEN value_label
           END) AS "lead_substage_values",
       MAX(CASE
               WHEN key_label = 'Product Stage' THEN relation_label
           END) AS "relation_product_stge",
       MAX(CASE
               WHEN key_label = 'Product Stage' THEN value_label
           END) AS "product_stage_values",
       MAX(CASE
               WHEN key_label = 'IP City' THEN relation_label
           END) AS "relation_ip_city_id",
       MAX(CASE
               WHEN key_label = 'IP City' THEN value_label
           END) AS "ip_city_id",
       MAX(CASE
               WHEN key_label = 'Current City' THEN relation_label
           END) AS "relation_city_id",
       MAX(CASE
               WHEN key_label = 'Current City' THEN value_label
           END) AS "city_id",
       MAX(CASE
               WHEN key_label = 'Preferred City' THEN relation_label
           END) AS "relation_preferred_city",
       MAX(CASE
               WHEN key_label = 'Preferred City' THEN value_label
           END) AS "preferred_city",
       MAX(CASE
               WHEN key_label = 'Current State' THEN relation_label
           END) AS "relation_state_id",
       MAX(CASE
               WHEN key_label = 'Current State' THEN value_label
           END) AS "state_id",
       MAX(CASE
               WHEN key_label = 'Preferred State' THEN relation_label
           END) AS "relation_preferred_state",
       MAX(CASE
               WHEN key_label = 'Preferred State' THEN value_label
           END) AS "preferred_state",
       MAX(CASE
               WHEN key_label = 'Preferred Specialization' THEN relation_label
           END) AS "relation_preferred_specialization",
       MAX(CASE
               WHEN key_label = 'Preferred Specialization' THEN value_label
           END) AS "preferred_specializations",
       MAX(CASE
               WHEN key_label = 'Preferred Mode' THEN relation_label
           END) AS "relation_preferred_study_mode",
       MAX(CASE
               WHEN key_label = 'Preferred Mode' THEN value_label
           END) AS "preferred_study_mode",
       MAX(CASE
               WHEN key_label = 'Preferred Degree' THEN relation_label
           END) AS "relation_preferred_degree",
       MAX(CASE
               WHEN key_label = 'Preferred Degree' THEN value_label
           END) AS "preferred_degree",
       MAX(CASE
               WHEN key_label = 'First Source URL' THEN relation_label
           END) AS "relation_first_source_url",
       MAX(CASE
               WHEN key_label = 'First Source URL' THEN value_label
           END) AS "first_source_url",
       MAX(CASE
               WHEN key_label = 'Source URL' THEN relation_label
           END) AS "relation_Source URL",
       MAX(CASE
               WHEN key_label = 'Source URL' THEN value_label
           END) AS "Source URL_values"
FROM value_labels l
LEFT JOIN collegedekho.utils_region r ON r.id=l.region_id
LEFT JOIN collegedekho.assignment_rulesets_assignmentruleset_streams ars ON l.id=ars.assignmentruleset_id
LEFT JOIN courses_stream st ON ars.stream_id=st.id
LEFT JOIN collegedekho.assignment_rulesets_assignmentruleset_institutes ii ON l.id=ii.assignmentruleset_id
LEFT JOIN collegedekho.assignment_rulesets_assignmentruleset_product_stages ps ON l.id=ps.assignmentruleset_id
GROUP BY l.id,
         l.ruleset_type,
         r.id
ORDER BY l.id;
"""

try:
    # Execute the query for ruleset data
    sql_read_ruleset = pd.read_sql(query2, engine_nf)
    logging.info(f"SQL Query for ruleset executed successfully with shape: {sql_read_ruleset.shape}")

    if sql_read_ruleset.empty:
        logging.error("The SQL query for ruleset returned an empty DataFrame.")
        raise ValueError("No ruleset data returned from the SQL query.")

    # Save the query result to a CSV file with headers
    output_csv_path_ruleset = "ruleset_data.csv"
    sql_read_ruleset.to_csv(output_csv_path_ruleset, index=False)
    logging.info(f"Ruleset data saved to {output_csv_path_ruleset}")

except Exception as e:
    logging.error(f"Error while executing SQL query for ruleset: {e}")
    raise

# Apply filter logic to lead profile and ruleset data
try:
    if sql_read.empty:
        logging.error("The DataFrame 'sql_read' is empty. Cannot extract lead profile data.")
        raise ValueError("Empty DataFrame")

    lead_profile = sql_read.iloc[0]
    logging.info(f"Lead profile data extracted with shape {sql_read.shape}")

    # Filter data
    filter_data(lead_profile, sql_read_ruleset)

except KeyError as e:
    logging.error(f"Key error during filtering: {e}")
    raise
except TypeError as e:
    logging.error(f"Type error during filtering: {e}")
    raise
except IndexError as e:
    logging.error(f"Index error during filtering: {e}")
    raise
except ValueError as e:
    logging.error(f"Value error: {e}")
    raise
except Exception as e:
    logging.error(f"Unexpected error during filtering: {e}")
    raise

# Running timer count for 4 minutes (240 seconds)
for remaining in range(240, 0, -1):
    print(f"Running in {remaining} seconds...", end="\r")
    time.sleep(1)

# Indicate that the timer has finished
print("Running now!")

# Read lead_profile_data.csv
lead_profile_data_path = "lead_profile_data.csv"
lead_profile_data = pd.read_csv(lead_profile_data_path)

# Extract lead_id from the first row
lead_id = lead_profile_data.iloc[0]['id']
logging.info(f"Extracted lead_id: {lead_id}")

# Query to fetch assignment ruleset log using lead_id
query = f"SELECT * FROM collegedekho.assignment_rulesets_assignmentrulesetlog WHERE lead_id = {lead_id}"
assignment_ruleset_log = pd.read_sql(query, engine_nf)
logging.info(f"Fetched assignment ruleset log with {assignment_ruleset_log.shape[0]} records")

# Extract assignment_ruleset_id from the query result
assignment_ruleset_ids = assignment_ruleset_log['assignment_ruleset_id'].unique()
logging.info(f"Extracted assignment_ruleset_id(s): {assignment_ruleset_ids}")

# Load combined_filter_data.csv
combined_filter_data_path = "combined_filter_data.csv"
combined_filter_data = pd.read_csv(combined_filter_data_path)

# Check for matching ruleset_id in combined_filter_data.csv
matched_data = combined_filter_data[combined_filter_data['ruleset_id'].isin(assignment_ruleset_ids)]

if not matched_data.empty:
    logging.info("Best match found.")
    print("Best match found")
    output_file_path = "best_match_found.csv"
else:
    logging.info("Best match not found.")
    print("Best match not found")
    output_file_path = "best_match_not_found.csv"

# Save the result to a new CSV file
matched_data.to_csv(output_file_path, index=False)
logging.info(f"Result saved to {output_file_path}")

# Print the path of the output file
print(f"Output file saved at: {output_file_path}")
