import time
import requests
from selenium.webdriver.common.by import By
from common_functions import commonfunctions
from utilities.Readproperties import ReadConfig
from utilities.customlogger import Logs
from common_functions import *

class Test_Jobassuredlisting(commonfunctions):
    
    baseUrl = ReadConfig.JobassuredlistingURL()

    def test_Jobassuredlistingcta(self, setup):
        self.logger = Logs.loggen('Test Jobassuredlisting')  # logger of current test case
        self.logger.info("******* Starting CTA TEST JOBASSUREDLISTING**********")
        
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
        Phone_no = self.driver.find_element(By.XPATH,"//input[@id='id_phone_no']")
        Phone_no.send_keys(random_no)
        self.logger.info(random_no)
        time.sleep(3)
        Submit_Button = self.driver.find_element(By.XPATH,"//button[@id='id-book-open-demo']")
        Submit_Button.click()
        Submit_Text= Submit_Button.text
        self.logger.info( "CTA Text : " + Submit_Text)
        time.sleep(3)

       
        