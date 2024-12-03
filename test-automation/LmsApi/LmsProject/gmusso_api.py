import time
import unittest
import requests
import mysql.connector
import psycopg2
from payloads import Attributes
from dotenv import load_dotenv
import os

load_dotenv()

gmu_host_ssoapi = os.getenv("gmu_host_ssoapi")
gmu_username_ssoapi = os.getenv("gmu_username_ssoapi")
gmu_pass_ssoapi = os.getenv("gmu_pass_ssoapi")
gmu_databasename_ssoapi = os.getenv("gmu_databasename_ssoapi")
gmu_auth_plugin = os.getenv("gmu_auth_plugin")

gmu_host_live = os.getenv("gmu_host_live")
gmu_username_live = os.getenv("gmu_username_live")
gmu_pass_live= os.getenv("gmu_pass_live")
gmu_databasename_live = os.getenv("gmu_databasename_live")

class Test(unittest.TestCase):
    def test_sso(self):
        hold_start = time.time()

        # Number of requests to make
        number_of_requests = 1

        # Keep track of failed requests
        failed_requests = 0

        url = "http://sso.collegedekho.com/api/users/"
            
        for i in range(number_of_requests):
            count = 0
            payload = Attributes().gmusso_payloads()
            
            for payloads in payload:

                try:
                    response = requests.post(url,headers={'Authorization':'Token 2961f0aa05951161b5fbd69b936e33230735027c'},json=payloads)

                    # Check if the request was successful
                    if response.status_code != 200:
                        failed_requests += 1
                        print("Record Generate")
                    # print(response.json())
                except Exception as exc:
                    print("Exception - ", exc)
                    failed_requests += 1

                
                print("Failed requests: ", failed_requests)
                print("Successful requests: ", number_of_requests - failed_requests)
                resp = response.json()
                user_id = resp['id']
                user_name = resp['name']
                user_mobile = resp['phone_no']
                vertical = resp['business_unit']
                groups = resp['groups']
                print('User_id : ',user_id)
                print('User_name : ' ,user_name)
                print('User_mobile : ',user_mobile)
                print('Business Unit : ',vertical)
                print('Groups : ',groups)
                time.sleep(2)
            
                
        conn = mysql.connector.connect(host=gmu_host_ssoapi, database=gmu_databasename_ssoapi, user=gmu_username_ssoapi,
                                           password=gmu_pass_ssoapi,auth_plugin=gmu_auth_plugin)
        conn = mysql.connector.connect(host=gmu_host_ssoapi, database=gmu_databasename_ssoapi, user=gmu_username_ssoapi,
                                           password=gmu_pass_ssoapi,auth_plugin=gmu_auth_plugin)
        print(conn)
        sso_query = ("""select * from users_user where id = {}""".format(user_id))
        cursor = conn.cursor()
        cursor.execute(sso_query)
        sso_row = cursor.fetchall()
        sso_result_dict = list(sso_row)
        # print(sso_result_dict)

        for i in sso_result_dict:
            sso_user_id = i[0]
            sso_user_name = i[4]
            sso_user_mobile = i[5]
            sso_user_email = i[8]
            print("sso_user_id : ",sso_user_id)
            print("sso_user_name : ",sso_user_name)
            print("sso_user_mobile : ",sso_user_mobile)
            print("sso_user_email : ",sso_user_email)

        if user_id == sso_user_id:
            print("user id match ")
        else:
            print("user id not match")

        if user_name == sso_user_name:
            print("user name match")
        else:
            print("user name not match")
        
        if user_mobile==sso_user_mobile:
            print("user mobile match")
        else:
            print("user mobile not match")


   
#Lms api checking lead status in lms 
        lms_api = requests.get("http://lms-rhz.collegedekho.com/2/lead/{}/".format(sso_user_id))

        print("Status_code : ",lms_api.status_code)
        if lms_api.status_code != 200:
            failed_requests += 1
            print(lms_api.json())
                
        lms_resp = lms_api.json()
        lms_user_id = lms_resp['id']
        lms_user_name = lms_resp['name']
        lms_user_mobile = lms_resp['phone_no']
        print("lms_userid : ",lms_user_id)
        print("lms_username : ",lms_user_name)
        print("lms_usermobile : ",lms_user_mobile)

        verify_userid = user_id == sso_user_id==lms_user_id
        if not verify_userid:
            print(user_id,lms_user_id,sso_user_id)




        login_payload = Attributes().login_payloads()
        print(login_payload)
        login_api = requests.post("http://sso.collegedekho.com/api/users/login",json=login_payload)
        if login_api.status_code != 200:
            failed_requests += 1
            print(login_api.json())
        login_resp = login_api.json()
        print("-----------------------")
        login_accesstoken = login_resp['access-token']
        print(login_accesstoken)
        time.sleep(5)



        headers = {"Authorization": "Bearer {}".format(login_accesstoken)}
        recommendation_url = "http://lms-rhz.collegedekho.com/2/cohort/{}/recommendation/".format(lms_user_id) 
        
        recomendation_api = requests.get(recommendation_url, headers=headers)
        if recomendation_api.status_code != 200:
            failed_requests += 1
            print("-------------")
            print(recomendation_api.json())
        recommendation_resp = recomendation_api.json()
        print("================================")
        print(recommendation_resp)
        if len(recommendation_resp)!=0:
            print("Created")
        else:
            print("Not Creaded")
        all_end = time.time()
        final_time = all_end - hold_start
        print("final time",final_time)


        user_activity = requests.get("http://lms-rhz.collegedekho.com/1/lead/{}/activity/".format(lms_user_id),headers=headers)
        print(user_activity.json())

    
        
        
        conn = psycopg2.connect(
        host=gmu_host_live,
        database=gmu_databasename_live,
        user=gmu_username_live,
        password=gmu_pass_live)
        host=gmu_host_live,
        database=gmu_databasename_live,
        user=gmu_username_live,
        password=gmu_pass_live)
        print(conn)
        lms_query = ("""SELECT uup.added_on,
                            uup.id,
                            uup.name,
                            uup.email,
                            uup.phone_no,
                            uup.city_id,
                            uup.state_id,
                            uup.source_url,
                            ulp.preferred_level_id,
                            ups.stream_id,
                            upc.city_id AS "pref city",
                            upd.degree_id,
                            upst.state_id AS "pref state"
                        FROM gmu.users_leadprofile AS uup
                        LEFT JOIN gmu.users_leadpreferences AS ulp ON uup.id = ulp.lead_id
                        LEFT JOIN gmu.users_preferredstream AS ups ON ulp.id = ups.preferrence_id
                        LEFT JOIN gmu.users_preferredcity AS upc ON ulp.id = upc.preferrence_id
                        LEFT JOIN gmu.users_preferreddegree AS upd ON ulp.id = upd.preferrence_id
                        LEFT JOIN gmu.users_preferredstate AS upst ON ulp.id = upst.preferrence_id
                        WHERE uup.id = {}""".format(lms_user_id))
        cursor = conn.cursor()
        cursor.execute(lms_query)
        lms_row = cursor.fetchall()
        lms_result_dict = list(lms_row)

        print(lms_result_dict)

        # print(lms_result_dict)

        for i in lms_result_dict:
            lms_db_added_on = i[0]
            lms_db_user_id = i[1]
            lms_db_user_name = i[2]
            lms_db_user_email = i[3]
            lms_db_user_mobile = i[4]
            lms_db_city_id = [5]
            lms_db_state_id = i[6]
            lms_db_source_url = i[7]
            lms_db_pref_id = i[8]
            lms_db_level_id = i[9]
            lms_db_stream_id = i[10]
            lms_db_pref_city = i[11]
            lms_db_pref_degree_id = i[12]
            # lms_db_pref_state_id = i[13]

            print("Lead Added On in LMS : ",lms_db_added_on)
            print("Lead ID in LMS : ",lms_db_user_id)
            print("Lead Name in LMS : " ,lms_db_user_name)
            print("Lead Email in LMS : " ,lms_db_user_email)
            print("Lead Mobile in LMS : ",lms_db_user_mobile)


        stage_query = """select * from gmu.users_leadstage where lead_id = {}""".format(lms_user_id)
        cursor.execute(stage_query)
        stage_rules = cursor.fetchall()
        stage_dict = list(stage_rules)
        # print(stage_dict)

        for i in stage_dict:
            stage_ruleset_id = i[5]
            print("Stage id : ",stage_ruleset_id)

            if i[5] == 1:
                print("Fresh Lead")
            else:
                print("not Fresh lead")

        substage_query = """select * from gmu.users_leadsubstage where lead_id = {}""".format(lms_user_id)
        cursor.execute(substage_query)
        substage_rules = cursor.fetchall()
        substage_dict = list(substage_rules)
        print(substage_dict)

        for i in substage_dict:
            substage_ruleset_id = i[5]
            print("Substage_id :", substage_ruleset_id)

            if i[5] == 2:
                print("No Call Done")

            else :
                print(i[5])
                print("Status Differant")

            print(lms_db_user_id)
        
       
        
if __name__ == "__main__":
    unittest.main()