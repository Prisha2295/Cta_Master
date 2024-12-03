import time
import requests
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from IELTS.pageObjects.ielts_common_config import Ielts_Signup
from IELTS.utilities.readProperties import ReadConfig
from IELTS.utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class Test_IELTSignup(Ielts_Signup):

    # URLs loaded from config
    IELTS_url = ReadConfig.getIELTSURL()
    Article_url = ReadConfig.getArticleURL()
    logger = LogGen.loggen(test_name="IELTSCta")

    def log_page_info(self):
        """Logs current page title, URL, and status code."""
        actual_title = self.driver.title
        current_url = self.driver.current_url
        response = requests.get(current_url)

        self.logger.info(f"Page title: {actual_title}")
        self.logger.info(f"Current URL: {current_url}")
        self.logger.info(f"Response status code: {response.status_code}")

    def click_element(self, locator_type, locator, wait_time=10):
        """Generic method to wait for and click a web element."""
        element = WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable((locator_type, locator))
        )
        element.click()
        self.logger.info(f"Clicked on element located by: {locator_type} = {locator}")
        return element

    def perform_signup(self):
        """Perform the Signup actions for IELTS."""
        # Navigate to the signup page
        self.click_element(By.CSS_SELECTOR, ".ielts-header-login-btn-txt")
        
        # Click on the Signup button
        self.click_element(By.CSS_SELECTOR, "div[class='ielts-otp-ctn'] a[class='signUpLink getLeadForm']")
        time.sleep(3)

        # Fill the signup form (from Ielts_Signup class method)
        self.cta_detail()
        time.sleep(2)

        # Close the demo popup if it appears
        self.click_element(By.CSS_SELECTOR, ".ieltsmaterialIcons.closeIcon.ielts-dialog-close-btn.desktop_only")

        # Verify successful signup and log username
        signup_verify = self.driver.find_element(By.XPATH, "//span[@class='ielts-header-login-btn-txt']")
        logged_username = signup_verify.text
        self.logger.info("Logged UserName: " + logged_username)

        # Hover over the signup verification element
        actions = ActionChains(self.driver)
        actions.move_to_element(signup_verify).perform()
        time.sleep(2)
        self.logger.info("SignUp Success")

        # Retrieve and log text from the menu items
        menu_items = self.driver.find_elements(By.XPATH, "//div[@class='ielts-header-login-menu']//a")
        texts = [item.text for item in menu_items]
        self.logger.info(f"Menu Items: {texts}")

    def signout_user(self):
        """Logs out the currently signed-in user."""
        signout_btn = self.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Sign Out']")
        signout_btn.click()
        time.sleep(3)
        self.logger.info("SignOut Success")

    def download_article_cta(self):
        """Handles clicking on the 'Download Now' CTA on article pages."""
        try:
            # Wait for the "Download Now" button to be present
            download_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".ielts-cue-card-sixth-btn"))
            )
            self.logger.info("Download button found.")

            # Scroll to the button and adjust scroll position
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", download_button)
            time.sleep(0.5)  # Allow time for the smooth scrolling to complete
            self.driver.execute_script("window.scrollBy(0, -50);")  # Adjust scroll position to bring the button into view

            # Click on the button after ensuring it is visible and clickable
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of(download_button)  # Ensure the button is visible
            )
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(download_button)  # Ensure the button is clickable
            ).click()

            self.logger.info("Clicked on the 'Download Now' button successfully!")

            # Handle lead form submission if present
            self.cta_detail()
            time.sleep(3)  # Wait after form submission
            self.logger.info("Lead form submitted")

        except Exception as e:
            self.logger.error(f"An error occurred: {str(e)}")
            raise

    def test_Signup(self, setup):
        """Test to validate the signup functionality."""
        self.logger.info("******* Starting IELTS Test Script *********")
        self.driver = setup
        self.driver.get(self.IELTS_url)
        self.logger.info("Navigated to IELTS Sign-Up Page")

        self.log_page_info()
        time.sleep(2)
        self.perform_signup()
        self.signout_user()

    def test_articlecta(self, setup):
        """Test to validate the CTA on article pages."""
        self.logger.info("******* Starting IELTS CTA's Automation *********")
        self.driver = setup
        self.driver.get(self.Article_url)
        self.logger.info("Navigated to Article Page")

        self.log_page_info()
        time.sleep(2)
        self.download_article_cta()
