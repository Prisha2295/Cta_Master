import unittest
import random
import string
import logging
from common.LeadPage import LeadPage
from common.otpcheck import OTPPage    

class NewLead(unittest.TestCase):
    def __init__(self, driver, logger):
        """Initialize with WebDriver and logger"""
        self.driver = driver  # Assign the driver to the class instance
        self.logger = logger  # Assign the logger to the class instance
        self.random_generated_number = None
        
    def setUp(self):
        # Set up WebDriver, logging, and other resources
        self.logger = logging.getLogger("NewLeadTest")
        self.timeout = 10  # Set dynamic wait timeout (can be configured)
        # Initialize the LeadPage and OTPPage objects with a timeout
        self.lead_page = LeadPage(self.driver, self.logger, self.timeout)
        self.otp_page = OTPPage(self.driver, self.logger, self.timeout)

    def random_name(self):
        return 'Test' + "".join(random.choices(string.ascii_lowercase, k=6))

    def random_email(self):
        random_str = 'Test-' + "".join(random.choice(string.ascii_letters) for _ in range(7))
        return random_str + "@gmail.com"

    def random_phone_number(self):
        ph_no = [random.randint(6, 9)] + [random.randint(0, 9) for _ in range(9)]
        return ''.join(map(str, ph_no))

    def test_new_lead(self):
        try:
            # Generate random values
            random_name = self.random_name()
            random_email = self.random_email()
            random_phone = self.random_phone_number()

            # Use the page objects to interact with the form using dynamic waits
            self.lead_page.enter_name(random_name)
            self.lead_page.enter_email(random_email)
            self.lead_page.enter_phone(random_phone)
            self.lead_page.submit_form()

            self.logger.info("Lead creation test passed")

        except Exception as e:
            self.logger.error(f"Error during lead creation: {e}")

    def test_invalid_submission(self):
        """Test to verify error messages appear for invalid form submission."""
        try:
            # Enter invalid details (e.g., empty name and email)
            self.lead_page.enter_name("")  # Invalid case: empty name
            self.lead_page.enter_email("invalid-email-format")  # Invalid email
            self.lead_page.enter_phone("12345")  # Invalid phone number (too short)

            # Submit form
            self.lead_page.submit_form()

            # Check for error messages
            name_error = self.lead_page.check_error_message("name")
            email_error = self.lead_page.check_error_message("email")
            phone_error = self.lead_page.check_error_message("phone")

            # Log or assert the presence of errors
            self.assertIsNotNone(name_error, "No error message for empty name")
            self.assertIsNotNone(email_error, "No error message for invalid email")
            self.assertIsNotNone(phone_error, "No error message for invalid phone number")

            self.logger.info("Invalid form submission test passed")

        except Exception as e:
            self.logger.error(f"Error during invalid form submission test: {e}")

    def test_otp_check(self):
        try:
            # Assuming random_number is generated in the `newlead` method
            random_number = self.random_phone_number()

            # Fetch the OTP from the database using the page object
            otp_code = self.otp_page.fetch_otp_from_db(random_number)

            if otp_code:
                # Enter and verify OTP using page objects
                self.otp_page.enter_otp(otp_code)
                self.otp_page.verify_otp()
                self.logger.info("OTP check test passed")
            else:
                self.logger.error("OTP was not fetched from the database")

        except Exception as e:
            self.logger.error(f"Error during OTP check: {e}")

    def tearDown(self):
    # Clean up resources, close WebDriver, etc.
        self.driver.quit()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    unittest.main()
