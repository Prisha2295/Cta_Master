import time
import random
from faker import Faker
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException
)

def generate_words(count=20, chunk_size=3):
    """Generate random words for testing inputs, chunked into specified sizes."""
    fake = Faker()
    # Generate a list of random words
    words = [fake.word() for _ in range(count)]
    # Chunk each word into parts of length chunk_size
    chunked_words = []
    for word in words:
        chunked_word = ' '.join(word[i:i+chunk_size] for i in range(0, len(word), chunk_size))
        chunked_words.append(chunked_word)
    return chunked_words

# Generate and print the word list
word_list = generate_words()

def lead_remark(self):
    lms_communication_element = ("//label[normalize-space()='Dialer Call Dispose']",
                             "//label[normalize-space()='Outside LMS Communication']")

    # Select a random element from the tuple
    selected_xpath = random.choice(lms_communication_element)

    # Locate the element
    try:
        select_reason_for_update = self.driver.find_element(By.XPATH, selected_xpath)
        time.sleep(2)
        self.logger.info(f"Selected reason text: {select_reason_for_update.text}")
        
        # Click the element
        select_reason_for_update.click()
        time.sleep(2)
        
    except Exception as e:
        self.logger.error(f"Error selecting and clicking element: {e}")


    Intentelement = ("//label[normalize-space()='Cold']","//label[normalize-space()='Hot']","//label[normalize-space()='Warm']")
    # Select a random element from the tuple
    selected_intent_random = random.choice(Intentelement)

    try:
        intent_update = self.driver.find_element(By.XPATH,selected_intent_random)
        time.sleep(2)
        self.logger.info(f"Selected Intent text: {intent_update.text}")
        print(f"Selected Intent text: {intent_update.text}")

        intent_update.click()
        time.sleep(2)

    except Exception as e:
        self.logger.error(f"Error selecting and clicking element: {e}")

    # Find the dropdown element
    sub_stage_element = self.driver.find_element(By.XPATH, "//select[@aria-label='Default select example']")
    sub_stage = Select(sub_stage_element)

    # Get all enabled options (excluding the disabled ones)
    available_options = [option for option in sub_stage.options if option.is_enabled()]

    # Select a random option
    random_option = random.choice(available_options)
    sub_stage.select_by_visible_text(random_option.text)

    # Log the selected option
    self.logger.info("Product Status: " + random_option.text)

    time.sleep(4)

    callback_select_date = self.driver.find_element(By.XPATH,"//input[@id='date-field']")
    callback_select_date.click()
    time.sleep(2)

    # Generate the current date in the required format (e.g., 'September 2, 2024')
    current_date = datetime.now().strftime('%B %d, %Y')
    date_xpath = ".open .today"
    

    try:
        for _ in range(3):  # Retry mechanism to handle stale elements
            try:
                # Locate the date element using the constructed XPath
                date_element = self.driver.find_element(By.CSS_SELECTOR, date_xpath)

                # Scroll the date element into view to avoid any obstruction issues
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", date_element)
                time.sleep(1)  # Pause briefly to allow scrolling to complete

                # Check for overlays or obstructions and try to dismiss them if present
                try:
                    overlays = self.driver.find_elements(By.CSS_SELECTOR, '.overlay, .popup-close-btn')
                    for overlay in overlays:
                        self.driver.execute_script("arguments[0].click();", overlay)
                        time.sleep(0.5)  # Allow time for the overlay to be dismissed
                    self.logger.info("Dismissed obstructive overlays.")
                except Exception as e:
                    self.logger.info(f"No overlays to dismiss or unable to dismiss: {e}")

                # Re-locate the date element after dismissing overlays (to avoid stale reference)
                date_element = self.driver.find_element(By.CSS_SELECTOR, date_xpath)

                try:
                    # Attempt to click on the date element using JavaScript to bypass click interception
                    self.driver.execute_script("arguments[0].click();", date_element)
                    time.sleep(1)  # Allow time for the action
                    date_element.click()  # Attempt a standard click as a backup
                    self.logger.info(f"Clicked on the date: {current_date}")
                except ElementClickInterceptedException as e:
                    self.logger.warning(f"Click intercepted on the first attempt: {e}")

                    # Retry clicking the element by scrolling it back into view and attempting click again
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", date_element)
                    self.driver.execute_script("arguments[0].click();", date_element)
                    self.logger.info("Retried clicking the element successfully.")
                break  # Break out of the retry loop if successful

            except StaleElementReferenceException as e:
                self.logger.warning(f"Stale element reference encountered, retrying: {e}")
                time.sleep(1)  # Wait before retrying

    except NoSuchElementException as e:
        self.logger.error(f"Date element not found: {e}")
    except Exception as e:
        self.logger.error(f"Unexpected error occurred: {e}")

    try:
        
        time.sleep(5)
        callback_select_time = self.driver.find_element(By.XPATH,"(//div[@class='dropdown-selected-value'])[1]")
        time.sleep(5)
        callback_select_time.click()
        time.sleep(3)  # Brief pause to allow the dropdown to open

        options = self.driver.find_element(By.XPATH,"//div[@class='dropdown-menu drop1']")
        time.sleep(2)
        self.logger.info(options.text)
        time.sleep(5)

        click_on_7 = self.driver.find_element(By.XPATH,"(//div[@class='dropdown-item false'])[10]")
        time.sleep(5)
        click_on_7.click()
        time.sleep(5)

    except NoSuchElementException as e:
        self.logger.info(e)

    try:
        click_on_time = self.driver.find_element(By.XPATH,"(//a)[30]")
        time.sleep(3)
        click_on_time.click()
        time.sleep(5)
    except NoSuchElementException as e:
        self.logger.error(f"Error finding the time slots: {e}")

    remark_add = self.driver.find_element(By.ID,"validationTextarea")
    time.sleep(2)
    remark_add.send_keys(self.generate_words())
    time.sleep(5)

    click_on_remark_submit = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Submit Form'])[1]")
    time.sleep(2)
    click_on_remark_submit.click()
    time.sleep(2)