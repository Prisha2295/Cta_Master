
import numbers
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector
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


class GIS_Signup():
    random_generated_number = None

    def cta_detail(self):

        time.sleep(2)

        random_name = random_namee()
        Name = self.driver.find_element(By.ID, "leadpopupform-fullname")
        Name.send_keys(random_name)
        self.logger.info("Name : " + random_name)
        
        random_emaill = self.random_email()
        self.driver.find_element(By.ID, "leadpopupform-email").send_keys(random_emaill)
        time.sleep(1)
        self.logger.info("Email : " + random_emaill)
        time.sleep(3)

        application = Select(self.driver.find_element(By.CSS_SELECTOR,"#leadpopupform-applicationcategoryid"))
        application.select_by_index(3)
        App = application.first_selected_option.text
        self.logger.info("Type of Application: " + App)
        time.sleep(2)

        random_password = generate_random_password()
        Password = self.driver.find_element(By.XPATH, "//input[@type='password']")
        Password.send_keys(random_password)
        self.logger.info("Passsword : " + random_password)
        time.sleep(3)


        # Click to open the country code dropdown
        dropdown_trigger = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@title='India (भारत): +91']"))
        )
        dropdown_trigger.click()

        # Wait for the dropdown to expand and the country options to be visible
        select_country = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li[id='iti-item-af'] span[class='iti__country-name']"))  
        )
        select_country.click()

        # Get the selected country
        selected_country = select_country.text 
        # self.logger.info(selected_country)

        time.sleep(2)

        random_number = self.random_phonenumber()

        self.random_generated_number = random_number


        self.driver.find_element(By.ID, "leadpopupform-mobile").send_keys(random_number)
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
