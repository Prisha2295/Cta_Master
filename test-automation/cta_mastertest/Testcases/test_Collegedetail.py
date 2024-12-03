import time
import requests
from selenium.webdriver.common.by import By
from common_functions import commonfunctions
from utilities.Readproperties import ReadConfig
from utilities.customlogger import Logs
from database import *

class Test_Collegedetail(commonfunctions):
        
    
    baseUrl = ReadConfig.CollegedetailURL()

    def test_collegedetailcta(self, setup):
        self.logger = Logs.loggen('Test Collegedetail')  # logger of current test case
        self.logger.info("******* Starting CTA TEST COLLEGEDETAIL**********")
        
        # Initialize the 'driver' attribute
        self.driver = setup
        
        self.driver.get(self.baseUrl)
        self.logger.info("-------------------------")
        actual_title = self.driver.title
        self.logger.info(actual_title)
        time.sleep(2)
        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        response = requests.get(current_url)
        self.logger.info("Response : " + str(response.status_code))
        time.sleep(2)

        # popup CTA
        
        self.driver.get(self.baseUrl)
        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(30)
        try:
            iframe = self.driver.find_element(By.XPATH,"//iframe[@id='webklipper-publisher-widget-container-notification-frame']")
            self.driver.switch_to.frame (iframe)
            time.sleep(2)
            close_admission_popup=self.driver.find_element(By.XPATH, "//i[@class='we_close']")
            close_admission_popup.click()
            time.sleep(2)
        except:
            pass
        popup_cta = self.driver.find_element(By.XPATH,"//h1[contains(text(),'Confused if this is the right college for you? Reg')]")
        time.sleep(2)
        popup_cta.click()
        time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(480)
        sso_lead_ID, sso_name, sso_email, sso_phone_no = SSO_lead(self.logger,entered_phone_no)
        time.sleep(2)
        lms_lead_id, lms_name, lms_email, lms_phone_no, lms_source, lms_first_source, lms_city_id, lms_user_city, lms_state_id, lms_preferred_level, lms_preferred_specialization, lms_preferred_stream, lms_preferred_state, lms_preferred_degree, lms_preferred_city, lms_institute_id = lMS_lead(self.logger,entered_phone_no)
        time.sleep(2)
        sync_name, sync_phoneNo, sync_email, sync_first_source_URL, sync_city, sync_ip_city, sync_state, sync_level, sync_stream, sync_endpoint, sync_latitude, sync_longitude, sync_source_URL = pushlog_payload(self.logger, entered_phone_no)
        time.sleep(2)
        response_message = pushlog_response(self.logger, entered_phone_no)
        time.sleep(2)

            # Create a DataFrame with the results
        data = {
                'CTA' : [ 'Popup' , 'Popup' , ' Popup', 'Popup', 'Popup', 'Popup'],
                'Platforms' : ['Entered Lead','CLD','LMS', 'SSO', 'Payload', 'Response'],
                'Lead ID' : [ None, lead_id, lms_lead_id, sso_lead_ID, None, response_message],
                'Name': [entered_name, lead_name, lms_name, sso_name, sync_name, None],
                'Email': [entered_email, lead_email, lms_email, sso_email, sync_email, None],
                'Phone No': [entered_phone_no, lead_phone_no, lms_phone_no, sso_phone_no, sync_phoneNo, None],
                'Stream': [entered_stream, lead_stream_ID, lms_preferred_stream, None, sync_stream, None],
                'User State': [entered_state, lead_state, lms_state_id, None, sync_state, None],
                'Preferred State': [None, lead_preferred_state, lms_preferred_state, None, None, None],
                'City ID' : [None, lead_city_ID, lms_city_id, None, sync_city, None],
                'User City': [entered_city, lead_user_city, lms_user_city, None, sync_ip_city, None],
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
        df.to_csv('collegedetail.csv', mode='a', header=False, index=False)

        if entered_name == lead_name:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_email == lead_email:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_phone_no == lead_phone_no:
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        profile_click.click()
        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(2)
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)

        # first CTA top

        get_free_counselling = self.driver.find_element(By.XPATH,"//button[@data-position='1']")
        time.sleep(2)
        get_free_counselling_text = get_free_counselling.text
        self.logger.info( "CTA Text : " + get_free_counselling_text)
        time.sleep(2)
        get_free_counselling.click()
        time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(480)
        sso_lead_ID, sso_name, sso_email, sso_phone_no = SSO_lead(self.logger,entered_phone_no)
        time.sleep(2)
        lms_lead_id, lms_name, lms_email, lms_phone_no, lms_source, lms_first_source, lms_city_id, lms_user_city, lms_state_id, lms_preferred_level, lms_preferred_specialization, lms_preferred_stream, lms_preferred_state, lms_preferred_degree, lms_preferred_city, lms_institute_id = lMS_lead(self.logger,entered_phone_no)
        time.sleep(2)
        sync_name, sync_phoneNo, sync_email, sync_first_source_URL, sync_city, sync_ip_city, sync_state, sync_level, sync_stream, sync_endpoint, sync_latitude, sync_longitude, sync_source_URL = pushlog_payload(self.logger, entered_phone_no)
        time.sleep(2)
        response_message = pushlog_response(self.logger, entered_phone_no)
        time.sleep(2)

            # Create a DataFrame with the results
        data = {
                'CTA' : [ get_free_counselling_text, get_free_counselling_text, get_free_counselling_text, get_free_counselling_text,get_free_counselling_text, get_free_counselling_text],
                'Platforms' : ['Entered Lead','CLD','LMS', 'SSO', 'Payload', 'Response'],
                'Lead ID' : [ None, lead_id, lms_lead_id, sso_lead_ID, None, response_message],
                'Name': [entered_name, lead_name, lms_name, sso_name, sync_name, None],
                'Email': [entered_email, lead_email, lms_email, sso_email, sync_email, None],
                'Phone No': [entered_phone_no, lead_phone_no, lms_phone_no, sso_phone_no, sync_phoneNo, None],
                'Stream': [entered_stream, lead_stream_ID, lms_preferred_stream, None, sync_stream, None],
                'User State': [entered_state, lead_state, lms_state_id, None, sync_state, None],
                'Preferred State': [None, lead_preferred_state, lms_preferred_state, None, None, None],
                'City ID' : [None, lead_city_ID, lms_city_id, None, sync_city, None],
                'User City': [entered_city, lead_user_city, lms_user_city, None, sync_ip_city, None],
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
        df.to_csv('collegedetail.csv', index=False)

        if entered_name == lead_name:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_email == lead_email:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_phone_no == lead_phone_no:
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        profile_click.click()
        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(2)
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)   

        #2nd CTA

        self.driver.get(self.baseUrl)
        time.sleep(2)
        apply_now = self.driver.find_element(By.XPATH,"//button[@data-position='2']")
        time.sleep(2)
        apply_now_text = apply_now.text
        self.logger.info( "CTA Text : " + apply_now_text)
        time.sleep(2)
        apply_now.click()
        time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(480)
        sso_lead_ID, sso_name, sso_email, sso_phone_no = SSO_lead(self.logger,entered_phone_no)
        time.sleep(2)
        lms_lead_id, lms_name, lms_email, lms_phone_no, lms_source, lms_first_source, lms_city_id, lms_user_city, lms_state_id, lms_preferred_level, lms_preferred_specialization, lms_preferred_stream, lms_preferred_state, lms_preferred_degree, lms_preferred_city, lms_institute_id = lMS_lead(self.logger,entered_phone_no)
        time.sleep(2)
        sync_name, sync_phoneNo, sync_email, sync_first_source_URL, sync_city, sync_ip_city, sync_state, sync_level, sync_stream, sync_endpoint, sync_latitude, sync_longitude, sync_source_URL = pushlog_payload(self.logger, entered_phone_no)
        time.sleep(2)
        response_message = pushlog_response(self.logger, entered_phone_no)
        time.sleep(2)

            # Create a DataFrame with the results
        data = {
                'CTA' : [ apply_now_text, apply_now_text, apply_now_text, apply_now_text,apply_now_text, apply_now_text],
                'Platforms' : ['Entered Lead','CLD','LMS', 'SSO', 'Payload', 'Response'],
                'Lead ID' : [ None, lead_id, lms_lead_id, sso_lead_ID, None, response_message],
                'Name': [entered_name, lead_name, lms_name, sso_name, sync_name, None],
                'Email': [entered_email, lead_email, lms_email, sso_email, sync_email, None],
                'Phone No': [entered_phone_no, lead_phone_no, lms_phone_no, sso_phone_no, sync_phoneNo, None],
                'Stream': [entered_stream, lead_stream_ID, lms_preferred_stream, None, sync_stream, None],
                'User State': [entered_state, lead_state, lms_state_id, None, sync_state, None],
                'Preferred State': [None, lead_preferred_state, lms_preferred_state, None, None, None],
                'City ID' : [None, lead_city_ID, lms_city_id, None, sync_city, None],
                'User City': [entered_city, lead_user_city, lms_user_city, None, sync_ip_city, None],
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
        df.to_csv('collegedetail.csv', mode='a', header=False, index=False)

        if entered_name == lead_name:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_email == lead_email:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_phone_no == lead_phone_no:
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        profile_click.click()
        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(2)
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)
        
        # Course shortlist CTA

        self.driver.get(self.baseUrl)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,4500)","")
        time.sleep(2)
        save_cta = self.driver.find_element(By.XPATH,"(//button[@id='btn-cta637'])[1]")
        time.sleep(2)
        save_cta_text = save_cta.text
        self.logger.info( "CTA Text : " + save_cta_text)
        time.sleep(2)
        save_cta.click()
        time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(480)
        sso_lead_ID, sso_name, sso_email, sso_phone_no = SSO_lead(self.logger,entered_phone_no)
        time.sleep(2)
        lms_lead_id, lms_name, lms_email, lms_phone_no, lms_source, lms_first_source, lms_city_id, lms_user_city, lms_state_id, lms_preferred_level, lms_preferred_specialization, lms_preferred_stream, lms_preferred_state, lms_preferred_degree, lms_preferred_city, lms_institute_id = lMS_lead(self.logger,entered_phone_no)
        time.sleep(2)
        sync_name, sync_phoneNo, sync_email, sync_first_source_URL, sync_city, sync_ip_city, sync_state, sync_level, sync_stream, sync_endpoint, sync_latitude, sync_longitude, sync_source_URL = pushlog_payload(self.logger, entered_phone_no)
        time.sleep(2)
        response_message = pushlog_response(self.logger, entered_phone_no)
        time.sleep(2)

            # Create a DataFrame with the results
        data = {
                'CTA' : [ save_cta_text, save_cta_text, save_cta_text, save_cta_text,save_cta_text, save_cta_text],
                'Platforms' : ['Entered Lead','CLD','LMS', 'SSO', 'Payload', 'Response'],
                'Lead ID' : [ None, lead_id, lms_lead_id, sso_lead_ID, None, response_message],
                'Name': [entered_name, lead_name, lms_name, sso_name, sync_name, None],
                'Email': [entered_email, lead_email, lms_email, sso_email, sync_email, None],
                'Phone No': [entered_phone_no, lead_phone_no, lms_phone_no, sso_phone_no, sync_phoneNo, None],
                'Stream': [entered_stream, lead_stream_ID, lms_preferred_stream, None, sync_stream, None],
                'User State': [entered_state, lead_state, lms_state_id, None, sync_state, None],
                'Preferred State': [None, lead_preferred_state, lms_preferred_state, None, None, None],
                'City ID' : [None, lead_city_ID, lms_city_id, None, sync_city, None],
                'User City': [entered_city, lead_user_city, lms_user_city, None, sync_ip_city, None],
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
        df.to_csv('collegedetail.csv', mode='a', header=False, index=False)

        if entered_name == lead_name:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_email == lead_email:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_phone_no == lead_phone_no:
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        profile_click.click()
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)

        # get expert help

        self.driver.get(self.baseUrl)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,5100)","")
        time.sleep(2)
        get_expert_help_cta = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Connect Now'])[1]")
        time.sleep(2)
        get_expert_help_cta_text = get_expert_help_cta.text
        self.logger.info( "CTA Text : " + get_expert_help_cta_text)
        time.sleep(2)
        get_expert_help_cta.click()
        time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(480)
        sso_lead_ID, sso_name, sso_email, sso_phone_no = SSO_lead(self.logger,entered_phone_no)
        time.sleep(2)
        lms_lead_id, lms_name, lms_email, lms_phone_no, lms_source, lms_first_source, lms_city_id, lms_user_city, lms_state_id, lms_preferred_level, lms_preferred_specialization, lms_preferred_stream, lms_preferred_state, lms_preferred_degree, lms_preferred_city, lms_institute_id = lMS_lead(self.logger,entered_phone_no)
        time.sleep(2)
        sync_name, sync_phoneNo, sync_email, sync_first_source_URL, sync_city, sync_ip_city, sync_state, sync_level, sync_stream, sync_endpoint, sync_latitude, sync_longitude, sync_source_URL = pushlog_payload(self.logger, entered_phone_no)
        time.sleep(2)
        response_message = pushlog_response(self.logger, entered_phone_no)
        time.sleep(2)

            # Create a DataFrame with the results
        data = {
                'CTA' : [ get_expert_help_cta_text, get_expert_help_cta_text, get_expert_help_cta_text, get_expert_help_cta_text,get_expert_help_cta_text, get_expert_help_cta_text],
                'Platforms' : ['Entered Lead','CLD','LMS', 'SSO', 'Payload', 'Response'],
                'Lead ID' : [ None, lead_id, lms_lead_id, sso_lead_ID, None, response_message],
                'Name': [entered_name, lead_name, lms_name, sso_name, sync_name, None],
                'Email': [entered_email, lead_email, lms_email, sso_email, sync_email, None],
                'Phone No': [entered_phone_no, lead_phone_no, lms_phone_no, sso_phone_no, sync_phoneNo, None],
                'Stream': [entered_stream, lead_stream_ID, lms_preferred_stream, None, sync_stream, None],
                'User State': [entered_state, lead_state, lms_state_id, None, sync_state, None],
                'Preferred State': [None, lead_preferred_state, lms_preferred_state, None, None, None],
                'City ID' : [None, lead_city_ID, lms_city_id, None, sync_city, None],
                'User City': [entered_city, lead_user_city, lms_user_city, None, sync_ip_city, None],
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
        df.to_csv('collegedetail.csv', mode='a', header=False, index=False)

        if entered_name == lead_name:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_email == lead_email:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_phone_no == lead_phone_no:
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        time.sleep(2)
        profile_click.click()
        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(2)
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)

        #3rd CTA

        self.driver.get(self.baseUrl)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,800)","")
        time.sleep(2)
        request_a_callback = self.driver.find_element(By.XPATH,"//button[@data-position='7']")
        time.sleep(2)
        request_a_callback_text = request_a_callback.text
        self.logger.info( "CTA Text : " + request_a_callback_text)
        time.sleep(2)
        request_a_callback.click()
        time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(480)
        sso_lead_ID, sso_name, sso_email, sso_phone_no = SSO_lead(self.logger,entered_phone_no)
        time.sleep(2)
        lms_lead_id, lms_name, lms_email, lms_phone_no, lms_source, lms_first_source, lms_city_id, lms_user_city, lms_state_id, lms_preferred_level, lms_preferred_specialization, lms_preferred_stream, lms_preferred_state, lms_preferred_degree, lms_preferred_city, lms_institute_id = lMS_lead(self.logger,entered_phone_no)
        time.sleep(2)
        sync_name, sync_phoneNo, sync_email, sync_first_source_URL, sync_city, sync_ip_city, sync_state, sync_level, sync_stream, sync_endpoint, sync_latitude, sync_longitude, sync_source_URL = pushlog_payload(self.logger, entered_phone_no)
        time.sleep(2)
        response_message = pushlog_response(self.logger, entered_phone_no)
        time.sleep(2)

            # Create a DataFrame with the results
        data = {
                'CTA' : [ request_a_callback_text, request_a_callback_text, request_a_callback_text, request_a_callback_text,request_a_callback_text, request_a_callback_text],
                'Platforms' : ['Entered Lead','CLD','LMS', 'SSO', 'Payload', 'Response'],
                'Lead ID' : [ None, lead_id, lms_lead_id, sso_lead_ID, None, response_message],
                'Name': [entered_name, lead_name, lms_name, sso_name, sync_name, None],
                'Email': [entered_email, lead_email, lms_email, sso_email, sync_email, None],
                'Phone No': [entered_phone_no, lead_phone_no, lms_phone_no, sso_phone_no, sync_phoneNo, None],
                'Stream': [entered_stream, lead_stream_ID, lms_preferred_stream, None, sync_stream, None],
                'User State': [entered_state, lead_state, lms_state_id, None, sync_state, None],
                'Preferred State': [None, lead_preferred_state, lms_preferred_state, None, None, None],
                'City ID' : [None, lead_city_ID, lms_city_id, None, sync_city, None],
                'User City': [entered_city, lead_user_city, lms_user_city, None, sync_ip_city, None],
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
        df.to_csv('collegedetail.csv', mode='a', header=False, index=False)

        if entered_name == lead_name:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_email == lead_email:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_phone_no == lead_phone_no:
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        profile_click.click()
        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(2)
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)

        #4th CTA

        self.driver.get(self.baseUrl)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,800)","")
        time.sleep(2)
        check_eligibility = self.driver.find_element(By.XPATH,"//button[@data-position='8']")
        time.sleep(2)
        check_eligibility_text = check_eligibility.text
        self.logger.info( "CTA Text : " + check_eligibility_text)
        time.sleep(2)
        check_eligibility.click()
        time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(480)
        sso_lead_ID, sso_name, sso_email, sso_phone_no = SSO_lead(self.logger,entered_phone_no)
        time.sleep(2)
        lms_lead_id, lms_name, lms_email, lms_phone_no, lms_source, lms_first_source, lms_city_id, lms_user_city, lms_state_id, lms_preferred_level, lms_preferred_specialization, lms_preferred_stream, lms_preferred_state, lms_preferred_degree, lms_preferred_city, lms_institute_id = lMS_lead(self.logger,entered_phone_no)
        time.sleep(2)
        sync_name, sync_phoneNo, sync_email, sync_first_source_URL, sync_city, sync_ip_city, sync_state, sync_level, sync_stream, sync_endpoint, sync_latitude, sync_longitude, sync_source_URL = pushlog_payload(self.logger, entered_phone_no)
        time.sleep(2)
        response_message = pushlog_response(self.logger, entered_phone_no)
        time.sleep(2)

            # Create a DataFrame with the results
        data = {
                'CTA' : [ check_eligibility_text, check_eligibility_text, check_eligibility_text, check_eligibility_text,check_eligibility_text, check_eligibility_text],
                'Platforms' : ['Entered Lead','CLD','LMS', 'SSO', 'Payload', 'Response'],
                'Lead ID' : [ None, lead_id, lms_lead_id, sso_lead_ID, None, response_message],
                'Name': [entered_name, lead_name, lms_name, sso_name, sync_name, None],
                'Email': [entered_email, lead_email, lms_email, sso_email, sync_email, None],
                'Phone No': [entered_phone_no, lead_phone_no, lms_phone_no, sso_phone_no, sync_phoneNo, None],
                'Stream': [entered_stream, lead_stream_ID, lms_preferred_stream, None, sync_stream, None],
                'User State': [entered_state, lead_state, lms_state_id, None, sync_state, None],
                'Preferred State': [None, lead_preferred_state, lms_preferred_state, None, None, None],
                'City ID' : [None, lead_city_ID, lms_city_id, None, sync_city, None],
                'User City': [entered_city, lead_user_city, lms_user_city, None, sync_ip_city, None],
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
        df.to_csv('collegedetail.csv', mode='a', header=False, index=False)

        if entered_name == lead_name:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_email == lead_email:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_phone_no == lead_phone_no:
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        profile_click.click()
        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(2)
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)


        # course tab

        self.driver.get(self.baseUrl)
        time.sleep(2)
        course_tab=self.driver.find_element(By.XPATH,"//a[normalize-space()='Courses']")
        course_tab.click()
        time.sleep(2)
        get_free_counselling = self.driver.find_element(By.XPATH,"//button[@data-position='1']")
        time.sleep(2)
        get_free_counselling_text = get_free_counselling.text
        self.logger.info( "CTA Text : " + get_free_counselling_text)
        time.sleep(2)
        get_free_counselling.click()
        time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(480)
        sso_lead_ID, sso_name, sso_email, sso_phone_no = SSO_lead(self.logger,entered_phone_no)
        time.sleep(2)
        lms_lead_id, lms_name, lms_email, lms_phone_no, lms_source, lms_first_source, lms_city_id, lms_user_city, lms_state_id, lms_preferred_level, lms_preferred_specialization, lms_preferred_stream, lms_preferred_state, lms_preferred_degree, lms_preferred_city, lms_institute_id = lMS_lead(self.logger,entered_phone_no)
        time.sleep(2)
        sync_name, sync_phoneNo, sync_email, sync_first_source_URL, sync_city, sync_ip_city, sync_state, sync_level, sync_stream, sync_endpoint, sync_latitude, sync_longitude, sync_source_URL = pushlog_payload(self.logger, entered_phone_no)
        time.sleep(2)
        response_message = pushlog_response(self.logger, entered_phone_no)
        time.sleep(2)

            # Create a DataFrame with the results
        data = {
                'CTA' : [ get_free_counselling_text, get_free_counselling_text, get_free_counselling_text, get_free_counselling_text,get_free_counselling_text, get_free_counselling_text],
                'Platforms' : ['Entered Lead','CLD','LMS', 'SSO', 'Payload', 'Response'],
                'Lead ID' : [ None, lead_id, lms_lead_id, sso_lead_ID, None, response_message],
                'Name': [entered_name, lead_name, lms_name, sso_name, sync_name, None],
                'Email': [entered_email, lead_email, lms_email, sso_email, sync_email, None],
                'Phone No': [entered_phone_no, lead_phone_no, lms_phone_no, sso_phone_no, sync_phoneNo, None],
                'Stream': [entered_stream, lead_stream_ID, lms_preferred_stream, None, sync_stream, None],
                'User State': [entered_state, lead_state, lms_state_id, None, sync_state, None],
                'Preferred State': [None, lead_preferred_state, lms_preferred_state, None, None, None],
                'City ID' : [None, lead_city_ID, lms_city_id, None, sync_city, None],
                'User City': [entered_city, lead_user_city, lms_user_city, None, sync_ip_city, None],
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
        df.to_csv('collegedetail.csv', mode='a', header=False, index=False)
        if entered_name == lead_name:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_email == lead_email:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_phone_no == lead_phone_no:
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        profile_click.click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(2)
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        time.sleep(2)
        logout_click.click()
        time.sleep(5)   

        # course tab apply now

        self.driver.get(self.baseUrl)
        time.sleep(2)
        course_tab=self.driver.find_element(By.XPATH,"//a[normalize-space()='Courses']")
        course_tab.click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,3900)","")
        time.sleep(2)
        course_tab_apply_now_cta = self.driver.find_element(By.XPATH,"(//button[contains(text(),'Apply Now')])[2]")
        time.sleep(2)
        course_tab_apply_now_cta_text = course_tab_apply_now_cta.text
        self.logger.info( "CTA Text : " + course_tab_apply_now_cta_text)
        time.sleep(2)
        course_tab_apply_now_cta.click()
        time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(480)
        sso_lead_ID, sso_name, sso_email, sso_phone_no = SSO_lead(self.logger,entered_phone_no)
        time.sleep(2)
        lms_lead_id, lms_name, lms_email, lms_phone_no, lms_source, lms_first_source, lms_city_id, lms_user_city, lms_state_id, lms_preferred_level, lms_preferred_specialization, lms_preferred_stream, lms_preferred_state, lms_preferred_degree, lms_preferred_city, lms_institute_id = lMS_lead(self.logger,entered_phone_no)
        time.sleep(2)
        sync_name, sync_phoneNo, sync_email, sync_first_source_URL, sync_city, sync_ip_city, sync_state, sync_level, sync_stream, sync_endpoint, sync_latitude, sync_longitude, sync_source_URL = pushlog_payload(self.logger, entered_phone_no)
        time.sleep(2)
        response_message = pushlog_response(self.logger, entered_phone_no)
        time.sleep(2)

            # Create a DataFrame with the results
        data = {
                'CTA' : [ course_tab_apply_now_cta_text, course_tab_apply_now_cta_text, course_tab_apply_now_cta_text, course_tab_apply_now_cta_text,course_tab_apply_now_cta_text, course_tab_apply_now_cta_text],
                'Platforms' : ['Entered Lead','CLD','LMS', 'SSO', 'Payload', 'Response'],
                'Lead ID' : [ None, lead_id, lms_lead_id, sso_lead_ID, None, response_message],
                'Name': [entered_name, lead_name, lms_name, sso_name, sync_name, None],
                'Email': [entered_email, lead_email, lms_email, sso_email, sync_email, None],
                'Phone No': [entered_phone_no, lead_phone_no, lms_phone_no, sso_phone_no, sync_phoneNo, None],
                'Stream': [entered_stream, lead_stream_ID, lms_preferred_stream, None, sync_stream, None],
                'User State': [entered_state, lead_state, lms_state_id, None, sync_state, None],
                'Preferred State': [None, lead_preferred_state, lms_preferred_state, None, None, None],
                'City ID' : [None, lead_city_ID, lms_city_id, None, sync_city, None],
                'User City': [entered_city, lead_user_city, lms_user_city, None, sync_ip_city, None],
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
        df.to_csv('collegedetail.csv', mode='a', header=False, index=False)

        if entered_name == lead_name:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_email == lead_email:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_phone_no == lead_phone_no:
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        profile_click.click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(2)
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)

        #course tab request callback

        self.driver.get(self.baseUrl)
        time.sleep(2)
        course_tab=self.driver.find_element(By.XPATH,"//a[normalize-space()='Courses']")
        course_tab.click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,12900)","")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,-200)","")
        time.sleep(2)
        course_tab_request_callback = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Request a Call Back'])[1]")
        time.sleep(2)
        course_tab_request_callback_text = course_tab_request_callback.text
        self.logger.info( "CTA Text : " + course_tab_request_callback_text)
        time.sleep(2)
        course_tab_request_callback.click()
        time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(480)
        sso_lead_ID, sso_name, sso_email, sso_phone_no = SSO_lead(self.logger,entered_phone_no)
        time.sleep(2)
        lms_lead_id, lms_name, lms_email, lms_phone_no, lms_source, lms_first_source, lms_city_id, lms_user_city, lms_state_id, lms_preferred_level, lms_preferred_specialization, lms_preferred_stream, lms_preferred_state, lms_preferred_degree, lms_preferred_city, lms_institute_id = lMS_lead(self.logger,entered_phone_no)
        time.sleep(2)
        sync_name, sync_phoneNo, sync_email, sync_first_source_URL, sync_city, sync_ip_city, sync_state, sync_level, sync_stream, sync_endpoint, sync_latitude, sync_longitude, sync_source_URL = pushlog_payload(self.logger, entered_phone_no)
        time.sleep(2)
        response_message = pushlog_response(self.logger, entered_phone_no)
        time.sleep(2)

            # Create a DataFrame with the results
        data = {
                'CTA' : [ course_tab_request_callback_text, course_tab_request_callback_text, course_tab_request_callback_text, course_tab_request_callback_text,course_tab_request_callback_text, course_tab_request_callback_text],
                'Platforms' : ['Entered Lead','CLD','LMS', 'SSO', 'Payload', 'Response'],
                'Lead ID' : [ None, lead_id, lms_lead_id, sso_lead_ID, None, response_message],
                'Name': [entered_name, lead_name, lms_name, sso_name, sync_name, None],
                'Email': [entered_email, lead_email, lms_email, sso_email, sync_email, None],
                'Phone No': [entered_phone_no, lead_phone_no, lms_phone_no, sso_phone_no, sync_phoneNo, None],
                'Stream': [entered_stream, lead_stream_ID, lms_preferred_stream, None, sync_stream, None],
                'User State': [entered_state, lead_state, lms_state_id, None, sync_state, None],
                'Preferred State': [None, lead_preferred_state, lms_preferred_state, None, None, None],
                'City ID' : [None, lead_city_ID, lms_city_id, None, sync_city, None],
                'User City': [entered_city, lead_user_city, lms_user_city, None, sync_ip_city, None],
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
        df.to_csv('collegedetail.csv', mode='a', header=False, index=False)

        if entered_name == lead_name:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_email == lead_email:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_phone_no == lead_phone_no:
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        profile_click.click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(2)
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)

        #admission requirements

        self.driver.get(self.baseUrl)
        time.sleep(2)
        admission_tab=self.driver.find_element(By.XPATH,"(//a[normalize-space()='Admission'])[1]")
        admission_tab.click()
        time.sleep(2)
        see_admission_requirements = self.driver.find_element(By.XPATH,"(//button[normalize-space()='See Admission Requirements'])[1]")
        time.sleep(2)
        see_admission_requirements_text = see_admission_requirements.text
        self.logger.info( "CTA Text : " + see_admission_requirements_text)
        time.sleep(2)
        see_admission_requirements.click()
        time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(480)
        sso_lead_ID, sso_name, sso_email, sso_phone_no = SSO_lead(self.logger,entered_phone_no)
        time.sleep(2)
        lms_lead_id, lms_name, lms_email, lms_phone_no, lms_source, lms_first_source, lms_city_id, lms_user_city, lms_state_id, lms_preferred_level, lms_preferred_specialization, lms_preferred_stream, lms_preferred_state, lms_preferred_degree, lms_preferred_city, lms_institute_id = lMS_lead(self.logger,entered_phone_no)
        time.sleep(2)
        sync_name, sync_phoneNo, sync_email, sync_first_source_URL, sync_city, sync_ip_city, sync_state, sync_level, sync_stream, sync_endpoint, sync_latitude, sync_longitude, sync_source_URL = pushlog_payload(self.logger, entered_phone_no)
        time.sleep(2)
        response_message = pushlog_response(self.logger, entered_phone_no)
        time.sleep(2)


            # Create a DataFrame with the results
        data = {
                'CTA' : [ see_admission_requirements_text, see_admission_requirements_text, see_admission_requirements_text, see_admission_requirements_text,see_admission_requirements_text, see_admission_requirements_text],
                'Platforms' : ['Entered Lead','CLD','LMS', 'SSO', 'Payload', 'Response'],
                'Lead ID' : [ None, lead_id, lms_lead_id, sso_lead_ID, None, response_message],
                'Name': [entered_name, lead_name, lms_name, sso_name, sync_name, None],
                'Email': [entered_email, lead_email, lms_email, sso_email, sync_email, None],
                'Phone No': [entered_phone_no, lead_phone_no, lms_phone_no, sso_phone_no, sync_phoneNo, None],
                'Stream': [entered_stream, lead_stream_ID, lms_preferred_stream, None, sync_stream, None],
                'User State': [entered_state, lead_state, lms_state_id, None, sync_state, None],
                'Preferred State': [None, lead_preferred_state, lms_preferred_state, None, None, None],
                'City ID' : [None, lead_city_ID, lms_city_id, None, sync_city, None],
                'User City': [entered_city, lead_user_city, lms_user_city, None, sync_ip_city, None],
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
        df.to_csv('collegedetail.csv', mode='a', header=False, index=False)

        if entered_name == lead_name:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_email == lead_email:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_phone_no == lead_phone_no:
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        time.sleep(2)
        profile_click.click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(2)
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)

        #scholarship details

        self.driver.get(self.baseUrl)
        time.sleep(2)
        scholarship_tab =self.driver.find_element(By.XPATH,"(//a[normalize-space()='Scholarship'])[1]")
        scholarship_tab.click()
        time.sleep(2)
        get_scholarship_details = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Get Scholarship Details'])[1]")
        time.sleep(2)
        get_scholarship_details_text = get_scholarship_details.text
        self.logger.info( "CTA Text : " + get_scholarship_details_text)
        time.sleep(2)
        get_scholarship_details.click()
        time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(480)
        sso_lead_ID, sso_name, sso_email, sso_phone_no = SSO_lead(self.logger,entered_phone_no)
        time.sleep(2)
        lms_lead_id, lms_name, lms_email, lms_phone_no, lms_source, lms_first_source, lms_city_id, lms_user_city, lms_state_id, lms_preferred_level, lms_preferred_specialization, lms_preferred_stream, lms_preferred_state, lms_preferred_degree, lms_preferred_city, lms_institute_id = lMS_lead(self.logger,entered_phone_no)
        time.sleep(2)
        sync_name, sync_phoneNo, sync_email, sync_first_source_URL, sync_city, sync_ip_city, sync_state, sync_level, sync_stream, sync_endpoint, sync_latitude, sync_longitude, sync_source_URL = pushlog_payload(self.logger, entered_phone_no)
        time.sleep(2)
        response_message = pushlog_response(self.logger, entered_phone_no)
        time.sleep(2)

            # Create a DataFrame with the results
        data = {
                'CTA' : [ get_scholarship_details_text, get_scholarship_details_text, get_scholarship_details_text, get_scholarship_details_text,get_scholarship_details_text, get_scholarship_details_text],
                'Platforms' : ['Entered Lead','CLD','LMS', 'SSO', 'Payload', 'Response'],
                'Lead ID' : [ None, lead_id, lms_lead_id, sso_lead_ID, None, response_message],
                'Name': [entered_name, lead_name, lms_name, sso_name, sync_name, None],
                'Email': [entered_email, lead_email, lms_email, sso_email, sync_email, None],
                'Phone No': [entered_phone_no, lead_phone_no, lms_phone_no, sso_phone_no, sync_phoneNo, None],
                'Stream': [entered_stream, lead_stream_ID, lms_preferred_stream, None, sync_stream, None],
                'User State': [entered_state, lead_state, lms_state_id, None, sync_state, None],
                'Preferred State': [None, lead_preferred_state, lms_preferred_state, None, None, None],
                'City ID' : [None, lead_city_ID, lms_city_id, None, sync_city, None],
                'User City': [entered_city, lead_user_city, lms_user_city, None, sync_ip_city, None],
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
        df.to_csv('collegedetail.csv', mode='a', header=False, index=False)
        if entered_name == lead_name:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_email == lead_email:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_phone_no == lead_phone_no:
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        time.sleep(2)
        profile_click.click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(2)
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)

        #placement report

        self.driver.get(self.baseUrl)
        time.sleep(2)
        placement_tab =self.driver.find_element(By.XPATH,"(//a[normalize-space()='Placements'])[1]")
        placement_tab.click()
        time.sleep(10)
        get_placement_report = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Download Placement Report'])[1]")
        time.sleep(2)
        get_placement_report_text = get_placement_report.text
        self.logger.info( "CTA Text : " + get_placement_report_text)
        time.sleep(2)
        get_placement_report.click()
        time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(480)
        sso_lead_ID, sso_name, sso_email, sso_phone_no = SSO_lead(self.logger,entered_phone_no)
        time.sleep(2)
        lms_lead_id, lms_name, lms_email, lms_phone_no, lms_source, lms_first_source, lms_city_id, lms_user_city, lms_state_id, lms_preferred_level, lms_preferred_specialization, lms_preferred_stream, lms_preferred_state, lms_preferred_degree, lms_preferred_city, lms_institute_id = lMS_lead(self.logger,entered_phone_no)
        time.sleep(2)
        sync_name, sync_phoneNo, sync_email, sync_first_source_URL, sync_city, sync_ip_city, sync_state, sync_level, sync_stream, sync_endpoint, sync_latitude, sync_longitude, sync_source_URL = pushlog_payload(self.logger, entered_phone_no)
        time.sleep(2)
        response_message = pushlog_response(self.logger, entered_phone_no)
        time.sleep(2)

            # Create a DataFrame with the results
        data = {
                'CTA' : [ get_placement_report_text, get_placement_report_text, get_placement_report_text, get_placement_report_text,get_placement_report_text, get_placement_report_text],
                'Platforms' : ['Entered Lead','CLD','LMS', 'SSO', 'Payload', 'Response'],
                'Lead ID' : [ None, lead_id, lms_lead_id, sso_lead_ID, None, response_message],
                'Name': [entered_name, lead_name, lms_name, sso_name, sync_name, None],
                'Email': [entered_email, lead_email, lms_email, sso_email, sync_email, None],
                'Phone No': [entered_phone_no, lead_phone_no, lms_phone_no, sso_phone_no, sync_phoneNo, None],
                'Stream': [entered_stream, lead_stream_ID, lms_preferred_stream, None, sync_stream, None],
                'User State': [entered_state, lead_state, lms_state_id, None, sync_state, None],
                'Preferred State': [None, lead_preferred_state, lms_preferred_state, None, None, None],
                'City ID' : [None, lead_city_ID, lms_city_id, None, sync_city, None],
                'User City': [entered_city, lead_user_city, lms_user_city, None, sync_ip_city, None],
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
        df.to_csv('collegedetail.csv', mode='a', header=False, index=False)

        if entered_name == lead_name:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_email == lead_email:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_phone_no == lead_phone_no:
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        time.sleep(2)
        profile_click.click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(2)
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)

        #cutoff details

        self.driver.get(self.baseUrl)
        time.sleep(2)
        cutoff_tab =self.driver.find_element(By.XPATH,"(//a[normalize-space()='CutOffs'])[1]")
        cutoff_tab.click()
        time.sleep(2)
        get_cutoff_details = self.driver.find_element(By.XPATH,"(//button[normalize-space()='View Detailed Cut Off'])[1]")
        time.sleep(2)
        get_cutoff_details_text = get_cutoff_details.text
        self.logger.info( "CTA Text : " + get_cutoff_details_text)
        time.sleep(2)
        get_cutoff_details.click()
        time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(480)
        sso_lead_ID, sso_name, sso_email, sso_phone_no = SSO_lead(self.logger,entered_phone_no)
        time.sleep(2)
        lms_lead_id, lms_name, lms_email, lms_phone_no, lms_source, lms_first_source, lms_city_id, lms_user_city, lms_state_id, lms_preferred_level, lms_preferred_specialization, lms_preferred_stream, lms_preferred_state, lms_preferred_degree, lms_preferred_city, lms_institute_id = lMS_lead(self.logger,entered_phone_no)
        time.sleep(2)
        sync_name, sync_phoneNo, sync_email, sync_first_source_URL, sync_city, sync_ip_city, sync_state, sync_level, sync_stream, sync_endpoint, sync_latitude, sync_longitude, sync_source_URL = pushlog_payload(self.logger, entered_phone_no)
        time.sleep(2)
        response_message = pushlog_response(self.logger, entered_phone_no)
        time.sleep(2)

        # Create a DataFrame with the results
        data = {
                'CTA' : [ get_cutoff_details_text, get_cutoff_details_text, get_cutoff_details_text, get_cutoff_details_text,get_cutoff_details_text, get_cutoff_details_text],
                'Platforms' : ['Entered Lead','CLD','LMS', 'SSO', 'Payload', 'Response'],
                'Lead ID' : [ None, lead_id, lms_lead_id, sso_lead_ID, None, response_message],
                'Name': [entered_name, lead_name, lms_name, sso_name, sync_name, None],
                'Email': [entered_email, lead_email, lms_email, sso_email, sync_email, None],
                'Phone No': [entered_phone_no, lead_phone_no, lms_phone_no, sso_phone_no, sync_phoneNo, None],
                'Stream': [entered_stream, lead_stream_ID, lms_preferred_stream, None, sync_stream, None],
                'User State': [entered_state, lead_state, lms_state_id, None, sync_state, None],
                'Preferred State': [None, lead_preferred_state, lms_preferred_state, None, None, None],
                'City ID' : [None, lead_city_ID, lms_city_id, None, sync_city, None],
                'User City': [entered_city, lead_user_city, lms_user_city, None, sync_ip_city, None],
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
        df.to_csv('collegedetail.csv', mode='a', header=False, index=False)
        if entered_name == lead_name:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_email == lead_email:
            assert True
        else:
            assert False
        time.sleep(2)
        if entered_phone_no == lead_phone_no:
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)

        # footer form

        self.driver.execute_script("window.scrollBy(0,10500)","")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,3700)","")
        time.sleep(2)
        self.footerform()
    

        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        time.sleep(2)
        profile_click.click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(2)
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)