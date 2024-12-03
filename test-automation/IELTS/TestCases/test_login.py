import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from IELTS.pageObjects.ielts_common_config import Ielts_Signup
from IELTS.utilities.readProperties import ReadConfig
from IELTS.utilities.customLogger import LogGen

class Test_Signup(Ielts_Signup):

    Base_url = ReadConfig.getIELTSURL() 
    logger = LogGen.loggen()  # Logger

    def test_Login(self, setup):
        time.sleep(2)
        self.logger.info("******* Starting IELTS Login Automation*********")
        self.driver = setup
        self.driver.get(self.Base_url)
        self.logger.info("-------------------------")

        # Verify page title and log it
        actual_title = self.driver.title
        self.logger.info(f"Page title: {actual_title}")
        time.sleep(2)
        
        # Log current URL and status code
        current_url = self.driver.current_url
        self.logger.info(f"Current URL: {current_url}")
        response = requests.get(current_url)
        self.logger.info(f"Response: {response.status_code}")
        time.sleep(2)

        # Navigate to the Sign-Up page
        login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".ielts-header-login-btn-txt"))
        )
        login_btn.click()
        self.logger.info("Navigated to Login page")
        time.sleep(2)


