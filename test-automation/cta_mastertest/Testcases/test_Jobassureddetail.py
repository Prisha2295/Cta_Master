import time
import requests
from selenium.webdriver.common.by import By
from common_functions import commonfunctions
from utilities.Readproperties import ReadConfig
from utilities.customlogger import Logs
from common_functions import *

import os
from dotenv import load_dotenv

load_dotenv()

cld_host_live = os.getenv("cld_host_live")
cld_username_live = os.getenv("cld_username_live")
cld_pass_live = os.getenv("cld_pass_live")
cld_databasename_live = os.getenv("cld_databasename_live")

cld_host_staging = os.getenv("cld_host_live")
cld_username_staging = os.getenv("cld_username_staging")
cld_pass_staging = os.getenv("cld_pass_staging")
cld_databasename_staging = os.getenv("cld_databasename_staging")

class Test_Jobassureddetail(commonfunctions):
    
    baseUrl = ReadConfig.JobassureddetailURL()

    def test_Jobassureddetailcta(self, setup):
        self.logger = Logs.loggen('Test Jobassureddetail')  # logger of current test case
        self.logger.info("******* Starting CTA TEST JOBASSUREDDETAIL**********")
        
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
        enrol_now = self.driver.find_element(By.XPATH,"(//span[contains(text(),'Enroll Now')])[1]")
        time.sleep(2)
        enrol_now.click()
        time.sleep(2)
        enrolnow_signup = self.driver.find_element(By.XPATH,"(//button[normalize-space()='SignUp'])[1]")
        time.sleep(2)
        enrolnow_signup.click()
        time.sleep(2)
        random_name = random_namee()
        random_emaill = random_email()
        random_no = random_phonenumber()
        time.sleep(2)
        Name = self.driver.find_element(By.XPATH,"//input[@id='id_signup_name']")
        Name.send_keys(random_name)
        self.logger.info(random_name)
        time.sleep(3)
        Email = self.driver.find_element(By.XPATH,"//input[@id='id_signup_email']")
        Email.send_keys(random_emaill)
        self.logger.info(random_emaill)
        time.sleep(3)
        Phone_no = self.driver.find_element(By.XPATH,"//input[@id='id_signup_phone']")
        Phone_no.send_keys(random_no)
        self.logger.info(random_no)
        time.sleep(3)
        Submit_Button = self.driver.find_element(By.XPATH,"//button[@id='id_signup']")
        Submit_Button.click()
        Submit_Text= Submit_Button.text
        self.logger.info( "CTA Text : " + Submit_Text)
        time.sleep(3)

        #OTP Connection

        conn = mysql.connector.connect(host=cld_host_live, database=cld_databasename_live, user=cld_username_live, password=cld_pass_live)
        # conn = mysql.connector.connect(host='cld_host_staging,database = cld_databasename_staging,user = cld_username_staging, password = cld_pass_staging)


        self.logger.info(conn)
        time.sleep(2)
        query = ("""select code,phone_no from users_otp where phone_no = {} order by id desc""").format(randomnumber)
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            self.logger.info("No OTP found for phone number {}".format(random_no))
            return  # or raise an exception, depending on your use case
        result_dict = list(row)
        self.logger.info(result_dict)

        # OTP Functionality

        for index, value in enumerate(result_dict):
            otp_1_new = self.driver.find_element(By.XPATH,
                                                    "//input[@id='digit1']".format(int(index) + 1))
            otp_1_new.send_keys(value)
            time.sleep(7)

        self.logger.info("Otp added successfully")
        time.sleep(4)

        # Clicking on verify button
        
        verify_button = self.driver.find_element(By.XPATH, "//button[@id='id_otp_verify']")
        verify_button.click()
        time.sleep(5)
        