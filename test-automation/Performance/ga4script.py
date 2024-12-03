import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime
from IPython.display import display
from googleapiclient.discovery import build
from datetime import date, timedelta
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest, OrderBy

# Set your Google Analytics service account credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'premium-gear-402905-ad663f427cf0.json'

# Define your GA4 property ID
property_id = '337899035'

# Create a BetaAnalyticsDataClient
client = BetaAnalyticsDataClient()

def format_report(request):
    response = client.run_report(request)
    
    # Row index
    row_index_names = [header.name for header in response.dimension_headers]
    row_header = []
    for i in range(len(row_index_names)):
        row_header.append([row.dimension_values[i].value for row in response.rows])
    row_index_named = pd.MultiIndex.from_arrays(np.array(row_header), names=np.array(row_index_names))
    
    # Row flat data
    metric_names = [header.name for header in response.metric_headers]
    data_values = []
    for i in range(len(metric_names)):
        data_values.append([row.metric_values[i].value for row in response.rows])
    output = pd.DataFrame(data=np.transpose(np.array(data_values, dtype='f')), index=row_index_named, columns=metric_names)
    
    return output

def run_ga4_report(property_id, dimensions, metrics, order_bys, date_ranges):
    request = RunReportRequest(
        property='properties/' + property_id,
        dimensions=dimensions,
        metrics=metrics,
        order_bys=order_bys,
        date_ranges=date_ranges,
    )
    return format_report(request)

def calc_start_date(end_date, no_days):
    if end_date == "today":
        start_date = date.today() - timedelta(days=no_days)
        
    else:
        start_date = date.fromisoformat(end_date) - timedelta(days=no_days)
        
    return start_date.strftime("%Y-%m-%d")
def produce_report(end_date, no_days, property_id=property_id, client=client, top_n=100):
    # Get the top 100 visited pages
    page_users_table = run_ga4_report(
        property_id,
        [Dimension(name="pagePath")],
        [Metric(name="activeUsers")],
        [OrderBy(metric={'metric_name': 'activeUsers'}, desc=True)],
        [DateRange(start_date=calc_start_date(end_date, no_days), end_date=end_date)]
    )
    page_users_table['activeUsers'] = page_users_table['activeUsers'].astype('int')
    
    # Remove the top activeUser and find the top Landing Page user URLs
    landing_page_users_table = run_ga4_report(
        property_id,
        [Dimension(name="landingPage")],
        [Metric(name="activeUsers")],
        [OrderBy(metric={'metric_name': 'activeUsers'}, desc=True)],
        [DateRange(start_date=calc_start_date(end_date, no_days), end_date=end_date)]
    )
    landing_page_users_table['activeUsers'] = landing_page_users_table['activeUsers'].astype('int')
    
    print('\nTop 10 Landing Pages')
    print(landing_page_users_table[0:20])
    
    # Save the top Landing Page user URLs to an Excel file
    landing_page_users_table[0:top_n].reset_index().to_csv('Top_Landing_Pages.csv', index=False)

# Define your end_date and no_days
end_date = "2023-11-30"
no_days = 30
top_n = 20

# Call the `produce_report` function with your desired parameters
produce_report(end_date, no_days, top_n=20)

df = pd.read_csv('Top_Landing_Pages.csv')

df['pagePath'] = 'https://www.collegedekho.com' + df['landingPage']

df.to_csv('Updated_Top100_Visited_Pages.csv', index=False)


# Read the updated top 100 visited pages CSV file
df = pd.read_csv('Updated_Top100_Visited_Pages.csv')



# Function to get page metrics using PageSpeed API (mobile)
def get_page_metrics(url):
    api_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&strategy=mobile'
    print(api_url)
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        cls_value = data['lighthouseResult']['audits']['cumulative-layout-shift']['displayValue']
        cls_after_dot = cls_value.split('.')[1] if '.' in cls_value else '0'
        metrics = {
            'Performance': data['lighthouseResult']['categories']['performance']['score'],
            'First Contentful Paint': data['lighthouseResult']['audits']['first-contentful-paint']['displayValue'],
            'Largest Contentful Paint': data['lighthouseResult']['audits']['largest-contentful-paint']['displayValue'],
            'Total Blocking Time': data['lighthouseResult']['audits']['total-blocking-time']['displayValue'],
            'Cumulative Layout Shift': cls_after_dot,           
            'Speed Index': data['lighthouseResult']['audits']['speed-index']['displayValue'],
            'First Input Delay': data['lighthouseResult']['audits']['max-potential-fid']['displayValue']
        }
        return metrics
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        with open('status_codes.csv', 'a') as f:
            f.write(f'{url},{status_code}\n')
        return None
    

# Get page metrics for each pagePath
df['Page Metrics'] = df['pagePath'].apply(get_page_metrics)

# Split the page metrics into separate columns
df = pd.concat([df.drop(['Page Metrics'], axis=1), df['Page Metrics'].apply(pd.Series)], axis=1)

# Save the updated CSV file with page metrics
df.to_csv('Updated_Top100_Visited_Pages_With_Metrics.csv', index=False)

df = pd.read_csv('Updated_Top100_Visited_Pages_With_Metrics.csv')

# Set the score thresholds
good_threshold = 0.90
improvement_threshold_low = 0.60
improvement_threshold_high = 0.89

# Create DataFrames for each category based on the score criteria
good_df = df[df['Performance'] >= good_threshold]
improvement_df = df[(df['Performance'] >= improvement_threshold_low) & (df['Performance'] <= improvement_threshold_high)]
poor_df = df[df['Performance'] < improvement_threshold_low]

# Define the file names with date
current_date = datetime.datetime.now().strftime('%Y-%m-%d')
good_csv_file = f'good_{current_date}.csv'
improvement_csv_file = f'improvement_{current_date}.csv'
poor_csv_file = f'poor_{current_date}.csv'

# Save the DataFrames to separate CSV files
good_df.to_csv(good_csv_file, index=False)
improvement_df.to_csv(improvement_csv_file, index=False)
poor_df.to_csv(poor_csv_file, index=False)

# Get the counts
good_count = len(good_df)
improvement_count = len(improvement_df)
poor_count = len(poor_df)

# Print the counts
print(f"Saved {good_count} good URLs to '{good_csv_file}'")
print(f"Saved {improvement_count} improvement URLs to '{improvement_csv_file}'")
print(f"Saved {poor_count} poor URLs to '{poor_csv_file}'")


# Get the current date and previous date (you may need to customize the date format)
current_date = datetime.datetime.now().strftime('%Y-%m-%d')
previous_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

# Load the previous date's CSV files
previous_good_df = pd.read_csv(f'good_{previous_date}.csv')
previous_improvement_df = pd.read_csv(f'improvement_{previous_date}.csv')
previous_poor_df = pd.read_csv(f'poor_{previous_date}.csv')

# Load the current date's CSV files
current_good_df = pd.read_csv(f'good_{current_date}.csv')
current_improvement_df = pd.read_csv(f'improvement_{current_date}.csv')
current_poor_df = pd.read_csv(f'poor_{current_date}.csv')

# Identify newly added URLs by comparing sets
new_good_urls = set(current_good_df['pagePath']) - set(previous_good_df['pagePath'])
new_improvement_urls = set(current_improvement_df['pagePath']) - set(previous_improvement_df['pagePath'])
new_poor_urls = set(current_poor_df['pagePath']) - set(previous_poor_df['pagePath'])


# Create DataFrames for newly added URLs
new_good_df = current_good_df[current_good_df['pagePath'].isin(new_good_urls)]
new_improvement_df = current_improvement_df[current_improvement_df['pagePath'].isin(new_improvement_urls)]
new_poor_df = current_poor_df[current_poor_df['pagePath'].isin(new_poor_urls)]

# Save DataFrames to new CSV files for comparison
new_good_df.to_csv('good_comparison.csv', index=False)
new_improvement_df.to_csv('improvement_comparison.csv', index=False)
new_poor_df.to_csv('poor_comparison.csv', index=False)
