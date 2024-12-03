import time
import requests
from selenium.webdriver.common.by import By
from common_functions import commonfunctions
from utilities.Readproperties import ReadConfig    
from utilities.customlogger import Logs
from common_functions import *
from database import *
from selenium.webdriver.common.keys import Keys

collegedekho_user1 = os.getenv("collegedekho_user1")
collegedekho_pass1 = os.getenv("collegedekho_pass1")

class Test_DashboardCheck(commonfunctions):
        
    
    baseUrl = ReadConfig.ExamDashboardURL()
    baseUrl1 = ReadConfig.NewsDashboardURL()
    baseUrl2 = ReadConfig.CMSDashboardURL()

    def test_dashboardcheck(self, setup):
        self.logger = Logs.loggen('Test_Dashboardcheck')  
        
        # Initialize the 'driver' attribute
        self.driver = setup
        
        self.driver.get(self.baseUrl)
        self.logger.info("Starting Exam Dashboard Check")
        get_url = self.driver.current_url
        self.logger.info(get_url)

        login_With_password = self.driver.find_element(By.XPATH, "(//a[normalize-space()='Login via Password'])[1]")
        login_With_password.click()
        time.sleep(2)

        Email_fill = self.driver.find_element(By.XPATH, "//input[@name='login']")
        Email_fill.send_keys(collegedekho_user1)

        Password_fill = self.driver.find_element(By.XPATH, "//input[@id='pass_log_id']")
        Password_fill.send_keys(collegedekho_pass1)

        login_click = self.driver.find_element(By.XPATH, "//input[@id='gtm_login']")
        login_click.click()
        time.sleep(2)

        add_exam = self.driver.find_element(By.XPATH, "(//a[normalize-space()='Create Base Exam'])[1]")
        time.sleep(5)
        add_exam.click()
        time.sleep(2)

        self.driver.get(self.baseUrl1)
        self.logger.info("Starting News Dashboard Check")

        add_news = self.driver.find_element(By.XPATH, "(//a[normalize-space()='Add News'])[1]")
        add_news.click()
        time.sleep(2)

        self.driver.get(self.baseUrl2)
        self.logger.info("Starting CMS Dashboard Check")

        Email_fill_cms = self.driver.find_element(By.XPATH, "(//input[@id='basic_email'])[1]")
        Email_fill_cms.send_keys(Keys.CONTROL + "a") 
        Email_fill_cms.send_keys(Keys.BACKSPACE)   
        time.sleep(2)
        Email_fill_cms.send_keys(collegedekho_user1)

        Password_fill_cms = self.driver.find_element(By.XPATH, "(//input[@id='basic_password'])[1]")
        Password_fill_cms.send_keys(Keys.CONTROL + "a")  
        Password_fill_cms.send_keys(Keys.BACKSPACE)   
        time.sleep(2)
        Password_fill_cms.send_keys(collegedekho_pass1)

        login_click_cms = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Sign In'])[1]")
        login_click_cms.click()
        time.sleep(2)

        add_institute = self.driver.find_element(By.XPATH, "(//span[normalize-space()='Add New Institute'])[1]")
        add_institute.click()
        time.sleep(2)

