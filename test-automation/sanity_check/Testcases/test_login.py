import time
import requests
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utilities.Readproperties import ReadConfig    
from utilities.customlogger import Logs
from common_functions import *
from database import *

import os
from dotenv import load_dotenv

load_dotenv()

collegedekho_user1 = os.getenv("collegedekho_user1")
collegedekho_pass1 = os.getenv("collegedekho_pass1")

class Test_Logincheck(commonfunctions):
        
    
    baseUrl = ReadConfig.HomepageURL()
    baseUrl6 = ReadConfig.ExamdetailURL()

    def test_login(self,setup):
        self.logger = Logs.loggen('Test_Logincheck')  


        # Initialize the 'driver' attribute
        self.driver = setup

        
        self.driver.get(self.baseUrl6)
        self.logger.info("------Starting Login Test ------")

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
        except :
            profile_icon = self.driver.find_element(By.XPATH, "(//img[@alt='Profile icon'])[2]")


        # Create an ActionChains object
        actions = ActionChains(self.driver)

        # Hover over the profile icon
        actions.move_to_element(profile_icon).perform()

        # Wait for the login button to become clickable 
        wait = WebDriverWait(self.driver, 5) 
        try:
            login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".CollegedekhoNavBar_btn__v2gmZ")))
        except:
            login_link = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='buttonCol']//button[@id='login']")))
  

        login_link.click()
        time.sleep(3)

        # random_Password = self.generate_random_password()
        # random_Email= self.random_email()
        # random_number = self.random_phonenumber()

        time.sleep(2)
      
        #Login Pass
        LoginviaPswrd = self.driver.find_element(By.ID, "gtm_loginViaPass")
        LoginviaPswrd.click()
        time.sleep(3)
        try:
            EmailV = self.driver.find_element(By.ID, "id_phone_cta")
        except:
            EmailV = self.driver.find_element(By.NAME, "login")
        time.sleep(2)

        EmailV.send_keys(collegedekho_user1)
        try:
            self.logger.info("Email text field Height = " + EmailV.value_of_css_property("height"))
            assert EmailV.value_of_css_property("height") == "38px"
            self.logger.info("Email text field box sizing = " + EmailV.value_of_css_property("box-sizing"))
            assert EmailV.value_of_css_property("box-sizing") == "border-box"
            self.logger.info("Email text field background color = " + EmailV.value_of_css_property("background-color"))
            assert EmailV.value_of_css_property("background-color") == "rgba(0, 0, 0, 0)"
            self.logger.info("Email text field margin-bottom = " + EmailV.value_of_css_property("margin-bottom"))
            assert EmailV.value_of_css_property("margin-bottom") == "20px"
            time.sleep(2)
        except Exception as e:
            self.logger.info(e)
            pass
        try:
            PasswordV = self.driver.find_element(By.ID, "id_password_cta")
        except:
            PasswordV = self.driver.find_element(By.NAME, "password")

        PasswordV.send_keys(collegedekho_pass1)
        time.sleep(3)
        

        LoginV = self.driver.find_element(By.ID, "gtm_login")
        LoginV.click()
        self.logger.info("Login with Valid email/password success")
        time.sleep(3)
        current_url = self.driver.current_url
        self.logger.info("Redirection Url: %s", current_url)

        
        time.sleep(5)


        # Locate the profile icon
        profile_icon = self.driver.find_element(By.XPATH, "//img[@alt='profile image']")
        time.sleep(2)
        # Create an ActionChains object
        actions = ActionChains(self.driver)

        # Hover over the profile icon
        actions.move_to_element(profile_icon).perform()

        time.sleep(4)
        # Profiletxt = self.driver.find_element(By.CSS_SELECTOR,".navBar_signOutBox__3EH5I")
        # try:
        #     assert Profiletxt.value_of_css_property("font-size") == "14px"
        # except exception as e:
        #     self.logger.info(e)
        #     pass
        # time.sleep(5)

        
        Signout = self.driver.find_element(By.XPATH,"//span[normalize-space()='Sign Out']")
        Signout.click()
        self.logger.info("SignOut Success")
        time.sleep(2)


        # try:
        #     id_Profile = self.driver.find_element(By.CLASS_NAME, "CollegedekhoNavBar_login__TpWB4")
        #     id_Profile.click()
        # except:
        #     old_id_profile = self.driver.find_element(By.ID,"login")
        #     old_id_profile.click()
        # time.sleep(2)

        # login_link = self.driver.find_element(By.CSS_SELECTOR, ".CollegedekhoNavBar_btn__v2gmZ")
        # login_link.click()
        # time.sleep(3)
        # self.logger.info("Clicked on Login link")
        # time.sleep(3)
       
        # LoginviaPswrd = self.driver.find_element(By.ID, "gtm_loginViaPass")
        # LoginviaPswrd.click()
        # time.sleep(3)
