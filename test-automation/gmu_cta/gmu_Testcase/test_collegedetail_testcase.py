import time
import pytest
import requests
from gmu_cta.Conftest import setup 
from selenium.webdriver.common.by import By
from .gmu_commonfunctions import commonfunctions
from ..gmu_utilities.Readproperties import ReadConfig
from ..gmu_utilities.custom_logger import Logs


@pytest.mark.usefixtures("setup")
class Test_Collegedetail(commonfunctions):
    baseUrl = ReadConfig.CollegedetailURL()

    def test_collegedetailcta(self,setup):
        self.logger = Logs.loggen('Test Collegedetail')  # logger of current test case
        self.logger.info("******* Starting CTA TEST COLLEGEDETAIL**********")
        
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
        apply_now_cta = self.driver.find_element(By.XPATH,"//button[@class='primaryBtn writeReview newHeroButtons getLeadForm courseCategory js-open-lead-form-new']")
        time.sleep(0.5)
        apply_now_cta.click()
    
        self.gmu_happyflow()
        time.sleep(5)
        
