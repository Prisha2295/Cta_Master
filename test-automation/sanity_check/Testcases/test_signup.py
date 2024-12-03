import time
import requests
import unittest
from database import *
from selenium.webdriver.common.action_chains import ActionChains
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from common_functions import *
from utilities.Readproperties import ReadConfig
from utilities.customlogger import Logs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

# Load environment variables
cld_host_live = os.getenv("cld_host_live")
cld_username_live = os.getenv("cld_username_live")
cld_pass_live = os.getenv("cld_pass_live")
cld_databasename_live = os.getenv("cld_databasename_live")

cld_host_staging = os.getenv("cld_host_staging")
cld_username_staging = os.getenv("cld_username_staging")
cld_pass_staging = os.getenv("cld_pass_staging")
cld_databasename_staging = os.getenv("cld_databasename_staging")


class Test_Signupcheck(commonfunctions):

    baseUrl = ReadConfig.HomepageURL()
    baseUrl6 = ReadConfig.ExamdetailURL()

    def test_signup(self, setup):
        self.logger = Logs.loggen('Test Signup')  # logger of current test case
        self.logger.info("******* Starting SIGNUP TEST**********")
        self.driver = setup

        self.driver.get(self.baseUrl6)
        self.logger.info("-------------------------")

        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        response = requests.get(current_url)
        assert response.status_code == 200
        self.logger.info("Response : " + str(response.status_code))

        time.sleep(6)

        try:
            # Wait for the close button element to be clickable
            popup_close = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='formContent']//button[@class='close'][normalize-space()='×']")))
            
            # Click the close button to close the popup
            popup_close.click()

            # Optionally, you can wait for some additional time after clicking (if necessary)
            time.sleep(2)

        except TimeoutException:
            # Handle the case when the element is not found within the specified timeout
            self.logger.info("Popup close button not found within timeout. Skipping.")


        
        try:
            profile_icon = self.driver.find_element(By.XPATH, "//img[@alt='profile image']")
        except:
            profile_icon = self.driver.find_element(By.XPATH, "(//img[@alt='Profile icon'])[2]")

        # Hover over the profile icon
        actions = ActionChains(self.driver)
        actions.move_to_element(profile_icon).perform()
        time.sleep(2)

        try:
            CreateAccbtn = self.driver.find_element(By.CSS_SELECTOR, ".CollegedekhoNavBar_createAccBtn__vRQ2u.secondaryBtn")
        except:
            CreateAccbtn = self.driver.find_element(By.CSS_SELECTOR, "button[onclick='get_login_modal(this)']")
        CreateAccbtn.click()
        time.sleep(2)

        random_name = random_namee()
        random_emaill = random_email()
        random_no = random_phonenumber()
        time.sleep(2)
        # Random name function in signup form

        self.logger.info("Name:" + random_name)
        name = self.driver.find_element(By.ID, "id_name_signup")
        name.send_keys(random_name)
        time.sleep(2)

        # Random email function in signup form
        self.logger.info("Email:" + random_emaill)  # Corrected from random_email to emaill
        email = self.driver.find_element(By.ID, "id_email_signup")
        email.send_keys(random_emaill)
        time.sleep(2)

        # Random phone number function in signup form

        self.logger.info("Phone Number:" + random_no)
        mobile = self.driver.find_element(By.ID, "id_phone_signup")
        mobile.send_keys(random_no)
        time.sleep(2)

        # Selecting preferred stream from dropdown
        pref_stream = Select(self.driver.find_element(By.ID, "id_preferred_stream_signup"))
        pref_stream.select_by_index(2)
        self.logger.info("Preferred Stream: " + pref_stream.first_selected_option.text)

        # Selecting preferred level from dropdown
        try:
            pref_level = Select(self.driver.find_element(By.XPATH, "//select[@id='id_preferred_level_signup']"))
            pref_level.select_by_index(3)
            self.logger.info("Preferred Level: " + pref_level.first_selected_option.text)
        except NoSuchElementException:
            self.logger.info("Element not found")

        # Generating random password in signup form
        self.logger.info("pass:" + random_password)
        password2 = self.driver.find_element(By.ID, "password_signup")
        password2.send_keys(random_password)
        time.sleep(3)

        # Clicking on signup button
        submit = self.driver.find_element(By.ID, "gtm_signup")
        submit.click()
        self.logger.info('Lead from signup submitted')
        time.sleep(3)     

        lead_id, lead_email, lead_name, lead_phone_no, lead_state, lead_city_ID, lead_user_city, lead_first_source_URL, lead_Source_URL, lead_institute_Id, lead_preferred_stream, lead_preferred_specialization, lead_stream_ID, lead_preferred_state, lead_preferred_city, lead_preferred_level, lead_degree_ID = cld_lead(self.logger,random_no)
        time.sleep(2)
        sso_lead_ID, sso_name, sso_email, sso_phone_no = SSO_lead(self.logger,random_no)
        time.sleep(480)
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
        df.to_csv('Signup_check.csv', index=False)
        


        # Log the redirection URL
        redirection_url = self.driver.current_url
        self.logger.info("Signup Redirection URL: %s", redirection_url)

        self.driver.refresh()
        time.sleep(3)

        # Locate the profile icon
        try:
            profile_icon = self.driver.find_element(By.XPATH, "//img[@alt='profile image']")
        except:
            profile_icon = self.driver.find_element(By.CSS_SELECTOR, "(//img[@alt='Profile icon'])[2]")
        
        # Hover over the profile icon
        actions = ActionChains(self.driver)
        actions.move_to_element(profile_icon).perform()
        time.sleep(2)

        # Profiletxt = self.driver.find_element(By.CSS_SELECTOR, ".navBar_signOutBox__3EH5I")
        # try:
        #     assert Profiletxt.value_of_css_property("font-size") == "14px"
        # except Exception as e:
        #     self.logger.info(e)
        #     pass
        # time.sleep(3)

        try:
            signout=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
            signout.click()
            time.sleep(5)
        except:
            signout=self.driver.find_element(By.XPATH, "//a[@class='signout-btn']")
            signout.click()
            time.sleep(5)

        self.logger.info("SignOut Success")
        time.sleep(3)

# if __name__ == '__main__':
#     unittest.main()
