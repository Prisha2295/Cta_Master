import os
import mysql.connector
from mysql.connector import Error
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

class OTPPage:
    def __init__(self, driver, logger, timeout=10):
        self.driver = driver
        self.logger = logger
        self.timeout = timeout
        # Load environment variables for the database
        self.db_host = os.getenv("cld_host_staging")
        self.db_user = os.getenv("cld_username_staging")
        self.db_pass = os.getenv("cld_pass_staging")
        self.db_name = os.getenv("cld_databasename_staging")

    def fetch_otp_from_db(self, phone_number):
        """Fetch the latest OTP from the database for a given phone number."""
        try:
            # Establish a database connection using environment variables
            conn = mysql.connector.connect(
                host=self.db_host,
                user=self.db_user,
                password=self.db_pass,
                database=self.db_name
            )

            if conn.is_connected():
                self.logger.info("Connected to the database")

                # Query to fetch the OTP for the provided phone number
                query = ("""
                    SELECT code FROM users_otp WHERE phone_no = %s ORDER BY id DESC LIMIT 1
                """)
                cursor = conn.cursor()
                cursor.execute(query, (phone_number,))

                # Fetch the OTP result
                row = cursor.fetchone()
                if row:
                    otp_code = row[0]
                    self.logger.info(f"Fetched OTP: {otp_code}")
                    return otp_code
                else:
                    self.logger.error("No OTP found for the given phone number")
                    return None

        except Error as e:
            self.logger.error(f"Error connecting to the database: {e}")
        finally:
            # Ensure the database connection is closed
            if conn.is_connected():
                conn.close()
                self.logger.info("Database connection closed")

    def enter_otp(self, otp_code):
        """Enter the fetched OTP into the input fields."""
        try:
            for index, digit in enumerate(otp_code):
                otp_input = WebDriverWait(self.driver, self.timeout).until(
                    EC.visibility_of_element_located((By.XPATH, f"(//input[@placeholder='-'])[{index + 1}]"))
                )
                otp_input.send_keys(digit)
            self.logger.info("OTP entered successfully")
        except NoSuchElementException as e:
            self.logger.error(f"OTP input field not found: {e}")

    def verify_otp(self):
        """Click the OTP verification button."""
        try:
            verify_button = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='gtm_loginVerify']"))
            )
            verify_button.click()
            self.logger.info("OTP verification completed")
        except NoSuchElementException as e:
            self.logger.error(f"Verify button not found: {e}")
