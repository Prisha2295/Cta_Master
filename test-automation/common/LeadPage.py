from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class LeadPage:
    def __init__(self, driver, logger, timeout=10):
        self.driver = driver
        self.logger = logger
        self.timeout = timeout

    def enter_name(self, name):
        try:
            name_field = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@id='validationCustom01']"))
            )
            name_field.send_keys(name)
            self.logger.info(f"Name entered: {name}")
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Error entering name: {e}")

    def enter_email(self, email):
        try:
            email_field = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@id='validationCustom02']"))
            )
            email_field.send_keys(email)
            self.logger.info(f"Email entered: {email}")
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Error entering email: {e}")

    def enter_phone(self, phone):
        try:
            phone_field = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((By.XPATH, "//ul[@class='mobileInput']//input[1]"))
            )
            phone_field.send_keys(phone)
            self.logger.info(f"Phone number entered: {phone}")
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Error entering phone: {e}")

    def submit_form(self):
        try:
            submit_button = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
            )
            submit_button.click()
            self.logger.info("Form submitted successfully")
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Submit button not found: {e}")

    def check_error_message(self, field_name):
        """Check if an error message is displayed after an invalid submission."""
        try:
            error_message = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((By.XPATH, f"//div[@class='invalid-feedback' and @data-field='{field_name}']"))
            )
            if error_message.is_displayed():
                self.logger.info(f"Error message displayed for {field_name}: {error_message.text}")
                return error_message.text
        except (TimeoutException, NoSuchElementException):
            self.logger.info(f"No error message displayed for {field_name}")
            return None
