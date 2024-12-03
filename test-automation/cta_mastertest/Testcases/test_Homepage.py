import time
import requests
from selenium.webdriver.common.by import By
from common_functions import commonfunctions
from utilities.Readproperties import ReadConfig    
from utilities.customlogger import Logs
from common_functions import *
from database import *

class Test_HomePage(commonfunctions):
        
    
    baseUrl = ReadConfig.HomepageURL()

    def test_homepagecta(self, setup):
        self.logger = Logs.loggen('Test_HomePage')  # logger of current test case
        self.logger.info("******* Starting CTA TEST HOMEPAGE**********")
        
        # Initialize the 'driver' attribute
        self.driver = setup
        
        self.driver.get(self.baseUrl)
        self.logger.info("-------------------------")
        actual_title = self.driver.title
        self.logger.info(actual_title)
        if actual_title == "Find Top Colleges & Universities in India | Explore Courses, Exams, Admissions & Latest News":
            assert True
        else:
            assert False
        time.sleep(2)
        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        response = requests.get(current_url)
        self.logger.info("Response : " + str(response.status_code))
        time.sleep(1)
        scroll_element = self.driver.find_element(By.XPATH,"(//span[normalize-space()='Get in touch with our'])[1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
        time.sleep(1)
        random_name = random_namee()
        random_emaill = random_email()
        random_no = random_phonenumber()
        time.sleep(2)
        Name = self.driver.find_element(By.XPATH,"//input[@id='id_name']")
        Name.send_keys(random_name)
        self.logger.info(random_name)
        time.sleep(3)
        Email = self.driver.find_element(By.XPATH,"//input[@id='id_email']")
        Email.send_keys(random_emaill)
        self.logger.info(random_emaill)
        time.sleep(3)
        Phone_no = self.driver.find_element(By.XPATH,"//input[@id='id_phone']")
        Phone_no.send_keys(random_no)
        self.logger.info(random_no)
        time.sleep(3)
        footer_stream = Select(self.driver.find_element(By.XPATH, "//select[@id='id_stream']"))
        footer_stream.select_by_index(1)
        Stream = footer_stream.first_selected_option
        Stream_value = Stream.text
        self.logger.info("Stream : " + Stream_value)
        Submit_Button = self.driver.find_element(By.XPATH,"//input[@id='id_submit']")
        Submit_Button.click()
        time.sleep(3)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,random_no)
        time.sleep(480)
        sso_lead_ID, sso_name, sso_email, sso_phone_no = SSO_lead(self.logger,random_no)
        time.sleep(2)
        lms_lead_id, lms_name, lms_email, lms_phone_no, lms_source, lms_first_source, lms_city_id, lms_user_city, lms_state_id, lms_preferred_level, lms_preferred_specialization, lms_preferred_stream, lms_preferred_state, lms_preferred_degree, lms_preferred_city, lms_institute_id = lMS_lead(self.logger,random_no)
        time.sleep(2)
        sync_name, sync_phoneNo, sync_email, sync_first_source_URL, sync_city, sync_ip_city, sync_state, sync_level, sync_stream, sync_endpoint, sync_latitude, sync_longitude, sync_source_URL = pushlog_payload(self.logger, random_no)
        time.sleep(2)
        response_message = pushlog_response(self.logger, random_no)
        time.sleep(2)

            # Create a DataFrame with the results
        data = {
                'CTA' : [ 'Homepage' , 'Homepage' , 'Homepage', 'Homepage', 'Homepage', 'Homepage'],
                'Platforms' : ['Entered Lead','CLD','LMS', 'SSO', 'Payload', 'Response'],
                'Lead ID' : [ None, lead_id, lms_lead_id, sso_lead_ID, None, response_message],
                'Name': [random_name, lead_name, lms_name, sso_name, sync_name, None],
                'Email': [random_emaill, lead_email, lms_email, sso_email, sync_email, None],
                'Phone No': [random_no, lead_phone_no, lms_phone_no, sso_phone_no, sync_phoneNo, None],
                'Stream': [None, lead_stream_ID, lms_preferred_stream, None, sync_stream, None],
                'User State': [None, lead_state, lms_state_id, None, sync_state, None],
                'Preferred State': [None, lead_preferred_state, lms_preferred_state, None, None, None],
                'City ID' : [None, lead_city_ID, lms_city_id, None, sync_city, None],
                'User City': [None, lead_user_city, lms_user_city, None, sync_ip_city, None],
                'Preferred City' : [None, lead_preferred_city, lms_preferred_city, None, None, None],                
                'First Source URL': [None, lead_first_source_URL, lms_first_source, None, sync_first_source_URL, None],
                'Source_URL': [None, lead_Source_URL, lms_source, None, sync_source_URL, None],
                'Level': [None, lead_preferred_level, lms_preferred_level, None, sync_level, None],
                'Specialisation': [None, lead_preferred_specialization, lms_preferred_specialization, None, None, None],
                'Degree ID': [None, lead_degree_ID, lms_preferred_degree, None, None, None],
                'Preferred Institute': [None, lead_institute_Id, lms_institute_id, None, None, None],
                'Longitude': [None, None, None, None, sync_longitude, None],
                'Latitude': [None, None, None, None, sync_latitude, None]
            }
        
        df = pd.DataFrame(data)
        # Save DataFrame to CSV
        df.to_csv('homepage.csv', index=False)
        


