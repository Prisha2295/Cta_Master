from locust import HttpUser,task,between
import endpoint
import payloads
import unittest
# import uvicorn

class Lmsloadtest(HttpUser):
    wait_time = between(5,15)

    @task
    def task1(self):
        try:
            # print(payloads.sso_payloads())
            response = self.client.post(url = endpoint.sso_api,auth = None,headers = {'Authorization':'Token 2961f0aa05951161b5fbd69b936e33230735027c'},json = payloads.sso_payloads())
            if response.status_code != 200:
                json_data = response.json()
                print(json_data[id])
        except Exception as exc:
                print("Exception - ", exc)
                # json_data = response.json()

        print(response.content)
        try:
            resp = response.json()
            user_id = resp['id']
            print("Core User Created - ",user_id)
        except Exception as ex:
            print(ex, "exception")
        return user_id
    
    @task
    def task2(self):
        try:
            id = self.task1()
            lms_lead = self.client.get(endpoint.lms_api.format(id))
            if lms_lead.status_code != 200:
                print(lms_lead.json())
                print("Lead Created In Gmu LMS")

        except Exception as e:
             print("Lms lead Exception - ",e)

        print(lms_lead.json())


    @task
    def task3(self):
        try:
            login_api = self.client.post(endpoint.login_api,json = payloads.login_payloads())
            if login_api.status_code != 200:
                print(login_api.json())

        except Exception as ex:
            print("Login_api Exception",ex)

        loginaccess_token = login_api.json()
        access_token = loginaccess_token['access-token']
        print(access_token)

        access_header = {"Authorization": "Bearer {}".format(access_token)}
        
        user_id = self.task1()
        try:
            
            recommendation_api = self.client.get(url=endpoint.recommendation_api.format(user_id),headers=access_header)
            if recommendation_api.status_code != 200:
                print(recommendation_api.json())

        except Exception as recomm:
            print("Recommendation Exception",recomm)


        print(recommendation_api.json())
        
                   

            






