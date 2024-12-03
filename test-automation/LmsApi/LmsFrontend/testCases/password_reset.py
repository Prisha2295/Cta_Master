import os
import time
import random
import string
from dotenv import load_dotenv,set_key
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


load_dotenv()

lms_preprod_pass = os.getenv("lms_preprod_pass")
lms_preprod_user = os.getenv("lms_preprod_user")
lms_profile_url = os.getenv("lms_profile_url")


def save_password_to_env(env_path, password_key, new_password):
    "Saves the new password to the specified .env file under the given key."

    if not os.path.exists(env_path):
        with open(env_path, 'w') as file:
            file.write("")  # Create the file if it doesn't exist

    # Load the existing .env file, update the key, and save the changes
    load_dotenv(env_path)
    set_key(env_path, password_key, new_password)
    load_dotenv(env_path)  # Reload environment variables after update

    print(f"Password updated in {env_path} under key '{password_key}'.")

def generate_password(self,length=8):
    if length < 4:  # Adjusted to ensure space for each type of required character
        raise ValueError("Password length must be at least 4 characters to include one lowercase, one uppercase, one digit, and one symbol.")

    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Ensure the password includes at least one of each required character type
    password_chars = [
        random.choice(lowercase_letters),  # Lowercase letter
        random.choice(uppercase_letters),  # Uppercase letter
        random.choice(digits),             # Digit
        random.choice(punctuation)         # Punctuation
    ]

    # If the desired length is more than 4, fill the rest with a mix of all characters
    if length > 4:
        all_characters = lowercase_letters + uppercase_letters + digits + punctuation
        password_chars.extend(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the list to randomize the order of characters
    random.shuffle(password_chars)

    # Join the list into a string to form the final password
    new_password = ''.join(password_chars)

    return new_password

def perform_standard_login(self):
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
    mobile_field = self.driver.find_element(By.ID, "username")
    mobile_field.clear()
    mobile_field.send_keys(lms_preprod_user)
    self.logger.info("Username entered.")


    # Wait until the password field is visible and then input the password
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "password-input")))
    password_field = self.driver.find_element(By.ID, "password-input")
    password_field.clear()
    password_field.send_keys(lms_preprod_pass)
    self.logger.info("Password entered.")

    # Wait for the submit button to be clickable and then click it
    submit_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")),
        message="Submit button not clickable"
    )
    submit_button.click()
    self.logger.info("Login form submitted.")

def handle_password_reset(self):
    # Assume this function resets the password
    self.logger.info("Resetting password due to security breach...")
    
    # Generate and save new password
    new_password = generate_password(self)

    # Click on the button with class "btn btn-secondary"
    WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-secondary"))
    )
    self.driver.find_element(By.CLASS_NAME, "btn.btn-secondary").click()
    self.logger.info("Clicked on reset button.")
    time.sleep(5)

    # Input the old password
    WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "old_password"))
    )
    old_password_input = self.driver.find_element(By.ID, "old_password")
    old_password_input.send_keys(lms_preprod_pass)  # Assuming old password is stored in env
    self.logger.info("Old password entered.")

    # Input the new password
    new_password_input = self.driver.find_element(By.ID, "new_password")
    new_password_input.send_keys(new_password)
    self.logger.info(f"New password entered: {new_password}")

    # Confirm the new password
    confirm_password_input = self.driver.find_element(By.ID, "confirm_password")
    confirm_password_input.send_keys(new_password)
    self.logger.info("Confirmed new password.")

    # Click the submit button to complete the password reset
    WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-success.w-100"))
    )
    self.driver.find_element(By.CLASS_NAME, "btn.btn-success.w-100").click()
    self.logger.info("Password reset submitted successfully.")

    # Save the new password to the .env file
    env_path = '/Users/parveenyadav/test-automation/.env'
    save_password_to_env(env_path, 'lms_preprod_pass', new_password)
    self.logger.info("Detected login page after password reset.")
    time.sleep(5)
    perform_standard_login(self)



def handle_url_conditions(self):
    # Wait until any URL change that could be a redirect post-login or another action
    try:
        WebDriverWait(self.driver, 10).until(EC.url_contains("/lead-dashboard"))
        self.logger.info("URL changed to /lead-dashboard")
        print("URL changed to /lead-dashboard")
    except Exception as e:
        self.logger.info(f"Failed to load lead-dashboard page: {e}")
        print(f"Failed to load lead-dashboard page: {e}")

    # Check the current URL and decide what to do next
    current_url = self.driver.current_url
    if "/securityBreach?reset" in current_url:
        self.logger.info("Detected security breach reset condition.")
        handle_password_reset(self)
        time.sleep(2)

    elif "/login" in current_url:
        self.logger.info("Detected login page.")
        self.perform_standard_login()

    elif "/my-profile" in current_url:
        self.logger.info("Logged into profile page.")
        # Logic to navigate to /login if necessary:
        self.driver.get(lms_profile_url + 'lead-dashboard')
        self.logger.info("Redirected back to login page.")



