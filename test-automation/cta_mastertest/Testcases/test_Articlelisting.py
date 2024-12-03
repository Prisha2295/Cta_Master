import time
import requests
from selenium.webdriver.common.by import By
from common_functions import commonfunctions
from utilities.Readproperties import ReadConfig
from utilities.customlogger import Logs
from database import *
import pandas as p

class Test_Articlelisting(commonfunctions):
        
    
    baseUrl = ReadConfig.ArticlelistingURL()

    def test_articlelistingcta(self, setup):
        self.logger = Logs.loggen('Test Articlelisting')  # logger of current test case
        self.logger.info("******* Starting CTA TEST ARTICLELISTING**********")
        
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

        #subscribe now college listing

        article_listing_subscribe_now = self.driver.find_element(By.XPATH, "//div[@class='news-letter-head']")
        article_listing_subscribe_now.location_once_scrolled_into_view
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,-200)","")
        time.sleep(2)
        article_listing_subscribe_now_cta = self.driver.find_element(By.XPATH,"//span[@id='btn-cta-21']")
        time.sleep(2)
        article_listing_subscribe_now_cta_text = article_listing_subscribe_now_cta.text
        self.logger.info( "CTA Text : " + article_listing_subscribe_now_cta_text)
        time.sleep(2)
        article_listing_subscribe_now_cta.click()
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
                'CTA' : [ article_listing_subscribe_now_cta_text , article_listing_subscribe_now_cta_text , article_listing_subscribe_now_cta_text, article_listing_subscribe_now_cta_text, article_listing_subscribe_now_cta_text, article_listing_subscribe_now_cta_text],
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
        df.to_csv('articlelisting.csv', index=False)


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
        profile_click = self.driver.find_element(By.XPATH,"(//img[@alt='Profile icon'])[2]")
        time.sleep(2)
        profile_click.click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(2)
        logout_click=self.driver.find_element(By.XPATH, "//a[@class='signout-btn']")
        logout_click.click()
        time.sleep(5)
