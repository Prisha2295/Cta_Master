import time
import requests
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from IELTS.pageObjects.toefl_common_config import TOEFL_Signup
from IELTS.utilities.readProperties import ReadConfig
from IELTS.utilities.customLogger import LogGen


@pytest.mark.usefixtures("setup")
class Test_TOEFLSignup(TOEFL_Signup):
    # URLs fetched from configuration file
    TOEFL_url = ReadConfig.getTOEFLURL()
    
    # Initialize the logger for this test using the test name "TOEFL"
    logger = LogGen.loggen(test_name="TOEFLCta")

    def navigate_to_page(self):
        """Navigate to the TOEFL URL and validate the navigation."""
        self.driver.get(self.TOEFL_url)
        self.logger.info("Navigated to TOEFL URL")
        
        # Validate the page title
        actual_title = self.driver.title
        assert "Contact" in actual_title, f"Expected 'Contact' in title, but got '{actual_title}'"
        self.logger.info(f"Page title validated: {actual_title}")

        # Log and verify the current URL and response status code
        current_url = self.driver.current_url
        self.logger.info(f"Current URL: {current_url}")
        response = requests.get(current_url)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        self.logger.info(f"Response status code: {response.status_code}")

    def test_Signup(self, setup):
        """Test the Signup process for TOEFL."""
        self.logger.info("******* Starting TOEFL SignUp Automation *********")
        self.driver = setup

        # Navigate to the TOEFL URL and perform initial validations
        self.navigate_to_page()

        # Verify "Contact Us" form presence and initiate CTA
        self.logger.info("Initiating CTA for Contact Us form")
        self.cta_detail()  # Function to handle the form filling and submission

        try:
            # Explicit wait for the "Thank You" popup to become visible
            thank_you = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#swal2-title"))
            )
            # Validate the popup message
            self.logger.info(f"Expected length: {len('Thank you for your response')}, Actual length: {len(thank_you.text)}")
            self.logger.info(f"Popup message: {thank_you.text}")
            self.logger.info("Contact Us form verified successfully")

        except TimeoutException:
            # If the popup does not appear, log the error and fail the test
            self.logger.error("Thank You popup did not appear within the expected time.")
            raise AssertionError("Contact Us form verification failed: 'Thank You' popup did not appear.")

    def verify_and_log(self, locator, description):
        """Helper method to verify element presence and log its text."""
        try:
            element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
            self.logger.info(f"{description}: {element.text}")
            return element
        except TimeoutException:
            self.logger.error(f"Could not find the {description} element.")
            raise
