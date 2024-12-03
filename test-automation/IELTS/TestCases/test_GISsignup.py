import time
import requests
import pytest
import random
import string
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from IELTS.pageObjects.gis_common_config import GIS_Signup
from IELTS.utilities.readProperties import ReadConfig
from IELTS.utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class Test_GISignup(GIS_Signup):
    GIS_Url = ReadConfig.getGISURL()
    GISService_Url = ReadConfig.getServiceURL()
    logger = LogGen.loggen(test_name="GISCta")

    def test_Signup(self, setup):
        self.logger.info("******* Starting Get GIS SignUp Automation *********")
        self.logger.info(f"GIS URL: {self.GIS_Url}")
        self.driver = setup
        self.load_page(self.GIS_Url)

        # Navigate to Sign-Up page
        self.navigate_to_signup()

        # Verify successful sign-up
        self.verify_signup_success()

        # Sign out after successful sign-up
        self.sign_out()

    def load_page(self, url):
        """Load the specified URL and log the status."""
        try:
            self.driver.get(url)
            self.logger.info("Page loaded successfully")
        except Exception as e:
            self.logger.error(f"Failed to load URL: {url}. Exception: {str(e)}")
            assert False, "Failed to load the URL"

        self.log_page_details()

    def log_page_details(self):
        """Log the current page title and URL."""
        time.sleep(2)
        actual_title = self.driver.title
        self.logger.info(f"Page title: {actual_title}")
        
        current_url = self.driver.current_url
        self.logger.info(f"Current URL: {current_url}")
        response = requests.get(current_url)
        self.logger.info(f"Response: {response.status_code}")
        time.sleep(2)

    def navigate_to_signup(self):
        """Navigate to the Sign-Up page."""
        login_signup_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='login-button']"))
        )
        login_signup_btn.click()
        self.logger.info("Navigated to Sign-Up page")
        
        time.sleep(2)
        signup_btn = self.driver.find_element(By.XPATH, "//div[@class='stepOne otpLogin']//p[2]//a[1]")
        signup_btn.click()
        time.sleep(3)

        self.cta_detail()  # Call additional functionality for CTA
        time.sleep(2)

    def verify_signup_success(self):
        """Verify if the user has signed up successfully."""
        signup_verify = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".login_cta_button_nav"))
        )
        logged_in = signup_verify.text.strip()
        self.logger.info("Logged UserName: " + logged_in)
        self.logger.info("SignUp Success")

    def sign_out(self):
        """Sign out from the application."""
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.CSS_SELECTOR, ".login_cta_button_nav")).perform()
        time.sleep(2)

        signout_btn = self.driver.find_element(By.XPATH, "//ul[@class='userDropdown dropdown-menu']//a[normalize-space()='Sign Out']")
        signout_btn.click()
        time.sleep(3)
        self.logger.info("SignOut Success")

    def test_giscta(self, setup):
        self.logger.info("******* Starting Get GIS CTA Automation *********")
        self.logger.info(f"GIS Service URL: {self.GISService_Url}")
        self.driver = setup
        self.load_page(self.GISService_Url)

        # Fill out the CTA form
        self.fill_cta_form()

    def fill_cta_form(self):
        """Fill out the CTA form with random data."""
        time.sleep(3)

        random_name = self.generate_random_name()
        self.driver.find_element(By.ID, "countrypageform-fullname").send_keys(random_name)
        self.logger.info("Name: " + random_name)

        random_email = self.random_email()
        self.driver.find_element(By.ID, "countrypageform-email").send_keys(random_email)
        self.logger.info("Email: " + random_email)
        time.sleep(1)

        random_number = self.random_phonenumber()
        self.driver.find_element(By.XPATH, "//input[@id='countrypageform-mobile']").send_keys(random_number)
        self.logger.info("Phone No: " + random_number)
        time.sleep(2)

        # Select application category
        application = Select(self.driver.find_element(By.ID, "countrypageform-applicationcategoryid"))
        application.select_by_index(3)
        app_text = application.first_selected_option.text
        self.logger.info("Type of Application: " + app_text)
        time.sleep(2)

        # Submit the form
        self.driver.find_element(By.ID, "submitCountryPageForm").click()
        time.sleep(3)
        self.logger.info("Lead form submitted")

    def generate_random_name(self):
        """Generate a random name for the form."""
        return 'Test' + "".join(random.choices(string.ascii_lowercase, k=6))

    def random_email(self):
        """Generate a random email."""
        return ''.join(random.choices(string.ascii_lowercase, k=5)) + "@example.com"

    def random_phonenumber(self):
        """Generate a random phone number."""
        return ''.join(random.choices(string.digits, k=10))
