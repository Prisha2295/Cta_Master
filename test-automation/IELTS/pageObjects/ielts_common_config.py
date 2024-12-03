from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
from selenium.webdriver.support.ui import Select
import os


def random_namee():
    return 'Test' + "".join(random.choices(string.ascii_lowercase, k=6))

def generate_random_password():
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(characters)
    password = []
    for i in range(1,10):
        password.append(random.choice(characters))
        random.shuffle(password)
    return "".join(password)


class Ielts_Signup():
    random_generated_number = None

    def cta_detail(self):

        time.sleep(2)
        try:
            random_name = random_namee()
            Name = self.driver.find_element(By.ID, "leadsignupform-fullname")
            Name.send_keys(random_name)
            self.logger.info("Name : " + random_name)
        except:
            random_name = random_namee()
            Name = self.driver.find_element(By.XPATH, "//input[@id='id_name_signup']")
            Name.send_keys(random_name)
            self.logger.info("Name : " + random_name)
        
        try:
            random_emaill = self.random_email()
            self.driver.find_element(By.ID, "leadsignupform-email").send_keys(random_emaill)
            time.sleep(1)
            self.logger.info("Email : " + random_emaill)
        except:
            random_emaill = self.random_email()
            self.driver.find_element(By.XPATH, "//input[@id='id_email_signup']").send_keys(random_emaill)
            time.sleep(1)
            self.logger.info("Email : " + random_emaill)

        exam = Select(self.driver.find_element(By.ID,"leadsignupform-applicationcategoryid"))
        exam.select_by_index(1)
        Exam = exam.first_selected_option
        self.logger.info("Pref Stream : " + Exam.text)
        time.sleep(2)


#changing country code
        # Click to open the country code dropdown
        country_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='form-group field-leadsignupform-mobile'] div[title='India (भारत): +91']"))
        )
        country_dropdown.click()

        # Wait for the dropdown to expand and the country options to be visible
        select_country = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='form-group field-leadsignupform-mobile']//li[@id='iti-item-af']"))
        )
        
        # Click on the Albania country code
        select_country.click()

        # Optional: Add a sleep if needed to observe the result (for debugging)
        time.sleep(2)

        random_number = self.random_phonenumber()

        self.random_generated_number = random_number


        self.driver.find_element(By.XPATH, "(//input[@id='leadsignupform-mobile'])[1]").send_keys(random_number)
        time.sleep(2)
        self.logger.info("Phone No : " + random_number)
        time.sleep(4)

        # Submit button
        self.driver.find_element(By.ID, "js-submit-signup-form").click()
        time.sleep(3)
        return random_number, random_emaill, random_name

    def random_phonenumber(self):

        ph_no = []

        ph_no.append(random.randint(6, 9))

        for i in range(1, 10):
            ph_no.append(random.randint(0, 9))

        number = ""

        for i in ph_no:
            print(i, end="")
            number += str(i)
        print(number)

        return number



    def random_email(self):
        random_str = 'Test-' + "".join(random.choice(string.ascii_letters) for _ in range(7))
        return random_str + "@gmail.com"