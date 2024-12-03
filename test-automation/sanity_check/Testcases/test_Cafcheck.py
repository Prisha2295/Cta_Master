import time
import requests
import mysql.connector
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from common_functions import commonfunctions
from common_functions import random_phonenumber,random_namee,random_email
from utilities.Readproperties import ReadConfig
from utilities.customlogger import Logs
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

class Test_Caf(commonfunctions):
        
    
    baseUrl = ReadConfig.CafURL()

    def test_caf(self, setup):
        self.logger = Logs.loggen('Test CAF')  # logger of current test case
        self.logger.info("******* Starting CAF Page TEST**********")
        
        # Initialize the 'driver' attribute
        self.driver = setup
        
        self.driver.get(self.baseUrl)
        self.logger.info("-------------------------")
        actual_title = self.driver.title
        self.logger.info(actual_title)
        #assert actual_title == "Common Application Form - Online College Admission Form | Collegedekho"
        time.sleep(2)
        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        response = requests.get(current_url)
        #assert current_url == self.baseUrl
        #assert response.status_code == 200
        self.logger.info("Response : " + str(response.status_code))

        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(2)
        college_name = self.driver.find_element(By.XPATH,"/html[1]/body[1]/section[3]/div[1]/ul[1]/li[1]/div[1]/div[3]/a[1]").text
        time.sleep(1)
        self.logger.info(college_name)
        caf_amount = self.driver.find_element(By.XPATH,"//li[1]//div[1]//div[1]//div[2]//p[1]").text
        time.sleep(1)
        self.logger.info(caf_amount)
        time.sleep(1)
        Apply_now = self.driver.find_element(By.XPATH,"(//a[@class='apply-now exit-popup-message'])[1]")
        time.sleep(1)
        Apply_now.click()
        time.sleep(2)
        Caf_course_page = self.driver.current_url
        input_string = college_name
        output_string = input_string.replace(' ', '-').replace(',', '').lower()
        #assert Caf_course_page == "https://www.collegedekho.com" + "/caf/"+ output_string + "/courses"
        time.sleep(1)
        self.logger.info("Caf_course_page : " + Caf_course_page)
        time.sleep(2)
        add_course = self.driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[1]/div[3]/div[3]/ul/li[1]/button[1]")
        time.sleep(1)
        add_course.click()
        time.sleep(2)
        sumit_button = self.driver.find_element(By.XPATH,"(//button[@type='submit'])[1]")
        time.sleep(1)
        sumit_button.click()
        time.sleep(1)
        sign_form = self.driver.find_element(By.ID,"id_show_signup")
        time.sleep(1)
        sign_form.click()
        time.sleep(1)
        sign_name = self.driver.find_element(By.ID,"id_signup_name")
        time.sleep(1)
        sign_name.send_keys(random_namee())
        time.sleep(1)
        sign_email = self.driver.find_element(By.ID,"id_signup_email")
        sign_email.send_keys(random_email())
        time.sleep(1)
        sign_phone = self.driver.find_element(By.ID,"id_signup_phone")
        random_number = random_phonenumber()
        sign_phone.send_keys(random_number)
        self.logger.info(random_number)
        time.sleep(2)
        sign_submit = self.driver.find_element(By.ID,"id_signup")
        sign_submit.click()
        time.sleep(2)

        conn = mysql.connector.connect(host=cld_host_live, database=cld_databasename_live, user=cld_username_live, password=cld_pass_live)
        # conn = mysql.connector.connect(host='cld_host_staging,database = cld_databasename_staging,user = cld_username_staging, password = cld_pass_staging)


        self.logger.info(conn)
        time.sleep(2)
        query = ("""select code from users_otp where phone_no = {} order by id desc""").format(random_number)
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            self.logger.info("No OTP found for phone number {}".format(random_number))
            return  # or raise an exception, depending on your use case
        result_dict = list(row)
        self.logger.info(result_dict)
        
        for index, value in enumerate(result_dict):
            otp_1_new = self.driver.find_element(By.ID,
                                                    "digit1".format(int(index) + 1))
            otp_1_new.send_keys(value)
            time.sleep(7)

        click_verify_button = self.driver.find_element(By.ID,"id_otp_verify")
        time.sleep(1)
        click_verify_button.click()
        time.sleep(2)
        cart_part_url = self.driver.current_url
        self.logger.info(cart_part_url)
        # assert cart_part_url == "https://www.collegedekho.com/caf/checkout?we_checkout=true&utm_source=&utm_medium=&utm_keywords="
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(2)
        click_proceed_button = self.driver.find_element(By.ID,"id-proceed-to-pay")
        time.sleep(1)
        click_proceed_button.click()

        paytm_url = self.driver.current_url
        self.logger.info(paytm_url)
        paytm_url_response = requests.get(paytm_url)
        paytm_url_status_code = paytm_url_response.status_code
        self.logger.info(f"Status Code for {paytm_url}: {paytm_url_status_code}")
        if paytm_url_status_code == 200:
            self.logger.info("CAf Working Properly")
        else:
            error_message = f"CAf returned a non-200 status code: {paytm_url_status_code}"
            self.logger.error(error_message)
            raise Exception(error_message)
        
        time.sleep(10)
