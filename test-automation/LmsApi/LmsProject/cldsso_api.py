import time
import unittest
import requests
import mysql.connector
from payloads import Attributes


class Test(unittest.TestCase):
    def test_write_csv_file(self):




        # url = "https://staging-hz.collegedekho.com/api/v2/ctasubmission"
        # payload={'cta': '3',
        # 'button': '3',
        # 'email': 'kgjfkhg@cld.com',
        # 'phone': '8593849939',
        # 'name': 'khrkjh'}
        # # headers = {
        # # 'Cookie': 'csrftoken=QBEB9MOvWiIqpoQx15ESaR0HQ4eT2fZyG9U9UzOgEaypYq5fQOjpIy4ZMJsXHxb6; sessionid=nhexs35p2a6bldiq1czpyl1eh83o0397'
        # # }
        # # headers = {"content-type": "application/json"}
        # response = requests.request("POST", url, data=payload)

        # print(response.text)
        # return

        # Number of requests to make
        number_of_requests = 1

        # Keep track of failed requests
        failed_requests = 0

        url = "https://staging-hz.collegedekho.com/api/v2/ctasubmission"
            
        for i in range(number_of_requests):
            count = 0
            payload = Attributes().cld_ctasubmission()
            # headers = {'Content-Type': 'application/json'}
            for payloads in payload:
                
                # print(payloads)
                try:
                    response = requests.post(url,data= payloads)
                    print(response.status_code)
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
                resp = response.text
                print(resp)
        #         user_id = resp['id']
        #         user_name = resp['name']
        #         user_mobile = resp['phone_no']
        #         vertical = resp['business_unit']
        #         groups = resp['groups']
        #         print('User_id : ',user_id)
        #         print('User_name : ' ,user_name)
        #         print('User_mobile : ',user_mobile)
        #         print('Business Unit : ',vertical)
        #         print('Groups : ',groups)
        #         time.sleep(2)
        # print(conn)
                
        
if __name__ == "__main__":
    unittest.main()