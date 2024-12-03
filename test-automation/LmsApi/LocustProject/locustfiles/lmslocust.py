from locust import HttpUser, task, between

# class WebsiteUser(HttpUser):
#     wait_time = between(5, 9)
#     lead_ids = [26297060,26598648] #26599292, 26599293, 26599294, 26599295, 26599296, 26599297, 26599298, 26599299, 26599300, 26599301, 26599302, 26599303, 26599304, 26599305, 26599306, 26599307, 26599308, 26599309, 26599310, 26599311, 26599312, 26599313, 26599314, 26599315, 26599316, 26599317, 26599318, 26599319, 26599320, 26599321, 26599322, 26599323, 26599324, 26599325, 26599326, 26599327, 26599328, 26599329, 26599330, 26599331, 26599332, 26599333, 26599334, 26599335, 26599336, 26599337, 26599338, 26599339, 26599340, 26599341, 26599342, 26599343, 26599344, 26599345, 26599346, 26599347, 26599348, 26599349, 26599350, 26599351, 26599352, 26599353, 26599354, 26599355, 26599356, 26599357, 26599358, 26599359, 26599360, 26599361, 26599362, 26599363, 26599364, 26599365]
#     @task
#     def login_api(self):
#         headers = {
#             "Content-Type": "application/json"
#         }
#         data = {
#             "phone_no": "8756365786",
#             "password": "dekho@123"
#         }
#         url = "https://sso.collegedekho.com/api/users/login?lms=True/api/users/login?lms=True"
#         self.client.post(url, json=data, headers=headers)

#     @task
#     def update_callback(self):
#         headers = {
#             "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4MTkzOTI5LCJpYXQiOjE3MTU2MDE5MjksImp0aSI6IjhhYmNjODczZDdhOTQxMGE5YTc0YTI4MWNjNjQ0YzE3IiwidXNlcl9pZCI6MzAzMjE0OTQsIm5hbWUiOiJzaGl2IHRlc3QgdCIsInBob25lX25vIjoiODc1NjM2NTc4NiIsImVtYWlsIjoiamtoamdqamtAampnamcuY2NjYyIsImlzX3N1cGVydXNlciI6ZmFsc2UsImlzX3N0YWZmIjp0cnVlLCJncm91cHMiOltdLCJwZXJtaXNzaW9ucyI6W10sImJ1Ijp7ImlkIjoxLCJuYW1lIjoiQ29sbGVnZWRla2hvIiwic2x1ZyI6ImNvbGxlZ2VkZWtobyJ9fQ.2HHY4tHvvWZSVR4o2CvCJfFW0N1J_MbHfZovumHlbuw",
#             "Content-Type": "application/json"
#         }
#         data = {
#             "substagename": "",
#             "category": "",
#             "intent": 3,
#             "next_callback_date": "2024-05-24",#change this
#             "next_callback_time": "11:09:00",#change this
#             "particular_slot": "10-11",#9-7
#             "sub_stage": "4",
#             "remarks": "",
#             "communication_type": "1",
#             "sub_stage_remarks": "",
#             "lead_ni_reason": None,
#             "institute_shortlist": None
#         }
#         for lead_id in self.lead_ids:
#             url = f"https://cache-locking-lms-lmshz.collegedekho.com/1/lead/{lead_id}/lead-callback/?stage_id=3"
#             self.client.post(url, json=data, headers=headers)
            

#     def on_start(self):
#         # Run login API once at the start of the test
#         self.login_api()


import random
from datetime import datetime, timedelta

lead_ids = [26599381,26599371] # List of lead IDs

class WebsiteUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def login_api(self):
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "phone_no": "8756365786",
            "password": "dekho@123"
        }
        url = "https://sso.collegedekho.com/api/users/login?lms=True/api/users/login?lms=True"
        self.client.post(url, json=data, headers=headers)

    # @task
    # def update_callback(self):
    #     headers = {
    #         "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4MTkzOTI5LCJpYXQiOjE3MTU2MDE5MjksImp0aSI6IjhhYmNjODczZDdhOTQxMGE5YTc0YTI4MWNjNjQ0YzE3IiwidXNlcl9pZCI6MzAzMjE0OTQsIm5hbWUiOiJzaGl2IHRlc3QgdCIsInBob25lX25vIjoiODc1NjM2NTc4NiIsImVtYWlsIjoiamtoamdqamtAampnamcuY2NjYyIsImlzX3N1cGVydXNlciI6ZmFsc2UsImlzX3N0YWZmIjp0cnVlLCJncm91cHMiOltdLCJwZXJtaXNzaW9ucyI6W10sImJ1Ijp7ImlkIjoxLCJuYW1lIjoiQ29sbGVnZWRla2hvIiwic2x1ZyI6ImNvbGxlZ2VkZWtobyJ9fQ.2HHY4tHvvWZSVR4o2CvCJfFW0N1J_MbHfZovumHlbuw",
    #         "Content-Type": "application/json"
    #     }
        
    #     # Generate random date within the specified range
    #     start_date = datetime(2024, 5, 16)
    #     end_date = datetime(2024, 9, 30)
    #     random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        
    #     # Generate random time within the specified range
    #     random_time = datetime.strptime(f"{random.randint(10, 11):02d}:{random.randint(0, 59):02d}:00", "%H:%M:%S").time()
        
    #     # Generate random slot within the specified range
    #     random_slot = random.choice(["9", "10", "11"])

    #     data = {
    #         "substagename": "",
    #         "category": "",
    #         "intent": 3,
    #         "next_callback_date": random_date.strftime("%Y-%m-%d"),
    #         "next_callback_time": random_time.strftime("%H:%M:%S"),
    #         "particular_slot": "10-11",
    #         "sub_stage": "4",
    #         "remarks": "",
    #         "communication_type": "1",
    #         "sub_stage_remarks": "",
    #         "lead_ni_reason": None,
    #         "institute_shortlist": None
    #     }
    #     print(data)
    #     for lead_id in lead_ids:
    #         url = f"https://cache-locking-lms-lmshz.collegedekho.com/1/lead/{lead_id}/lead-callback/?stage_id=3"
    #         self.client.post(url, json=data, headers=headers)

    def on_start(self):
        # Run login API once at the start of the test
        self.login_api()
