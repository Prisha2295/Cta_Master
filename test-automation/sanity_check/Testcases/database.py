import mysql.connector
from selenium.webdriver.common.by import By
import time
from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

cld_host_live = os.getenv("cld_host_live")
cld_username_live = os.getenv("cld_username_live")
cld_pass_live = os.getenv("cld_pass_live")
cld_databasename_live = os.getenv("cld_databasename_live")

cld_host_staging = os.getenv("cld_host_staging")
cld_username_staging = os.getenv("cld_username_staging")
cld_pass_staging = os.getenv("cld_pass_staging")
cld_databasename_staging = os.getenv("cld_databasename_staging")

lms_host_live = os.getenv("lms_host_live")
lms_username_live = os.getenv("lms_username_live")
lms_pass_live = os.getenv("lms_pass_live")
lms_databasename_live = os.getenv("lms_databasename_live")

lms_host_staging = os.getenv("lms_host_staging")
lms_username_staging = os.getenv("lms_username_staging")
lms_pass_staging = os.getenv("lms_pass_staging")
lms_databasename_staging = os.getenv("lms_databasename_staging")

sso_host_live = os.getenv("sso_host_live")
sso_username_live = os.getenv("sso_username_live")
sso_pass_live = os.getenv("sso_pass_live")
sso_databasename_live = os.getenv("sso_databasename_live")

sso_host_staging = os.getenv("sso_host_staging")
sso_username_staging = os.getenv("sso_username_staging")
sso_pass_staging = os.getenv("sso_pass_staging")
sso_databasename_staging = os.getenv("sso_databasename_staging")

def cld_lead(logger, phone_no):
    # Create a MySQL database connection
    conn = mysql.connector.connect(host=cld_host_live, database=cld_databasename_live, user=cld_username_live, password=cld_pass_live)
    # conn = mysql.connector.connect(host='95.217.156.247',database = 'collegedekho',user = 'cld_ro', password = 'w4snE59A$dr@k48q')

    logger.info(conn)
    
    query = ("""SELECT 
                    uup.id,
                    uup.email,
                    uup.name,
                    uup.phone_no,
                    iis.name as state_id,
                    iiic.name as city_id,
                    iic.name as user_city_id,
                    uup.first_source_url,
                    ua.source_url,
                    ua.institute_id,
                    cs.name as preferred_stream,
                    up.preferred_specialization_id,
                    cs.name as stream_name,
                    iiss.name as pref_state,
                    iiiic.name as pref_city,
                    up.preferred_level,
                    upd.degree_id
                FROM users_userprofile uup
                LEFT JOIN users_activity ua ON ua.user_id = uup.id
                LEFT JOIN users_userpreferences up ON up.user_id = uup.id
                LEFT JOIN course_stream css ON up.preferred_stream_id = css.id
                LEFT JOIN users_userpreferences_preferred_degrees upd ON upd.userpreferences_id = up.id  
                LEFT JOIN institute_state iis ON uup.state_id = iis.id
                LEFT JOIN institute_city iic ON uup.user_city_id = iic.id
                LEFT JOIN course_stream cs ON up.preferred_stream_id = cs.id
                LEFT JOIN institute_city iiic ON uup.city_id = iiic.id
                LEFT JOIN users_userpreferences_preferred_state ups ON ups.userpreferences_id = up.id
                LEFT JOIN institute_state iiss ON ups.state_id = iiss.id
                LEFT JOIN users_userpreferences_preferred_city upc ON upc.userpreferences_id = up.id
                LEFT JOIN institute_city iiiic ON upc.city_id = iiiic.id
                WHERE uup.phone_no = %s
                limit 1
                """)
    
    cursor = conn.cursor()
    cursor.execute(query,(phone_no,))
    CLD_Lead_Detail = cursor.fetchone()
    Lead_ID = CLD_Lead_Detail[0]
    Email = CLD_Lead_Detail[1]
    Name = CLD_Lead_Detail[2]
    Phone_No = CLD_Lead_Detail[3]
    State_ID = CLD_Lead_Detail[4]
    City_ID = CLD_Lead_Detail[5]
    User_City = CLD_Lead_Detail[6]
    First_Source_URL = CLD_Lead_Detail[7]
    Source_URL = CLD_Lead_Detail[8]
    Institute_Id = CLD_Lead_Detail[9]
    Preferred_Stream = CLD_Lead_Detail[10]
    Preferred_Specialization = CLD_Lead_Detail[11]
    Stream_ID = CLD_Lead_Detail[12]
    Preferred_State = CLD_Lead_Detail[13]
    Preferred_City = CLD_Lead_Detail[14]
    Preferred_Level = CLD_Lead_Detail[15]
    Degree_ID = CLD_Lead_Detail[16]

    for row in CLD_Lead_Detail:
        logger.info(row)
    
    # Close the cursor and database connection
    cursor.close()
    conn.close()
    
    return Lead_ID, Email, Name, Phone_No, State_ID, City_ID, User_City, First_Source_URL, Source_URL, Institute_Id, Preferred_Stream, Preferred_Specialization, Stream_ID, Preferred_State, Preferred_City, Preferred_Level, Degree_ID

def lMS_lead(logger,phone_no):
        # engine_nf = create_engine(f'postgresql+psycopg2://lms_username_staging:lms_pass_staging@lms_host_staging/lms_databasename_staging')
        engine_nf = create_engine(f'postgresql+psycopg2://{lms_username_live}:{lms_pass_live}@{lms_host_live}/{lms_databasename_live}')
        print("LMS NO", phone_no)
        logger.info("LMS NO" + phone_no)
        print(engine_nf)
        logger.info(engine_nf)
        sql_read =  pd.read_sql("""SELECT cul.id,
                            cul.name,
                            cul.email,
                            cul.phone_no,
                            cul.source_url,
                            cul.first_source_url,
                            cul.city_id,
                            cul.ip_city_id,
                            cul.state_id,
                            culp.preferred_level_id,
                            cups.specialization_id,
                            cupst.stream_id,
                            cupse.state_id as preferred_state,
                            cupd.degree_id,
                            cupc.city_id as preferred_city,
                            iis.institute_id as institute_id
                        FROM collegedekho.users_leadprofile cul
                        LEFT JOIN collegedekho.users_leadpreferences culp ON cul.id = culp.lead_id
                        LEFT JOIN collegedekho.users_preferredspecialization cups ON culp.id = cups.preferrence_id
                        LEFT JOIN collegedekho.users_preferredstream cupst ON culp.id = cupst.preferrence_id
                        LEFT JOIN collegedekho.users_preferredstate cupse ON culp.id = cupse.preferrence_id
                        LEFT JOIN collegedekho.users_preferreddegree cupd ON culp.id = cupd.preferrence_id
                        LEFT JOIN collegedekho.users_preferredcity cupc ON culp.id = cupc.preferrence_id
                        LEFT JOIN collegedekho.institutes_instituteshortlist iis ON iis.lead_id = cul.id
                        where cul.phone_no = '{}'""".format(phone_no), engine_nf)
        # print(sql_read)
        LMS_Lead_ID = sql_read['id'].iloc[0]
        logger.info(f"LMS Lead ID: {LMS_Lead_ID}")
        LMS_Name = sql_read['name'].iloc[0]
        logger.info(f"LMS Lead Name: {LMS_Name}")
        lMS_Email = sql_read['email'].iloc[0]
        logger.info(f"LMS Lead Email: {lMS_Email}")
        LMS_Phone_No = sql_read['phone_no'].iloc[0]
        logger.info(f"LMS Lead Phone No: {LMS_Phone_No}")
        LMS_Source_URL = sql_read['source_url'].iloc[0]
        logger.info(f"LMS Lead Source URL: {LMS_Source_URL}")
        LMS_First_Source_URL = sql_read['first_source_url'].iloc[0]
        logger.info(f"LMS Lead First Source: {LMS_First_Source_URL}")
        LMS_City_ID = sql_read['city_id'].iloc[0]
        logger.info(f"LMS Lead City: {LMS_City_ID}")
        LMS_User_City_ID = sql_read['ip_city_id'].iloc[0]
        logger.info(f"LMS User City: {LMS_User_City_ID}")
        LMS_State_ID = sql_read['state_id'].iloc[0]
        logger.info(f"LMS Lead State: {LMS_State_ID}")
        LMS_Preferred_Level = sql_read['preferred_level_id'].iloc[0]
        logger.info(f"LMS Lead Level: {LMS_Preferred_Level}")
        LMS_Preferred_Specialization = sql_read['specialization_id'].iloc[0]
        logger.info(f"LMS Lead Spec: {LMS_Preferred_Specialization}")
        LMS_Preferred_Stream = sql_read['stream_id'].iloc[0]
        logger.info(f"LMS Lead Stream: {LMS_Preferred_Stream}")
        LMS_Preferred_State = sql_read['preferred_state'].iloc[0]
        logger.info(f"LMS Lead Pr State: {LMS_Preferred_State}")
        LMS_Preferred_Degree = sql_read['degree_id'].iloc[0]
        logger.info(f"LMS Lead Degree: {LMS_Preferred_Degree}")
        LMS_Preferred_City = sql_read['preferred_city'].iloc[0]
        logger.info(f"LMS Lead Pr City: {LMS_Preferred_City}")
        LMS_Institute_ID = sql_read['institute_id'].iloc[0]
        logger.info(f"LMS Lead Institute ID: {LMS_Institute_ID}")
        return LMS_Lead_ID, LMS_Name, lMS_Email, LMS_Phone_No, LMS_Source_URL, LMS_First_Source_URL, LMS_City_ID, LMS_User_City_ID, LMS_State_ID, LMS_Preferred_Level, LMS_Preferred_Specialization,LMS_Preferred_Stream, LMS_Preferred_State, LMS_Preferred_Degree, LMS_Preferred_City, LMS_Institute_ID
    
def SSO_lead(logger, phone_no):
    # Create a MySQL database connection
    conn = mysql.connector.connect(host=sso_host_live, database=sso_databasename_live, user=sso_username_live, password=sso_pass_live)
    logger.info("Printing SSO Details")
    logger.info(conn)
    logger.info(phone_no)
    
    query = ("""select id, name, email, phone_no
                from users_user
                where phone_no = %s 
                limit 1""")
    
    cursor = conn.cursor()
    cursor.execute(query, (phone_no,))
    SSO_Lead_Detail = cursor.fetchone()

    if SSO_Lead_Detail is not None:
        SSO_Lead_ID = SSO_Lead_Detail[0]
        SSO_Name = SSO_Lead_Detail[1]
        SSO_Email = SSO_Lead_Detail[2]
        SSO_Phone_No = SSO_Lead_Detail[3]

        for row in SSO_Lead_Detail:
            logger.info(row)
    else:
        SSO_Lead_ID = None
        SSO_Name = None
        SSO_Email = None
        SSO_Phone_No = None
        logger.info("No results found for phone number: {}".format(phone_no))
    
    # Close the cursor and database connection
    cursor.close()
    conn.close()
    
    return SSO_Lead_ID, SSO_Name, SSO_Email, SSO_Phone_No


def pushlog_payload(logger, phone_no):
    # Create a MySQL database connection
    conn = mysql.connector.connect(host=cld_host_live, database=cld_databasename_live, user=cld_username_live, password=cld_pass_live)
    # conn = mysql.connector.connect(host='95.217.156.247',database = 'collegedekho',user = 'cld_ro', password = 'w4snE59A$dr@k48q')

    logger.info(conn)
    
    query = ("""SELECT
                JSON_UNQUOTE(JSON_EXTRACT(payload, '$.name')) AS name,
                JSON_UNQUOTE(JSON_EXTRACT(payload, '$.phone_no')) AS phone_no,
                JSON_UNQUOTE(JSON_EXTRACT(payload, '$.email')) AS email,
                JSON_UNQUOTE(JSON_EXTRACT(payload, '$.first_source_url')) AS first_source_url,
                JSON_UNQUOTE(JSON_EXTRACT(payload, '$.city')) AS city,
                JSON_UNQUOTE(JSON_EXTRACT(payload, '$.ip_city')) AS ip_city,
                JSON_UNQUOTE(JSON_EXTRACT(payload, '$.state')) AS state,
                JSON_UNQUOTE(JSON_EXTRACT(payload, '$.level')) AS level,
                JSON_UNQUOTE(JSON_EXTRACT(payload, '$.stream')) AS stream,
                JSON_UNQUOTE(JSON_EXTRACT(payload, '$.endpoint')) AS endpoint,
                JSON_UNQUOTE(JSON_EXTRACT(payload, '$.latitude')) AS latitude,
                JSON_UNQUOTE(JSON_EXTRACT(payload, '$.longitude')) AS longitude,
                JSON_UNQUOTE(JSON_EXTRACT(payload, '$.source_url')) AS source_url
                FROM users_pushusersynclog
                WHERE phone_no = %s""")
    
    cursor = conn.cursor()
    cursor.execute(query,(phone_no,))
    Push_Sync_Payload = cursor.fetchone()
    Sync_Name = Push_Sync_Payload[0]
    Sync_PhoneNo = Push_Sync_Payload[1]
    Sync_Email = Push_Sync_Payload[2]
    Sync_First_Source_URL = Push_Sync_Payload[3]
    Sync_City = Push_Sync_Payload[4]
    Sync_IP_City = Push_Sync_Payload[5]
    Sync_State = Push_Sync_Payload[6]
    Sync_Level = Push_Sync_Payload[7]
    Sync_Stream = Push_Sync_Payload[8]
    Sync_Endpoint = Push_Sync_Payload[9]
    Sync_Latitude = Push_Sync_Payload[10]
    Sync_Longitude = Push_Sync_Payload[11]
    Sync_Source_URL = Push_Sync_Payload[12]

    for row in Push_Sync_Payload:
        logger.info(row)
    
    # Close the cursor and database connection
    cursor.close()
    conn.close()
    
    return Sync_Name, Sync_PhoneNo, Sync_Email, Sync_First_Source_URL, Sync_City, Sync_IP_City, Sync_State, Sync_Level, Sync_Stream, Sync_Endpoint, Sync_Latitude, Sync_Longitude, Sync_Source_URL

def pushlog_response(logger,phone_no):
    
    conn = mysql.connector.connect(host=cld_host_live, database=cld_databasename_live, user=cld_username_live, password=cld_pass_live)
    # conn = mysql.connector.connect(host='95.217.156.247',database = 'collegedekho',user = 'cld_ro', password = 'w4snE59A$dr@k48q')
    logger.info(conn)
    
    query = ("""SELECT response
                FROM users_pushusersynclog
                WHERE phone_no = %s""")
    
    cursor = conn.cursor()
    cursor.execute(query,(phone_no,))
    Push_Sync_Payload = cursor.fetchone()
    Response_Message = Push_Sync_Payload[0]

    for row in Push_Sync_Payload:
        logger.info(row)
    
    # Close the cursor and database connection
    cursor.close()
    conn.close()
    
    return Response_Message

def news_url_connect(logger):
    # Create a MySQL database connection
    conn = mysql.connector.connect(host=cld_host_live, database=cld_databasename_live, user=cld_username_live, password=cld_pass_live)
    # conn = mysql.connector.connect(host='cld_host_staging,database = cld_databasename_staging,user = cld_username_staging, password = cld_pass_staging)
    # logger.info(conn)
    
    query = ("""select slug, uri_id
                from news_news
                where language_id = 1 && news_type = 1
                order by id desc
                limit 1""")
    
    cursor = conn.cursor()
    cursor.execute(query)
    Newsslug = cursor.fetchone()
    NewsURL = Newsslug[0]
    Uriid = Newsslug[1]
    
    # Close the cursor and database connection
    cursor.close()
    conn.close()
    
    return NewsURL, Uriid
