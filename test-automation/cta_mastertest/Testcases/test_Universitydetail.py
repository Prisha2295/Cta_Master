import time
import requests
# import sys
# sys.path.append('/home/praveenyadav/Desktop/Desktop/test-automation/cta_mastertest')
from selenium.webdriver.common.by import By
from database import *
from common_functions import commonfunctions
from utilities.Readproperties import ReadConfig
    
from utilities.customlogger import Logs

class Test_Universitydetail(commonfunctions):
        
    
    baseUrl = ReadConfig.UniversitydetailURL()

    def test_universitydetailcta(self, setup):
        self.logger = Logs.loggen('Test Universitydetail')  # logger of current test case
        self.logger.info("******* Starting CTA TEST UNIVERSITYDETAIL**********")
        
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
        get_free_counselling_university = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Get Free Counselling'])[1]")
        time.sleep(2)
        get_free_counselling_university_text = get_free_counselling_university.text
        self.logger.info( "CTA Text : " + get_free_counselling_university_text)
        time.sleep(2)
        get_free_counselling_university.click()
        time.sleep(2)
        # self.name_negative()
        # time.sleep(2)
        # self.name_positive()
        # time.sleep(2)
        # self.email_negative()
        # time.sleep(2)
        # self.email_positive()
        # time.sleep(2)
        # self.stream_negative()
        # time.sleep(2)
        # self.stream_positive()
        # time.sleep(2)
        # self.level_negative()
        # time.sleep(2)
        # self.level_positive()
        # time.sleep(2)
        # self.state_negative()
        # time.sleep(2)
        # self.state_positive()
        # time.sleep(2)
        # self.mobile_negative()
        # time.sleep(2)
        # self.mobile_positive()
        # time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
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
                'CTA' : [ get_free_counselling_university_text, get_free_counselling_university_text, get_free_counselling_university_text, get_free_counselling_university_text,get_free_counselling_university_text, get_free_counselling_university_text],
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
        df.to_csv('universitydetail.csv', index=False)
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
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        profile_click.click()
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)

        #2nd CTA

        self.driver.get(self.baseUrl)
        time.sleep(2)
        university_shortlist = self.driver.find_element(By.XPATH,"(//button[@id='btn-cta127'])[1]")
        time.sleep(2)
        university_shortlist_text = university_shortlist.text
        self.logger.info( "CTA Text : " + university_shortlist_text)
        time.sleep(2)
        university_shortlist.click()
        time.sleep(2)
        # self.name_negative()
        # time.sleep(2)
        # self.name_positive()
        # time.sleep(2)
        # self.email_negative()
        # time.sleep(2)
        # self.email_positive()
        # time.sleep(2)
        # self.stream_negative()
        # time.sleep(2)
        # self.stream_positive()
        # time.sleep(2)
        # self.level_negative()
        # time.sleep(2)
        # self.level_positive()
        # time.sleep(2)
        # self.state_negative()
        # time.sleep(2)
        # self.state_positive()
        # time.sleep(2)
        # self.mobile_negative()
        # time.sleep(2)
        # self.mobile_positive()
        # time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
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
                'CTA' : [ university_shortlist_text, university_shortlist_text, university_shortlist_text, university_shortlist_text,university_shortlist_text, university_shortlist_text],
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
        df.to_csv('universitydetail.csv', mode='a', header=False, index=False)
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
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        profile_click.click()
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)

        # save CTA

        self.driver.get(self.baseUrl)
        time.sleep(2)
        save_cta = self.driver.find_element(By.XPATH,"//span[normalize-space()='Save']")
        time.sleep(2)
        save_cta_text = save_cta.text
        self.logger.info( "CTA Text : " + save_cta_text)
        time.sleep(2)
        save_cta.click()
        time.sleep(2)
        # self.name_negative()
       # time.sleep(2)
        # self.name_positive()
        # time.sleep(2)
        # self.email_negative()
        # time.sleep(2)
        # self.email_positive()
        # time.sleep(2)
        # self.stream_negative()
        # time.sleep(2)
        # self.stream_positive()
        # time.sleep(2)
        # self.level_negative()
        # time.sleep(2)
        # self.level_positive()
        # time.sleep(2)
        # self.state_negative()
        # time.sleep(2)
        # self.state_positive()
        # time.sleep(2)
        # self.mobile_negative()
        # time.sleep(2)
        # self.mobile_positive()
        # time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
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
        df.to_csv('universitydetail.csv', mode='a', header=False, index=False)
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
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        profile_click.click()
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)

        # top courses and fees

        self.driver.get(self.baseUrl)
        time.sleep(2)
        top_courses_fees = self.driver.find_element(By.XPATH, "//h2[normalize-space()='DU Top Courses & Fees']")
        top_courses_fees.location_once_scrolled_into_view
        time.sleep(2)
        top_courses_fees_cta = self.driver.find_element(By.XPATH,"/html/body/div/div[3]/div[6]/div[1]/div/table/tbody/tr[4]/td[3]/button")
        time.sleep(2)
        top_courses_fees_cta_text = top_courses_fees_cta.text
        self.logger.info( "CTA Text : " + top_courses_fees_cta_text)
        time.sleep(2)
        top_courses_fees_cta.click()
        time.sleep(2)
        # self.name_negative()
       # time.sleep(2)
        # self.name_positive()
        # time.sleep(2)
        # self.email_negative()
        # time.sleep(2)
        # self.email_positive()
        # time.sleep(2)
        # self.stream_negative()
        # time.sleep(2)
        # self.stream_positive()
        # time.sleep(2)
        # self.level_negative()
        # time.sleep(2)
        # self.level_positive()
        # time.sleep(2)
        # self.state_negative()
        # time.sleep(2)
        # self.state_positive()
        # time.sleep(2)
        # self.mobile_negative()
        # time.sleep(2)
        # self.mobile_positive()
        # time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
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
        df.to_csv('universitydetail.csv', mode='a', header=False, index=False)
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
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        profile_click.click()
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)

        #education load cta

        self.driver.get(self.baseUrl)
        time.sleep(2)
        education_loan = self.driver.find_element(By.XPATH, "//div[normalize-space()='Worried About College Fees?']")
        education_loan.location_once_scrolled_into_view
        time.sleep(2)
        education_loan_cta = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Apply for Education Loan'])[1]")
        time.sleep(2)
        education_loan_cta_text = education_loan_cta.text
        self.logger.info( "CTA Text : " + education_loan_cta_text)
        time.sleep(2)
        education_loan_cta.click()
        time.sleep(2)
        # self.name_negative()
       # time.sleep(2)
        # self.name_positive()
        # time.sleep(2)
        # self.email_negative()
        # time.sleep(2)
        # self.email_positive()
        # time.sleep(2)
        # self.stream_negative()
        # time.sleep(2)
        # self.stream_positive()
        # time.sleep(2)
        # self.level_negative()
        # time.sleep(2)
        # self.level_positive()
        # time.sleep(2)
        # self.state_negative()
        # time.sleep(2)
        # self.state_positive()
        # time.sleep(2)
        # self.mobile_negative()
        # time.sleep(2)
        # self.mobile_positive()
        # time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
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
        df.to_csv('universitydetail.csv', mode='a', header=False, index=False)
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
        time.sleep(2)
        profile_click.click()
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)

        #take test now cta

        self.driver.get(self.baseUrl)
        time.sleep(2)
        take_test_now = self.driver.find_element(By.XPATH, "//div[normalize-space()='Are you feeling lost and unsure about what career path to take after completing 12th standard?']")
        take_test_now.location_once_scrolled_into_view
        time.sleep(2)
        take_test_now_cta = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Take the free test now'])[1]")
        time.sleep(2)
        take_test_now_cta_text = take_test_now_cta.text
        self.logger.info( "CTA Text : " + take_test_now_cta_text)
        time.sleep(2)
        take_test_now_cta.click()
        time.sleep(2)
        # self.name_negative()
       # time.sleep(2)
        # self.name_positive()
        # time.sleep(2)
        # self.email_negative()
        # time.sleep(2)
        # self.email_positive()
        # time.sleep(2)
        # self.stream_negative()
        # time.sleep(2)
        # self.stream_positive()
        # time.sleep(2)
        # self.level_negative()
        # time.sleep(2)
        # self.level_positive()
        # time.sleep(2)
        # self.state_negative()
        # time.sleep(2)
        # self.state_positive()
        # time.sleep(2)
        # self.mobile_negative()
        # time.sleep(2)
        # self.mobile_positive()
        # time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
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
        df.to_csv('universitydetail.csv', mode='a', header=False, index=False)
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
        time.sleep(2)
        profile_click.click()
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)

        # get expert help

        self.driver.get(self.baseUrl)
        time.sleep(2)
        get_expert_help = self.driver.find_element(By.XPATH, "//div[normalize-space()='Will you get admission in DU?']")
        get_expert_help.location_once_scrolled_into_view
        time.sleep(2)
        get_expert_help_cta = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Get Free Expert Help'])[1]")
        time.sleep(2)
        get_expert_help_cta_text = get_expert_help_cta.text
        self.logger.info( "CTA Text : " + get_expert_help_cta_text)
        time.sleep(2)
        get_expert_help_cta.click()
        time.sleep(2)
        # self.name_negative()
       # time.sleep(2)
        # self.name_positive()
        # time.sleep(2)
        # self.email_negative()
        # time.sleep(2)
        # self.email_positive()
        # time.sleep(2)
        # self.stream_negative()
        # time.sleep(2)
        # self.stream_positive()
        # time.sleep(2)
        # self.level_negative()
        # time.sleep(2)
        # self.level_positive()
        # time.sleep(2)
        # self.state_negative()
        # time.sleep(2)
        # self.state_positive()
        # time.sleep(2)
        # self.mobile_negative()
        # time.sleep(2)
        # self.mobile_positive()
        # time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
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
        df.to_csv('universitydetail.csv', mode='a', header=False, index=False)
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

        #footer form

        register_now = self.driver.find_element(By.XPATH,"//div[@class='commonFooterForm_footerFormContainer__yV2Nj']")
        register_now.location_once_scrolled_into_view
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,-200)","")
        time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_level = self.footerform()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_user_city, lead_city_ID, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city,lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
        sso_lead_ID, sso_name, sso_email, sso_phone_no = SSO_lead(self.logger,entered_phone_no)
        time.sleep(2)
        lms_lead_id, lms_name, lms_email, lms_phone_no, lms_source, lms_first_source, lms_city_id, lms_state_id, lms_preferred_level, lms_preferred_specialization, lms_preferred_stream, lms_preferred_state, lms_preferred_degree, lms_preferred_city, lms_institute_id = lMS_lead(self.logger,entered_phone_no)
        time.sleep(2)
        sync_name, sync_phoneNo, sync_email, sync_first_source_URL, sync_city, sync_state, sync_level, sync_stream, sync_endpoint, sync_latitude, sync_longitude, sync_source_URL = pushlog_payload(self.logger, entered_phone_no)
        time.sleep(2)
        response_message = pushlog_response(self.logger, entered_phone_no)
        time.sleep(2)

            # Create a DataFrame with the results
        data = {
                'CTA' : [ 'Footer Form', 'Footer Form', 'Footer Form', 'Footer Form','Footer Form', 'Footer Form'],
                'Platforms' : ['Entered Lead','CLD','LMS', 'SSO', 'Payload', 'Response'],
                'Lead ID' : [ None, lead_id, lms_lead_id, sso_lead_ID, None, response_message],
                'Name': [entered_name, lead_name, lms_name, sso_name, sync_name, None],
                'Email': [entered_email, lead_email, lms_email, sso_email, sync_email, None],
                'Phone No': [entered_phone_no, lead_phone_no, lms_phone_no, sso_phone_no, sync_phoneNo, None],
                'Stream': [entered_stream, lead_stream_ID, lms_preferred_stream, None, sync_stream, None],
                'User State': [None, lead_state, lms_state_id, None, sync_state, None],
                'Preferred State': [None, lead_preferred_state, lms_preferred_state, None, None, None],
                'User City': [None, lead_user_city, lms_city_id, None, sync_city, None],
                'City ID' : [None, lead_city_ID, None, None, None, None],
                'Preferred City' : [None, lead_preferred_city, lms_preferred_city, None, None, None],                
                'First Source URL': [None, lead_first_source_URL, lms_first_source, None, sync_first_source_URL, None],
                'Source_URL': [None, lead_Source_URL, lms_source, None, sync_source_URL, None],
                'Level': [entered_level, lead_preferred_level, lms_preferred_level, None, sync_level, None],
                'Specialisation': [None, lead_preferred_specialization, lms_preferred_specialization, None, None, None],
                'Degree ID': [None, lead_degree_ID, lms_preferred_degree, None, None, None],
                'Preferred Institute': [None, lead_institute_Id, lms_institute_id, None, None, None],
                'Longitude': [None, None, None, None, sync_longitude, None],
                'Latitude': [None, None, None, None, sync_latitude, None]
            }
        df = pd.DataFrame(data)
        # Save DataFrame to CSV
        df.to_csv('universitydetail.csv', mode='a', header=False, index=False)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        time.sleep(2)
        profile_click.click()
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)

        # course tab

        self.driver.get(self.baseUrl)
        time.sleep(2)
        course_tab=self.driver.find_element(By.XPATH,"//a[@title='Courses']")
        course_tab.click()
        time.sleep(2)
        get_course_list = self.driver.find_element(By.XPATH,"//button[@data-position='1']")
        time.sleep(2)
        get_course_list_text = get_course_list.text
        self.logger.info( "CTA Text : " + get_course_list_text)
        time.sleep(2)
        get_course_list.click()
        time.sleep(2)
        
        # self.name_negative()
       # time.sleep(2)
        # self.name_positive()
        # time.sleep(2)
        # self.email_negative()
        # time.sleep(2)
        # self.email_positive()
        # time.sleep(2)
        # self.stream_negative()
        # time.sleep(2)
        # self.stream_positive()
        # time.sleep(2)
        # self.level_negative()
        # time.sleep(2)
        # self.level_positive()
        # time.sleep(2)
        # self.state_negative()
        # time.sleep(2)
        # self.state_positive()
        # time.sleep(2)
        # self.mobile_negative()
        # time.sleep(2)
        # self.mobile_positive()
        # time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
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
                'CTA' : [ get_course_list_text, get_course_list_text, get_course_list_text, get_course_list_text,get_course_list_text, get_course_list_text],
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
        df.to_csv('universitydetail.csv', mode='a', header=False, index=False)
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
        course_tab=self.driver.find_element(By.XPATH,"//a[@title='Courses']")
        course_tab.click()
        time.sleep(2)
        course_tab_shortlist = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[6]/div[3]/div/h2")
        course_tab_shortlist.location_once_scrolled_into_view
        time.sleep(2)
        course_tab_shortlist_cta = self.driver.find_element(By.XPATH,"(//button[contains(text(),'Shortlist')])[2]")
        time.sleep(2)
        course_tab_shortlist_cta_text = course_tab_shortlist_cta.text
        self.logger.info( "CTA Text : " + course_tab_shortlist_cta_text)
        time.sleep(2)
        course_tab_shortlist_cta.click()
        time.sleep(2)
        # self.name_negative()
       # time.sleep(2)
        # self.name_positive()
        # time.sleep(2)
        # self.email_negative()
        # time.sleep(2)
        # self.email_positive()
        # time.sleep(2)
        # self.stream_negative()
        # time.sleep(2)
        # self.stream_positive()
        # time.sleep(2)
        # self.level_negative()
        # time.sleep(2)
        # self.level_positive()
        # time.sleep(2)
        # self.state_negative()
        # time.sleep(2)
        # self.state_positive()
        # time.sleep(2)
        # self.mobile_negative()
        # time.sleep(2)
        # self.mobile_positive()
        # time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
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
                'CTA' : [ course_tab_shortlist_cta_text, course_tab_shortlist_cta_text, course_tab_shortlist_cta_text, course_tab_shortlist_cta_text,course_tab_shortlist_cta_text, course_tab_shortlist_cta_text],
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
        df.to_csv('universitydetail.csv', mode='a', header=False, index=False)
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

        #course tab request callback

        self.driver.get(self.baseUrl)
        time.sleep(2)
        course_tab=self.driver.find_element(By.XPATH,"//a[@title='Courses']")
        course_tab.click()
        time.sleep(2)
        course_tab_shortlist = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[6]/div[3]/div/h2")
        course_tab_shortlist.location_once_scrolled_into_view
        time.sleep(2)
        course_tab_request_callback = self.driver.find_element(By.XPATH,"/html/body/div/div[3]/div[6]/div[3]/div/div/div[1]/div[2]/div[2]/button[2]")
        time.sleep(2)
        course_tab_request_callback_text = course_tab_request_callback.text
        self.logger.info( "CTA Text : " + course_tab_request_callback_text)
        time.sleep(2)
        course_tab_request_callback.click()
        time.sleep(2)
        # self.name_negative()
       # time.sleep(2)
        # self.name_positive()
        # time.sleep(2)
        # self.email_negative()
        # time.sleep(2)
        # self.email_positive()
        # time.sleep(2)
        # self.stream_negative()
        # time.sleep(2)
        # self.stream_positive()
        # time.sleep(2)
        # self.level_negative()
        # time.sleep(2)
        # self.level_positive()
        # time.sleep(2)
        # self.state_negative()
        # time.sleep(2)
        # self.state_positive()
        # time.sleep(2)
        # self.mobile_negative()
        # time.sleep(2)
        # self.mobile_positive()
        # time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
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
        df.to_csv('universitydetail.csv', mode='a', header=False, index=False)
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
        time.sleep(2)
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
        # self.name_negative()
       # time.sleep(2)
        # self.name_positive()
        # time.sleep(2)
        # self.email_negative()
        # time.sleep(2)
        # self.email_positive()
        # time.sleep(2)
        # self.stream_negative()
        # time.sleep(2)
        # self.stream_positive()
        # time.sleep(2)
        # self.level_negative()
        # time.sleep(2)
        # self.level_positive()
        # time.sleep(2)
        # self.state_negative()
        # time.sleep(2)
        # self.state_positive()
        # time.sleep(2)
        # self.mobile_negative()
        # time.sleep(2)
        # self.mobile_positive()
        # time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
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
        df.to_csv('universitydetail.csv', mode='a', header=False, index=False)
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
        get_scholarship_details = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Get Scholarship details'])[1]")
        time.sleep(2)
        get_scholarship_details_text = get_scholarship_details.text
        self.logger.info( "CTA Text : " + get_scholarship_details_text)
        time.sleep(2)
        get_scholarship_details.click()
        time.sleep(2)
        # self.name_negative()
       # time.sleep(2)
        # self.name_positive()
        # time.sleep(2)
        # self.email_negative()
        # time.sleep(2)
        # self.email_positive()
        # time.sleep(2)
        # self.stream_negative()
        # time.sleep(2)
        # self.stream_positive()
        # time.sleep(2)
        # self.level_negative()
        # time.sleep(2)
        # self.level_positive()
        # time.sleep(2)
        # self.state_negative()
        # time.sleep(2)
        # self.state_positive()
        # time.sleep(2)
        # self.mobile_negative()
        # time.sleep(2)
        # self.mobile_positive()
        # time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
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
        df.to_csv('universitydetail.csv', mode='a', header=False, index=False)
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
        time.sleep(2)
        get_placement_report = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Get Placement report'])[1]")
        time.sleep(2)
        get_placement_report_text = get_placement_report.text
        self.logger.info( "CTA Text : " + get_placement_report_text)
        time.sleep(2)
        get_placement_report.click()
        time.sleep(2)
        # self.name_negative()
       # time.sleep(2)
        # self.name_positive()
        # time.sleep(2)
        # self.email_negative()
        # time.sleep(2)
        # self.email_positive()
        # time.sleep(2)
        # self.stream_negative()
        # time.sleep(2)
        # self.stream_positive()
        # time.sleep(2)
        # self.level_negative()
        # time.sleep(2)
        # self.level_positive()
        # time.sleep(2)
        # self.state_negative()
        # time.sleep(2)
        # self.state_positive()
        # time.sleep(2)
        # self.mobile_negative()
        # time.sleep(2)
        # self.mobile_positive()
        # time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
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
        df.to_csv('universitydetail.csv', mode='a', header=False, index=False)
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
        get_cutoff_details = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Download Cut Offs'])[1]")
        time.sleep(2)
        get_cutoff_details_text = get_cutoff_details.text
        self.logger.info( "CTA Text : " + get_cutoff_details_text)
        time.sleep(2)
        get_cutoff_details.click()
        time.sleep(2)
        # self.name_negative()
       # time.sleep(2)
        # self.name_positive()
        # time.sleep(2)
        # self.email_negative()
        # time.sleep(2)
        # self.email_positive()
        # time.sleep(2)
        # self.stream_negative()
        # time.sleep(2)
        # self.stream_positive()
        # time.sleep(2)
        # self.level_negative()
        # time.sleep(2)
        # self.level_positive()
        # time.sleep(2)
        # self.state_negative()
        # time.sleep(2)
        # self.state_positive()
        # time.sleep(2)
        # self.mobile_negative()
        # time.sleep(2)
        # self.mobile_positive()
        # time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
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
        df.to_csv('universitydetail.csv', mode='a', header=False, index=False)
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
        profile_click = self.driver.find_element(By.XPATH,"//img[@alt='profile image']")
        time.sleep(2)
        profile_click.click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(2)
        logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
        logout_click.click()
        time.sleep(5)

        # affiliated colleges download brochure

        self.driver.get(self.baseUrl)
        time.sleep(2)
        affliated_colleges_tab=self.driver.find_element(By.XPATH,"//a[@title='Affiliated Colleges']")
        affliated_colleges_tab.click()
        time.sleep(2)
        affliated_colleges_section = self.driver.find_element(By.XPATH, "//h2[normalize-space()='Delhi University Affiliated Colleges']")
        affliated_colleges_section.location_once_scrolled_into_view
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        download_brochure_affiliated_tab = self.driver.find_element(By.XPATH,"(//button[@id='btn-cta126'])[2]")
        time.sleep(2)
        download_brochure_affiliated_tab_text = download_brochure_affiliated_tab.text
        self.logger.info( "CTA Text : " + download_brochure_affiliated_tab_text)
        time.sleep(2)
        download_brochure_affiliated_tab.click()
        time.sleep(2)
        # self.name_negative()
       # time.sleep(2)
        # self.name_positive()
        # time.sleep(2)
        # self.email_negative()
        # time.sleep(2)
        # self.email_positive()
        # time.sleep(2)
        # self.stream_negative()
        # time.sleep(2)
        # self.stream_positive()
        # time.sleep(2)
        # self.level_negative()
        # time.sleep(2)
        # self.level_positive()
        # time.sleep(2)
        # self.state_negative()
        # time.sleep(2)
        # self.state_positive()
        # time.sleep(2)
        # self.mobile_negative()
        # time.sleep(2)
        # self.mobile_positive()
        # time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
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
                'CTA' : [ download_brochure_affiliated_tab_text, download_brochure_affiliated_tab_text, download_brochure_affiliated_tab_text, download_brochure_affiliated_tab_text,download_brochure_affiliated_tab_text, download_brochure_affiliated_tab_text],
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
        df.to_csv('universitydetail.csv', mode='a', header=False, index=False)
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

        # affiliated colleges shortlist

        self.driver.get(self.baseUrl)
        time.sleep(2)
        affliated_colleges_tab=self.driver.find_element(By.XPATH,"//a[@title='Affiliated Colleges']")
        affliated_colleges_tab.click()
        time.sleep(2)
        affliated_colleges = self.driver.find_element(By.XPATH, "//div[@class='box block affiliatedColleges_affilatedCollegesWrap__2psgo']")
        affliated_colleges.location_once_scrolled_into_view
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        apply_now_affiliated_tab = self.driver.find_element(By.XPATH,"(//button[@id='btn-cta127'])[2]")
        time.sleep(2)
        apply_now_affiliated_tab_text = apply_now_affiliated_tab.text
        self.logger.info( "CTA Text : " + apply_now_affiliated_tab_text)
        time.sleep(2)
        apply_now_affiliated_tab.click()
        time.sleep(2)
        # self.name_negative()
       # time.sleep(2)
        # self.name_positive()
        # time.sleep(2)
        # self.email_negative()
        # time.sleep(2)
        # self.email_positive()
        # time.sleep(2)
        # self.stream_negative()
        # time.sleep(2)
        # self.stream_positive()
        # time.sleep(2)
        # self.level_negative()
        # time.sleep(2)
        # self.level_positive()
        # time.sleep(2)
        # self.state_negative()
        # time.sleep(2)
        # self.state_positive()
        # time.sleep(2)
        # self.mobile_negative()
        # time.sleep(2)
        # self.mobile_positive()
        # time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
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
                'CTA' : [ apply_now_affiliated_tab_text, apply_now_affiliated_tab_text, apply_now_affiliated_tab_text, apply_now_affiliated_tab_text,apply_now_affiliated_tab_text, apply_now_affiliated_tab_text],
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
        df.to_csv('universitydetail.csv', mode='a', header=False, index=False)
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

        # affiliated colleges get counselling

        self.driver.get(self.baseUrl)
        time.sleep(2)
        affliated_colleges_tab=self.driver.find_element(By.XPATH,"//a[@title='Affiliated Colleges']")
        affliated_colleges_tab.click()
        time.sleep(2)
        affliated_colleges = self.driver.find_element(By.XPATH, "//div[@class='box block affiliatedColleges_affilatedCollegesWrap__2psgo']")
        affliated_colleges.location_once_scrolled_into_view
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        get_counselling_affiliated_tab = self.driver.find_element(By.XPATH,"(//button[@id='btn-cta126'])[3]")
        time.sleep(2)
        get_counselling_affiliated_tab_text = get_counselling_affiliated_tab.text
        self.logger.info( "CTA Text : " + get_counselling_affiliated_tab_text)
        time.sleep(2)
        get_counselling_affiliated_tab.click()
        time.sleep(2)
        # self.name_negative()
       # time.sleep(2)
        # self.name_positive()
        # time.sleep(2)
        # self.email_negative()
        # time.sleep(2)
        # self.email_positive()
        # time.sleep(2)
        # self.stream_negative()
        # time.sleep(2)
        # self.stream_positive()
        # time.sleep(2)
        # self.level_negative()
        # time.sleep(2)
        # self.level_positive()
        # time.sleep(2)
        # self.state_negative()
        # time.sleep(2)
        # self.state_positive()
        # time.sleep(2)
        # self.mobile_negative()
        # time.sleep(2)
        # self.mobile_positive()
        # time.sleep(2)
        entered_name, entered_email, entered_phone_no, entered_stream, entered_state, entered_city = self.happyflow()
        time.sleep(2)
        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,entered_phone_no)
        time.sleep(2)
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
                'CTA' : [ get_counselling_affiliated_tab_text, get_counselling_affiliated_tab_text, get_counselling_affiliated_tab_text, get_counselling_affiliated_tab_text,get_counselling_affiliated_tab_text, get_counselling_affiliated_tab_text],
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
        df.to_csv('universitydetail.csv', mode='a', header=False, index=False)
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
