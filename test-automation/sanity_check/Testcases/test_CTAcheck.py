import time
import requests
from selenium.webdriver.common.by import By
from common_functions import commonfunctions
from utilities.Readproperties import ReadConfig    
from utilities.customlogger import Logs
from common_functions import *
from database import *
import queue

class Test_CTAcheck(commonfunctions):
        
    
    baseUrl = ReadConfig.HomepageURL()
    baseUrl1 = ReadConfig.NewslistingURL()
    baseUrl2 = ReadConfig.CourseURL()
    baseUrl3 = ReadConfig.CollegedetailURL()
    baseUrl4 = ReadConfig.ExamdetailURL()


    def test_ctacheck(self, setup):
        self.logger = Logs.loggen('Test_CTAcheck')  
        
        # Initialize the 'driver' attribute
        self.driver = setup
        
        self.driver.get(self.baseUrl)
        self.logger.info("-------------------------")

        scroll_element = self.driver.find_element(By.XPATH,"//span[normalize-space()='Personalised Guidance.']")
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
        time.sleep(5)
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
        df.to_csv('CTA_check.csv', index=False)
        
        self.driver.get(self.baseUrl1)

        #subscribe now news listing

        news_listing_subscribe_now = self.driver.find_element(By.XPATH, "//div[@class='news-letter-head']")
        news_listing_subscribe_now.location_once_scrolled_into_view
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,-200)","")
        time.sleep(2)
        news_listing_subscribe_now_cta = self.driver.find_element(By.XPATH,"//span[@id='btn-cta-21']")
        time.sleep(2)
        news_listing_subscribe_now_cta_text = news_listing_subscribe_now_cta.text
        self.logger.info( "CTA Text : " + news_listing_subscribe_now_cta_text)
        time.sleep(2)
        news_listing_subscribe_now_cta.click()
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
                'CTA' : [ news_listing_subscribe_now_cta_text , news_listing_subscribe_now_cta_text , news_listing_subscribe_now_cta_text, news_listing_subscribe_now_cta_text, news_listing_subscribe_now_cta_text, news_listing_subscribe_now_cta_text],
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
        df.to_csv('CTA_check.csv', mode='a', header=False, index=False)
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
        try:
            logout_click=self.driver.find_element(By.XPATH, "//a[normalize-space()='Sign out']")
            logout_click.click()
            time.sleep(5)
        except:
            logout_click=self.driver.find_element(By.XPATH, "(//a[@class='signout-btn'])[1]")
            logout_click.click()
            time.sleep(5)

        #Check Eligibility CTA

        self.driver.get(self.baseUrl2)
        time.sleep(2)
        check_eligibility = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Check Eligibility'])[1]")
        time.sleep(2)
        check_eligibility_cta_text = check_eligibility.text
        self.logger.info( "CTA Text : " + check_eligibility_cta_text)
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
                'CTA' : [ check_eligibility_cta_text, check_eligibility_cta_text, check_eligibility_cta_text, check_eligibility_cta_text,check_eligibility_cta_text, check_eligibility_cta_text],
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
        df.to_csv('CTA_check.csv', mode='a', header=False, index=False)

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


        #Check Eligibility CTA

        self.driver.get(self.baseUrl3)
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
        df.to_csv('CTA_check.csv', mode='a', header=False, index=False)

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

        #exam detail

        self.driver.get(self.baseUrl4)
        time.sleep(2)
        set_exam_alert = self.driver.find_element(By.XPATH,"//button[@id='btn-cta-7']")
        time.sleep(2)
        set_exam_alert_text = set_exam_alert.text
        self.logger.info( "CTA Text : " + set_exam_alert_text)
        time.sleep(2)
        set_exam_alert.click()
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
                'CTA' : [ set_exam_alert_text, set_exam_alert_text, set_exam_alert_text, set_exam_alert_text,set_exam_alert_text, set_exam_alert_text],
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
        df.to_csv('CTA_check.csv', mode='a', header=False, index=False)

        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        profile_click = self.driver.find_element(By.XPATH,"(//img[@alt='Profile icon'])[2]")
        profile_click.click()
        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(2)
        logout_click=self.driver.find_element(By.XPATH, "//a[@class='signout-btn']")
        logout_click.click()
        time.sleep(5)

        # news detail
        news_url, URIID = news_url_connect(self.logger)
        self.logger.info(news_url)
        self.driver.get(f"https://www.collegedekho.com/news/{news_url}-{URIID}/")
        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        first_cta_top = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div[1]/div[1]/div[1]/div[3]/div[2]/button[1]")
        time.sleep(2)
        first_cta_top_text = first_cta_top.text
        self.logger.info( "CTA Text : " + first_cta_top_text)
        time.sleep(2)
        first_cta_top.click()
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
                    'CTA' : [ first_cta_top_text, first_cta_top_text, first_cta_top_text, first_cta_top_text,first_cta_top_text, first_cta_top_text],
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
        df.to_csv('CTA_check.csv', mode='a', header=False, index=False)

        new_url = self.driver.current_url
        self.logger.info("New URL : " + new_url)
        if new_url == current_url:
            time.sleep(2)
            self.driver.refresh()
        else:
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
            self.driver.refresh()
            time.sleep(2)
