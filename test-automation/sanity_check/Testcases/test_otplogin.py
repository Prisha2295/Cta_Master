import time
import requests
import mysql.connector
import unittest
from selenium.webdriver.common.by import By
from configparser import ConfigParser
from selenium.webdriver.support.ui import Select
from common_functions import *
from utilities.Readproperties import ReadConfig
from utilities.customlogger import Logs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import os
from dotenv import load_dotenv

load_dotenv()

cld_host_live = os.getenv("cld_host_live")
cld_username_live = os.getenv("cld_username_live")
cld_pass_live = os.getenv("cld_pass_live")
cld_databasename_live = os.getenv("cld_databasename_live")

cld_host_staging = os.getenv("cld_host_staging")
cld_username_staging = os.getenv("cld_username_staging")
cld_pass_staging = os.getenv("cld_pass_staging")
cld_databasename_staging = os.getenv("cld_databasename_staging")


class Test_checkloginotp(commonfunctions):

    baseUrl = ReadConfig.HomepageURL()
    baseUrl6 = ReadConfig.ExamdetailURL()

    def test_loginotp(self,setup):
        self.logger = Logs.loggen('Test Login-otp')  # logger of current test case
        self.logger.info("******* Starting LOGIN OTP TEST**********")
        self.driver = setup


        self.driver.get(self.baseUrl6)
        self.logger.info("-------------------------")

        time.sleep(2)
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

        # Create an ActionChains object
        actions = ActionChains(self.driver)

        # Hover over the profile icon
        actions.move_to_element(profile_icon).perform()

        # Wait for the login button to become clickable
        wait = WebDriverWait(self.driver, 5)
        try:
            login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".CollegedekhoNavBar_btn__v2gmZ")))
        except:
            login_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='buttonCol']//button[@id='login']")))

        login_link.click()
        time.sleep(3)

        try:
            otp_phnno = self.driver.find_element(By.CSS_SELECTOR, "input[name='phone_no']")
        except:
            otp_phnno = self.driver.find_element(By.XPATH, "//input[@id='phone_no']")

            otp_phnno.click()
        time.sleep(2)

        def test_phonetestcasehappycase_3(self):
            parser = ConfigParser()
            parser.read('Login.ini')

            phone_number = self.driver.find_element(By.CSS_SELECTOR, "input[name='phone_no']")


            phone_number.clear()
            time.sleep(2)
            phone_number.send_keys(parser.get('otplogin', 'Number_range_5'))
            time.sleep(2)
            self.logger.info(parser.get('otplogin', 'Number_range_5'))

            generate_otpbutton = self.driver.find_element(By.ID,"gtm_loginGenerateOtp")
            generate_otpbutton.click()
            time.sleep(5)

            conn = mysql.connector.connect(host=cld_host_live, database=cld_databasename_live, user=cld_username_live, password=cld_pass_live)
            self.logger.info(conn)
            time.sleep(2)
            # query = ("""select code from users_otp where phone_no = {} order by id desc""").format(random_number)
            # cursor = conn.cursor()
            # cursor.execute(query)
            # row = cursor.fetchone()
            # if row is None:
            #     self.logger.info("No OTP found for phone number {}".format(random_number))
            #     return  # or raise an exception, depending on your use case
            # result_dict = list(row)
            # self.logger.info(result_dict)
            
            # for index, value in enumerate(result_dict):
            #     otp_1_new = self.driver.find_element(By.ID,
            #                                             "digit1".format(int(index) + 1))
            #     otp_1_new.send_keys(value)
            #     time.sleep(7)

            # click_verify_button = self.driver.find_element(By.ID,"id_otp_verify")
            # time.sleep(1)
            # click_verify_button.click()
            # time.sleep(2)


            # conn = mysql.connector.connect(host='95.217.156.247',database = 'collegedekho',user = 'cld_ro', password = 'w4snE59A$dr@k48q')
            # self.logger.info(conn)

            otp_query_1 = ("""select * from users_otp where phone_no = {} order by id desc""".format(parser.get('otplogin', 'Number_range_5')))
            cursor = conn.cursor()
            cursor.execute(otp_query_1)
            row = cursor.fetchone()
            result_dict = list(row)
            self.logger.info('OTP: ' + str(result_dict[2]))
            try:
                otp_texts = self.driver.find_element(By.XPATH, "//div[@class='CollegedekhoNavBar_rightCol__7zEnR CollegedekhoNavBar_column__fhVRv']//p[1]")
            except:
                otp_texts = self.driver.find_element(By.CSS_SELECTOR, "div[id='otpVerification2'] p")
            self.logger.info(otp_texts.text)
            otp_value = [int(x) for x in str(result_dict[2])]
            try:
                for index, value in enumerate(otp_value):
                    try:
                        otp_1 = self.driver.find_element(By.XPATH, "//li[@class='CollegedekhoNavBar_otpFields__Xb_KM']//input[{}]".format(int(index) + 1))
                    except:
                        otp_1 = self.driver.find_element(By.XPATH, "//li[@class='otp_fields otp_fields_register']//input[{}]".format(int(index) + 1))
                    otp_1.send_keys(value)
                    time.sleep(5)
            except Exception as e:
                self.logger.info(e)
                for index, value in enumerate(result_dict):
                    try:
                        otp_1_new = self.driver.find_element(By.XPATH, "//input[@name='first'])[{}]".format(int(index) + 1))
                    except:
                        otp_1_new = self.driver.find_element(By.XPATH, "//input[@name='otp1'])[{}]".format(int(index) + 1))
                    otp_1_new.send_keys(value)
                    time.sleep(5)

            verify_button = self.driver.find_element(By.CSS_SELECTOR, "#gtm_loginVerify")
            verify_button.click()
            time.sleep(3)
            self.logger.info("Current_Url : " + current_url)
            self.logger.info('OTP Verified,user loggedin')
            time.sleep(2)

        test_phonetestcasehappycase_3(self)
