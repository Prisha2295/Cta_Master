import time
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import mysql.connector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import os
from dotenv import load_dotenv

load_dotenv()

cld_host_live = os.getenv("cld_host_live")
cld_username_live = os.getenv("cld_username_live")
cld_pass_live = os.getenv("cld_pass_live")
cld_databasename_live = os.getenv("cld_databasename_live")

cld_host_staging = os.getenv("cld_host_staging")
cld_username_staging = os.getenv("cld_username_staging")
cld_pass_staging = os.getenv("cld_pass_staging")
cld_databasename_staging = os.getenv("cld_databasename_staging")


def random_namee():
    return 'test' + "".join(random.choices(string.ascii_lowercase, k=6))

random_names = random_namee()

def random_phonenumber():

        ph_no = []

        ph_no.append(random.randint(6, 9))

        for i in range(1, 10):
            ph_no.append(random.randint(0, 9))

        number = ""

        for i in ph_no:
            number += str(i)
       
        return number

randomnumber = random_phonenumber()

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

random_password = generate_random_password()


def random_email():
        random_str = 'test-' + "".join(random.choice(string.ascii_lowercase) for _ in range(7))
        return random_str + "@gmail.com"

random_emails = random_email()

# name_negative = [' ','123','name@','  1name','@1name']
name_negative = ['name@']
# name_positive = ['name','  name name','NAME','NaMe','Name nAmE','name.com','.name']
name_positive = ['name','nAmE']
# phone_negative = ['5604403033','@@@@^&@^@&', 'name name ', 'name123', 'name@123.com', '0123456789']
phone_negative = ['5604403033','@@@@^&@^@&']
# phone_postive = ['6543210987','7383948473','8789012345','9012345678']
phone_positive = ['6543210987','7383948473']
# email_negative = ['emailtextaddress','@#@@##@%^%#$@#$@#.com','@email.com','email.email.com','email@example@email.com','.email@email.com','email@111.222.333.44444','”():;<>@email.com','email@email…com','email”not”correct@email.com']
email_negative = ['emailtextaddress','@#@@##@%^%#$@#$@#.com']
# email_positive = ['email@email.com','email.first.middle.lastname@email.com','email@subdomain.email.com','email@234.234.234.234','“email”@email.com','0987654321@email.com','email@email-one.com','email@email.co.jp','email+firstname+lastname@email.com']
email_positive = ['email@email.com','email.first.middle.lastname@email.com']
stream_negative = ['']
stream_positive = ['Design']
state_negative = ['']
state_positive = ['Delhi']
city_negative = ['']
city_positive = ['Delhi']
level_negative = ['']
level_positive = ['UG']


class commonfunctions:
    
            
    def happyflow(self):

        random_names = random_namee()
        randomnumber = random_phonenumber()
        random_emails = random_email()

        time.sleep(3)
        City_value, State_value, Stream_value = None, None, None

        try:
            time.sleep(2)
            footer_name = self.driver.find_element(By.ID, "id_name_cta")
        except:
            try:
                time.sleep(2)
                footer_name = self.driver.find_element(By.XPATH, "//input[@id='id_name']")
            except:
                pass
  
        footer_name.clear()
        time.sleep(1)
        footer_name.send_keys(random_names)
        self.logger.info(random_names)

        try:
            continue_button = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Continue'])[1]")
            continue_button.click()
        except:
            pass

        try:
           time.sleep(2)
           footer_email = self.driver.find_element(By.ID, "id_email_cta") 
        except:
            try:
                time.sleep(2)
                footer_email = self.driver.find_element(By.XPATH,"//input[@id='id_email']")
            except:
                pass

        footer_email.clear()
        time.sleep(1)
        footer_email.send_keys(random_emails)
        self.logger.info(random_emails)

        try:
            continue_button = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Continue'])[1]")
            continue_button.click()
        except:
            pass

        try:
           time.sleep(2)
           footer_mobile = self.driver.find_element(By.ID, "id_phone_cta")
        except:
            try:
                time.sleep(2)
                footer_mobile = self.driver.find_element(By.XPATH, "//input[@id='id_phone']")
            except:
                pass

        footer_mobile.clear()
        time.sleep(1)
        footer_mobile.send_keys(randomnumber)
        self.logger.info(randomnumber)

        try:
            continue_button = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Continue'])[1]")
            continue_button.click()
        except:
            pass
        
        try:
            time.sleep(2)
            footer_stream = Select(self.driver.find_element(By.ID, "id_stream_cta"))
            footer_stream.select_by_index(1)
            Stream = footer_stream.first_selected_option
            Stream_value = Stream.text
            self.logger.info("Stream : " + Stream_value)
        except:
            try:
                time.sleep(2)
                footer_stream = Select(self.driver.find_element(By.XPATH, "//select[@id='id_stream']"))
                footer_stream.select_by_index(1)
                Stream = footer_stream.first_selected_option
                Stream_value = Stream.text
                self.logger.info("Stream : " + Stream_value)
            except:
                pass
        
        try:
            continue_button = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Continue'])[1]")
            continue_button.click()
        except:
            pass

        try:
            footer_state = Select(self.driver.find_element(By.ID,"id_state_cta"))
            footer_state.select_by_index(1)
            state = footer_state.first_selected_option
            State_value = state.text
            self.logger.info("State : " + State_value)
        except:
            try:
                footer_state = Select(self.driver.find_element(By.XPATH, "//select[@id='id_state']"))
                footer_state.select_by_index(1)
                state = footer_state.first_selected_option
                State_value = state.text
                self.logger.info("State : " + State_value)
            except:
                pass

        try:
            continue_button = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Continue'])[1]")
            continue_button.click()
        except:
            pass
        
        
        try:
            footer_city = Select(self.driver.find_element(By.ID,"id_city"))
            footer_city.select_by_index(1)
            city = footer_city.first_selected_option
            City_value = city.text
            self.logger.info("City : " + City_value)
           
        except:
            pass
        
        try:
            continue_button = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Continue'])[1]")
            continue_button.click()
        except:
            pass

        try:
            time.sleep(2)
            footer_level = Select(self.driver.find_element(By.ID, "id_pref_level_cta"))
            time.sleep(1)
            footer_level.select_by_index(1)
            level=footer_level.first_selected_option
            Level_value = level.text
            self.logger.info("Level : " + Level_value)
        except:
            try:
                time.sleep(2)
                footer_level = Select(self.driver.find_element(By.XPATH,"//select[@id='id_pref_level']"))
                time.sleep(1)
                footer_level.select_by_index(1)
                level=footer_level.first_selected_option
                Level_value = level.text
                self.logger.info("Level : " + Level_value)
            except:
                pass

        try:
            continue_button = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Continue'])[1]")
            continue_button.click()
        except:
            pass
        
        try:
            footer_submitbutton = self.driver.find_element(By.ID,"id_submit_cta")
            time.sleep(2)
            Submit_Text= footer_submitbutton.text
            self.logger.info("CTA Text : " + Submit_Text)
            time.sleep(2)
            footer_submitbutton.click()
        except:
            try:
                footer_submitbutton = self.driver.find_element(By.XPATH,"//input[@id='id_submit']")
                time.sleep(2)
                Submit_Text= footer_submitbutton.text
                self.logger.info( "CTA Text : " + Submit_Text)
                time.sleep(2)
                footer_submitbutton.click()
                time.sleep(5)
            except:
                footer_submitbutton = self.driver.find_element(By.ID,"id_cta_submit")
                time.sleep(2)
                Submit_Text= footer_submitbutton.text
                self.logger.info( "CTA Text : " + Submit_Text)
                time.sleep(2)
                footer_submitbutton.click()
                time.sleep(5)

        # OTP Connection
        # conn = mysql.connector.connect(host=cld_host_staging,database = cld_databasename_staging,user = cld_username_staging, password = cld_pass_staging)
        conn = mysql.connector.connect(host=cld_host_live, database=cld_databasename_live, user=cld_username_live, password=cld_pass_live)
        
        self.logger.info(conn)
        time.sleep(2)
        query = ("""select code,phone_no from users_otp where phone_no = {} order by id desc""").format(randomnumber)
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            self.logger.info("No OTP found for phone number {}".format(randomnumber))
            return  # or raise an exception, depending on your use case
        result_dict = list(row)
        self.logger.info(result_dict)

        # OTP Functionality

        try:
            for index, value in enumerate(result_dict):
                otp_1_new = self.driver.find_element(By.XPATH,
                                                        "(//input[@placeholder = '-'])[1]".format(int(index) + 1))
                otp_1_new.send_keys(value)
                time.sleep(7)

        except:
            try:
                for index, value in enumerate(result_dict):
                    time.sleep(2)
                    otp_1_new = self.driver.find_element(By.XPATH, "(//input[@placeholder = '-'])[1]".format(int(index) + 1))
                    otp_1_new.send_keys(value)
                    time.sleep(7)
            except:
                pass

        self.logger.info("Otp added successfully")
        time.sleep(4)

        # Clicking on verify button
        try:
            verify_button = self.driver.find_element(By.XPATH, "//input[@id='gtm_loginVerify']")
            verify_button.click()
            time.sleep(5)
        except:
            try:
                verify_proceed_button = self.driver.find_element(By.XPATH, "//button[@id='gtm_loginVerify']")
                verify_proceed_button.click()
                time.sleep(5)
            except:
                pass
        #followup form
        try:
            thankyou_form = self.driver.find_element(By.XPATH, "(//*[name()='svg'][@class='CollegedekhoNavBar_closeArrow__U0hxp'])[1]")
            thankyou_form.click()
            time.sleep(5)
        except:
            try:
                close_callback = self.driver.find_element(By.XPATH, "//div[@class='userProfileLandingPage_closeIconBox__SD4gf']")
                close_callback.click()
        
            except:
                pass

        return random_names, random_emails, randomnumber, Stream_value, State_value, City_value
