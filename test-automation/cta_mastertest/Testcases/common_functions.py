import time
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import mysql.connector
from dotenv import load_dotenv
import os
from dotenv import load_dotenv
import os
from selenium.webdriver.common.keys import Keys

load_dotenv()

cld_host_live = os.getenv("cld_host_live")
cld_username_live = os.getenv("cld_username_live")
cld_pass_live = os.getenv("cld_pass_live")
cld_databasename_live = os.getenv("cld_databasename_live")

cld_host_staging = os.getenv("cld_host_staging")
cld_username_staging = os.getenv("cld_username_staging")
cld_pass_staging = os.getenv("cld_pass_staging")
cld_databasename_staging = os.getenv("cld_databasename_staging")

lms_host_live = os.getenv("lms_host_live")
lms_username_live = os.getenv("lms_username_live")
lms_pass_live = os.getenv("lms_pass_live")
lms_databasename_live = os.getenv("lms_databasename_live")

lms_host_staging = os.getenv("lms_host_staging")
lms_username_staging = os.getenv("lms_username_staging")
lms_pass_staging = os.getenv("lms_pass_staging")
lms_databasename_staging = os.getenv("lms_databasename_staging")

sso_host_live = os.getenv("sso_host_live")
sso_username_live = os.getenv("sso_username_live")
sso_pass_live = os.getenv("lms_sso_live")
sso_databasename_live = os.getenv("sso_databasename_live")

sso_host_staging = os.getenv("sso_host_staging")
sso_username_staging = os.getenv("sso_username_staging")
sso_pass_staging = os.getenv("sso_pass_staging")
sso_databasename_staging = os.getenv("sso_databasename_staging")

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
    
    def name_negative(self):
        self.logger.info("*******Name Negative Test Case*******")
        try:
            time.sleep(2)
            footer_name = self.driver.find_element(By.ID, "id_name_cta")
        except:
            try:
                time.sleep(2)
                footer_name = self.driver.find_element(By.XPATH, "//input[@id='id_name']")
            except:
                pass

        for negative_names in name_negative:

            self.driver.execute_script("arguments[0].value='';", footer_name)

            
            time.sleep(2)
            footer_name.send_keys(negative_names)
            time.sleep(1)
            try:
                name_gtm = footer_name.get_attribute('class')
                self.logger.info("GTM : " + name_gtm)
            except:
                pass
            time.sleep(2)
            try:
                footer_submitbutton = self.driver.find_element(By.ID,"id_submit_cta")
            except:
                try:
                    footer_submitbutton = self.driver.find_element(By.ID,"id_cta_submit")
                except:
                    footer_submitbutton = self.driver.find_element(By.XPATH,"//input[@id='id_submit']")
            time.sleep(5)
            action = ActionChains(self.driver)
            action.double_click(footer_submitbutton).perform()
            time.sleep(5)
            try:
                try:
                    error_text = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div[1]/div/form/div[1]/p")
                    if error_text.text == 'Enter a valid name':
                        self.logger.info(negative_names + ' ' + "Test Pass")
                except:
                    error_text = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/div[2]/form/ul/div[1]/li/p")
                    if error_text.text == ' Please enter a valid name':
                        self.logger.info(negative_names + ' ' + "Test Pass")                    
            except NoSuchElementException as e:
                self.logger.info(negative_names +' - ' + "Test Fail")
            time.sleep(1)

            footer_name.clear()
            time.sleep(2)
        footer_name.clear()
        time.sleep(2)

    def name_positive(self):
        self.logger.info("*******Name Postive Test Case*******")
        try:
            time.sleep(2)
            footer_name = self.driver.find_element(By.ID, "id_name_cta")
        except:
            try:
                time.sleep(2)
                footer_name = self.driver.find_element(By.XPATH, "//input[@id='id_name']")
            except:
                pass

        for positive_names in name_positive:
            footer_name.send_keys(positive_names)
            time.sleep(1)
            try:
                footer_submitbutton = self.driver.find_element(By.ID,"id_submit_cta")
            except:
                try:
                    footer_submitbutton = self.driver.find_element(By.ID,"id_cta_submit")
                except:
                    footer_submitbutton = self.driver.find_element(By.XPATH,"//input[@id='id_submit']")
            time.sleep(2)
            action = ActionChains(self.driver)
            action.double_click(footer_submitbutton).perform()
            time.sleep(1)
            error_name = None
            try:
                error_name = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div[1]/div/form/div[1]/p")
            except:
                try:
                    error_name = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/div[2]/form/ul/div[1]/li/p")
                except:
                    pass

            if error_name is None:
                self.logger.info(positive_names + ' Test Pass')
            else:
                self.logger.info(error_name.text + ' - ' + positive_names + ' Test Fail')
            footer_name.clear()
            time.sleep(2)
        footer_name.clear()
        time.sleep(2)

    def mobile_negative(self):
        self.logger.info("*******Mobile Negative Test Case*******")
        try:
           time.sleep(2)
           footer_mobile = self.driver.find_element(By.ID, "id_phone_cta")
        except:
            try:
                time.sleep(2)
                footer_mobile = self.driver.find_element(By.XPATH, "//input[@id='id_phone']")
            except:
                pass
        
        for negative_phone in phone_negative:
            footer_mobile.send_keys(negative_phone)
            time.sleep(1)
            try:
                footer_submitbutton = self.driver.find_element(By.ID,"id_submit_cta")
            except:
                try:
                    footer_submitbutton = self.driver.find_element(By.ID,"id_cta_submit")
                except:
                    footer_submitbutton = self.driver.find_element(By.XPATH,"//input[@id='id_submit']")
            time.sleep(1)
            action = ActionChains(self.driver)
            action.double_click(footer_submitbutton).perform()
            time.sleep(1)
            try:
                try:
                    valid_phone = self.driver.find_element(By.XPATH,"//input[@id='id_phone_cta']")
                    valid_message = valid_phone.get_attribute("validationMessage")
                    
                    if valid_message and valid_message == "Please match the format requested.":
                        self.logger.info(negative_phone + ' ' + "Test Pass") 
                    else:
                        self.logger.info("Test Fail")
            
                except:
                    valid_phone = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/div[2]/form/ul/div[2]/li/div/div[2]/p")
                    if valid_phone.text == 'Phone number should start with 6,7,8,9':
                        self.logger.info(negative_phone + ' ' + "Test Pass")
                
            except NoSuchElementException as e:
                self.logger.info(negative_phone + ' ' + "Test Fail")
            
            time.sleep(1)

            footer_mobile.clear()
            time.sleep(2)
        footer_mobile.clear()
        time.sleep(2)

    def mobile_positive(self):
        self.logger.info("*******Mobile Positive Test Case*******")
        try:
           time.sleep(2)
           footer_mobile = self.driver.find_element(By.ID, "id_phone_cta")
        except:
            try:
                time.sleep(2)
                footer_mobile = self.driver.find_element(By.XPATH, "//input[@id='id_phone']")
            except:
                pass

        for positive_phone in phone_positive:
            footer_mobile.send_keys(positive_phone)
            time.sleep(1)
            try:
                footer_submitbutton = self.driver.find_element(By.ID,"id_submit_cta")
            except:
                try:
                    footer_submitbutton = self.driver.find_element(By.ID,"id_cta_submit")
                except:
                    footer_submitbutton = self.driver.find_element(By.XPATH,"//input[@id='id_submit']")
            time.sleep(1)
            action = ActionChains(self.driver)
            action.double_click(footer_submitbutton).perform()
            time.sleep(1)
            try:
                valid_phone = self.driver.find_element(By.XPATH,"//input[@id='id_phone_cta']")
                valid_message = valid_phone.get_attribute("validationMessage")
            except:
                valid_phone = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/div[2]/form/ul/div[1]/li/p")
                valid_message = valid_phone.text
                         
            if valid_message:
                self.logger.info(positive_phone + ' ' + "Test Fail")
            else:
                self.logger.info(positive_phone + ' ' + "Test Pass")

            footer_mobile.clear()
            time.sleep(2)
        footer_mobile.clear()
        time.sleep(2)

    def email_negative(self):
        self.logger.info("*******Email Negative Test Case*******")
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
                footer_email = self.driver.find_element(By.ID,"id_email")
            except:
                pass

        for negative_email in email_negative:
            footer_email.send_keys(negative_email)
            time.sleep(1)
            try:
                footer_submitbutton = self.driver.find_element(By.ID,"id_submit_cta")
            except:
                try:
                    footer_submitbutton = self.driver.find_element(By.ID,"id_cta_submit")
                except:
                    footer_submitbutton = self.driver.find_element(By.XPATH,"//input[@id='id_submit']")
            time.sleep(1)
            action = ActionChains(self.driver)
            action.double_click(footer_submitbutton).perform()
            time.sleep(1)
            try:
                try:
                    valid_email = self.driver.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div[1]/div/form/div[2]/p")
                    if valid_email.text == "Enter a valid email":
                        self.logger.info(negative_email + ' ' + "Test Pass")
                except: 
                    valid_email = self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div[3]/div/div/div[2]/form/ul/div[3]/li/p")
                    if valid_email.text == "Please enter a valid email":
                        self.logger.info(negative_email + ' ' + "Test Pass")
                    
            except NoSuchElementException as e:
                self.logger.info("Negative Email Test Fail")
   
            time.sleep(2)
            footer_email.clear()
        time.sleep(2)
        footer_email.clear()    

    def email_positive(self):
        self.logger.info("*******Email Positive Test Case*******")
        try:
           time.sleep(2)
           footer_email = self.driver.find_element(By.ID, "id_email_cta") 
        except:
            try:
                time.sleep(2)
                footer_email = self.driver.find_element(By.XPATH,"//input[@id='id_email']")
            except:
                pass

        for positive_email in email_positive:
            footer_email.send_keys(positive_email)
            time.sleep(1)
            try:
                footer_submitbutton = self.driver.find_element(By.ID,"id_submit_cta")
            except:
                try:
                    footer_submitbutton = self.driver.find_element(By.ID,"id_cta_submit")
                except:
                    footer_submitbutton = self.driver.find_element(By.XPATH,"//input[@id='id_submit']")
            time.sleep(1)
            action = ActionChains(self.driver)
            action.double_click(footer_submitbutton).perform()
            time.sleep(1)
            error_email = None
            try:
                error_email = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div[1]/div/form/div[2]/p")
            except:
                try:
                    error_email = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/div[2]/form/ul/div[3]/li/p")
                except:
                    pass

            if error_email is None:
                self.logger.info(positive_email + ' Test Pass')
            else:
                self.logger.info(error_email.text + ' - ' + positive_email + ' Test Fail')

            time.sleep(2)

            footer_email.clear()
            time.sleep(2)
        footer_email.clear()
        time.sleep(2)


    def stream_negative(self):
        try:
            self.logger.info("*******Stream Negative Test Case*******")
            time.sleep(2)
            try:
                footer_submitbutton = self.driver.find_element(By.ID,"id_submit_cta")
                time.sleep(2)
                footer_submitbutton.click()
            except:
                try:
                    footer_submitbutton = self.driver.find_element(By.ID,"id_cta_submit")
                    time.sleep(2)
                    footer_submitbutton.click()
                except:
                    footer_submitbutton = self.driver.find_element(By.XPATH,"//input[@id='id_submit']")
                    time.sleep(2)
                    footer_submitbutton.click()
            
            try:
                try:
                    valid_stream = self.driver.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div[1]/div/form/div[4]/div/p")
                    if valid_stream.text == "Please Choose Preferred Stream":
                        self.logger.info(valid_stream.text + ' - ' + "Test Pass")
                except:
                    valid_stream = self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div[3]/div/div/div[2]/form/ul/div[4]/li/p")
                    if valid_stream.text == "Please select preferred stream":
                        self.logger.info(valid_stream.text + ' - ' + "Test Pass")
                
            except NoSuchElementException as e:
                self.logger.info("Stream Negatiive Test Fail")
        except:
            self.logger.info("No Stream Feild Available")

    def stream_positive(self):
        try:
            self.logger.info("*******Stream Positive Test Case*******")
            
            try:
                footer_stream = Select(self.driver.find_element(By.ID, "id_stream_cta"))
            except:
                try:
                    footer_stream = Select(self.driver.find_element(By.XPATH, "//select[@id='id_state']"))
                except:
                    pass

            for positive_stream in stream_positive:
                footer_stream.select_by_visible_text(positive_stream)
                time.sleep(1)
                try:
                    footer_submitbutton = self.driver.find_element(By.ID,"id_submit_cta")
                except:
                    try:
                        footer_submitbutton = self.driver.find_element(By.ID,"id_cta_submit")
                    except:
                        footer_submitbutton = self.driver.find_element(By.XPATH,"//input[@id='id_submit']")
                time.sleep(1)
                action = ActionChains(self.driver)
                action.double_click(footer_submitbutton).perform()
                time.sleep(1)

                error_stream = None
                try:
                    error_stream = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div[1]/div/form/div[4]/div/p")
                except:
                    try:
                        error_stream = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/div[2]/form/ul/div[4]/li/p")
                    except:
                        pass

                if error_stream is None:
                    self.logger.info(positive_stream + ' Test Pass')
                else:
                    self.logger.info(error_stream.text + ' - ' + positive_stream + ' Test Fail')

                time.sleep(2)
        except:
            self.logger.info("No Stream Feild Available")        


    def state_negative(self):
        try:
            self.logger.info("*******State Negative Test Case*******")
            time.sleep(2)
            try:
                footer_submitbutton = self.driver.find_element(By.ID,"id_submit_cta")
                time.sleep(2)
                footer_submitbutton.click()
            except:
                try:
                    footer_submitbutton = self.driver.find_element(By.ID,"id_cta_submit")
                    time.sleep(2)
                    footer_submitbutton.click()
                except:
                    footer_submitbutton = self.driver.find_element(By.XPATH,"//input[@id='id_submit']")
                    time.sleep(2)
                    footer_submitbutton.click()
            try:
                valid_state = self.driver.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div[1]/div/form/div[6]/div/p")
                if valid_state.text == "Please Choose State":
                    self.logger.info(valid_state.text + ' - ' +  "Test Pass") 
                
            except NoSuchElementException as e:
                error_state = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div[1]/div/form/div[6]/div/p")
                self.logger.info(error_state.text + ' - ' + "Test Fail")
                time.sleep(2)
        except:
            self.logger.info("No State Feild Available")

    def state_positive(self):
        try:
            self.logger.info("*******State Positive Test Case*******")
            try:
                footer_state = Select(self.driver.find_element(By.ID,"id_state_cta"))
            except:
                try:
                    footer_state = Select(self.driver.find_element(By.XPATH, "//select[@id='id_state']"))
                except:
                    pass

            for positive_state in state_positive:
                footer_state.select_by_index(1)
                time.sleep(1)
                try:
                    footer_submitbutton = self.driver.find_element(By.ID,"id_submit_cta")
                except:
                    try:
                        footer_submitbutton = self.driver.find_element(By.ID,"id_cta_submit")
                    except:
                        footer_submitbutton = self.driver.find_element(By.XPATH,"//input[@id='id_submit']")

                time.sleep(1)
                action = ActionChains(self.driver)
                action.double_click(footer_submitbutton).perform()
                time.sleep(1)

                error_state = None
                try:
                    error_state = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div[1]/div/form/div[6]/div/p")
                except:
                    pass

                if error_state is None:
                    self.logger.info(positive_state + ' Test Pass')
                else:
                    self.logger.info(error_state.text + ' - ' + positive_state + ' Test Fail')

                time.sleep(2)
        except:
            self.logger.info("No State Feild Available")    

    def level_negative(self):
        try:
            self.logger.info("*******Level Negative Test Case*******")
            try:
                footer_submitbutton = self.driver.find_element(By.ID,"id_submit_cta")
                time.sleep(2)
                footer_submitbutton.click()
            except:
                try:
                    footer_submitbutton = self.driver.find_element(By.ID,"id_cta_submit")
                    time.sleep(2)
                    footer_submitbutton.click()
                except:
                    footer_submitbutton = self.driver.find_element(By.XPATH,"//input[@id='id_submit']")
                    time.sleep(2)
                    footer_submitbutton.click()

            try:
                try:
                    valid_level = self.driver.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div[1]/div/form/div[5]/div/p")
                    time.sleep(1)
                    if valid_level.text == "Please Choose Preferred Level":
                        self.logger.info('Level '+ ' - '+ valid_level.text + ' - ' + "Test Pass")
                except:
                    valid_level = self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div[3]/div/div/div[2]/form/ul/div[5]/li/p")
                    time.sleep(1)
                    if valid_level.text == "Please select preferred level":
                        self.logger.info('Level '+ ' - '+ valid_level.text + ' - ' + "Test Pass")
            except NoSuchElementException as e:
                self.logger.info(" Level Negative Test Fail")
                time.sleep(2)
        except:
            self.logger.info("No Level Feild Available")

    def level_positive(self): 
        try:
            self.logger.info("*******Level Positive Test Case*******")
            try:
                time.sleep(2)
                footer_level = Select(self.driver.find_element(By.ID, "id_pref_level_cta"))
                time.sleep(1)
            except:
                try:
                    time.sleep(2)
                    footer_level = Select(self.driver.find_element(By.XPATH,"//select[@id='id_pref_level']"))
                    time.sleep(1)
                except:
                    pass

            for positive_level in level_positive:
                footer_level.select_by_index(1)
                time.sleep(1)
                try:
                    footer_submitbutton = self.driver.find_element(By.ID,"id_submit_cta")
                except:
                    try:
                        footer_submitbutton = self.driver.find_element(By.ID,"id_cta_submit")
                    except:
                        footer_submitbutton = self.driver.find_element(By.XPATH,"//input[@id='id_submit']")
                time.sleep(1)
                action = ActionChains(self.driver)
                action.double_click(footer_submitbutton).perform()
                time.sleep(1)

                error_level = None
                try:
                    error_level = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div[1]/div/form/div[5]/div/p")
                except:
                    try:
                        error_level = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/div[2]/form/ul/div[5]/li/p")
                    except:
                        pass

                if error_level is None:
                    self.logger.info(positive_level + ' Test Pass')
                else:
                    self.logger.info(error_level.text + ' - ' + positive_level + ' Test Fail')

                time.sleep(2)
        except:
            self.logger.info("No Level Feild Available")

        
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
            self.logger.info("Button Text : " + Submit_Text)
            time.sleep(2)
            footer_submitbutton.click()
        except:
            try:
                footer_submitbutton = self.driver.find_element(By.XPATH,"//input[@id='id_submit']")
                time.sleep(2)
                Submit_Text= footer_submitbutton.text
                self.logger.info( "Button Text : " + Submit_Text)
                time.sleep(2)
                footer_submitbutton.click()
                time.sleep(5)
            except:
                footer_submitbutton = self.driver.find_element(By.ID,"id_cta_submit")
                time.sleep(2)
                Submit_Text= footer_submitbutton.text
                self.logger.info( "Button Text : " + Submit_Text)
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

    def footerform(self):

        random_names = random_namee()
        randomnumber = random_phonenumber()
        random_emails = random_email()

        time.sleep(3)
        City_value, State_value, Stream_value, Level_value = None, None, None, None

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
            # self.logger.info("Button Text : " + Submit_Text)
            time.sleep(2)
            footer_submitbutton.click()
        except:
            try:
                footer_submitbutton = self.driver.find_element(By.XPATH,"//input[@id='id_submit']")
                time.sleep(2)
                Submit_Text= footer_submitbutton.text
                # self.logger.info( "Button Text : " + Submit_Text)
                time.sleep(2)
                footer_submitbutton.click()
                time.sleep(5)
            except:
                footer_submitbutton = self.driver.find_element(By.ID,"id_cta_submit")
                time.sleep(2)
                Submit_Text= footer_submitbutton.text
                # self.logger.info( "Button Text : " + Submit_Text)
                time.sleep(2)
                footer_submitbutton.click()
                time.sleep(5)

        return random_names, random_emails, randomnumber, Stream_value, Level_value

    def newsubscribe(self):

        Level_value, State_value, Stream_value = None, None, None

        time.sleep(2)
        footer_name = self.driver.find_element(By.ID, "id_name_news_subscribe")
        footer_name.clear()
        time.sleep(1)
        footer_name.send_keys(random_names)
        self.logger.info(random_names)

        time.sleep(2)
        footer_email = self.driver.find_element(By.ID, "id_email_news_subscribe") 
        footer_email.clear()
        time.sleep(1)
        footer_email.send_keys(random_emails)
        self.logger.info(random_emails)

        time.sleep(2)
        footer_mobile = self.driver.find_element(By.ID, "id_phone_news_subscribe")
        footer_mobile.clear()
        time.sleep(1)
        footer_mobile.send_keys(randomnumber)
        self.logger.info(randomnumber)

        self.driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(2)

        try:
            time.sleep(2)
            footer_stream = Select(self.driver.find_element(By.ID, "id_stream_news_subscribe"))
            footer_stream.select_by_index(1)
            Stream = footer_stream.first_selected_option
            Stream_value = Stream.text
            self.logger.info("Stream : " + Stream_value)
        except:
            pass
        
        try:
            footer_state = Select(self.driver.find_element(By.ID,"id_state_news_subscribe"))
            footer_state.select_by_index(1)
            state = footer_state.first_selected_option
            State_value = state.text
            self.logger.info("State : " + State_value)
        except:
            pass

        try:
            footer_level = Select(self.driver.find_element(By.ID,"id_pref_level_news_subscribe"))
            footer_level.select_by_index(1)
            level = footer_state.first_selected_option
            Level_value = level.text
            self.logger.info("State : " + Level_value)
        except:
            pass
        
        footer_submitbutton = self.driver.find_element(By.ID,"id_submit_news_subscribe")
        time.sleep(2)
        footer_submitbutton.click()

        return random_names, random_emails, randomnumber, Stream_value, State_value
    
    def du_college_predictor(self):

        State_value, Stream_value = None, None

        time.sleep(2)
        footer_name = self.driver.find_element(By.XPATH, "//input[@id='univ_id_name']")
        footer_name.clear()
        time.sleep(1)
        footer_name.send_keys(random_names)
        self.logger.info(random_names)

        time.sleep(2)
        footer_email = self.driver.find_element(By.XPATH, "//input[@id='univ_id_email']") 
        footer_email.clear()
        time.sleep(1)
        footer_email.send_keys(random_emails)
        self.logger.info(random_emails)

        time.sleep(2)
        footer_mobile = self.driver.find_element(By.XPATH, "//input[@id='univ_id_phone']")
        footer_mobile.clear()
        time.sleep(1)
        footer_mobile.send_keys(randomnumber)
        self.logger.info(randomnumber)

        time.sleep(2)
        footer_courses = self.driver.find_element(By.XPATH, "//input[@placeholder='Select Courses']")
        footer_courses.click()
        footer_courses.send_keys("B.Com in Commerce (Commerce & Banking)")
        footer_courses.send_keys(Keys.DOWN)
        time.sleep(2)
        footer_courses.send_keys(Keys.ENTER)
        time.sleep(2)       
        
        time.sleep(2)
        footer_colleges = self.driver.find_element(By.XPATH, "//input[@placeholder='Select Colleges']")
        footer_colleges.click()
        footer_colleges.send_keys("Aditi Mahavidyalaya")
        footer_colleges.send_keys(Keys.DOWN)
        time.sleep(2)
        footer_colleges.send_keys(Keys.ENTER)
        time.sleep(2) 
        
        time.sleep(2)
        footer_submitbutton = self.driver.find_element(By.XPATH,"//button[@id='du-eligibility-next']")
        time.sleep(2)
        footer_submitbutton.click()

        return random_names, random_emails, randomnumber, Stream_value, State_value
    

    def select_options(self):

        result = {}
    
        for i in range(4):
            
            time.sleep(2)
            questions = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/ul[1]/li[{}]/p[1]".format(i+1))
            
            radio_point = []
            answer = []
            radio_point_1 = self.driver.find_element(By.XPATH,"(//input[@id='0'])[{}]".format(i+1))
            radio_point_2 = self.driver.find_element(By.XPATH,"(//input[@id='1'])[{}]".format(i+1))
            radio_point_3 = self.driver.find_element(By.XPATH,"(//input[@id='2'])[{}]".format(i+1))
            radio_point.append(radio_point_1)
            radio_point.append(radio_point_2)
            radio_point.append(radio_point_3)

            answer_1 = self.driver.find_element(By.XPATH,"(//span[contains(text(),'Never')])[1]").text
            answer_2 = self.driver.find_element(By.XPATH,"(//span[contains(text(),'Sometimes')])[1]").text
            answer_3 = self.driver.find_element(By.XPATH,"(//span[contains(text(),'Always')])[1]").text
            questions_text = questions.text.split(".", 1)[1].strip()

            
            answer.append(answer_1)
            answer.append(answer_2)
            answer.append(answer_3)
            
            time.sleep(1)

            var = random.randint(0,2)
            random_radio_button = radio_point[var]      
            random_radio_button.click()
            answer = answer[var]
            result[questions_text] = var
                
    def optionselect(self):

        button_id = 0

        for button_id in range(15):

            self.select_options()        
            
            self.driver.execute_script("window.scrollTo(0, 100)") 
            time.sleep(2)
            try:
                
                next_button = self.driver.find_element(By.XPATH,"//button[normalize-space()='Next']")
                time.sleep(1)
                next_button.click()
                time.sleep(1)
            
            except:
                pass

            try:
                submit_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
                time.sleep(1)
                submit_button.click()
                time.sleep(2)
                # time.sleep(2)
                # login_button = self.driver.find_element(By.XPATH,"//a[normalize-space()='Login']")
                # time.sleep(1)
                # login_button.click()
                # time.sleep(1)
                # username = self.driver.find_element(By.ID,"id_email_cta")
                # username.send_keys("praveen.yadav@gmail.com")
                # time.sleep(1)
                # userpass = self.driver.find_element(By.ID,"id_password_cta")
                # userpass.send_keys("praveen990589")
                # submit = self.driver.find_element(By.ID,"gtm_login")
                # submit.click()
                # time.sleep(1)
            except:
                pass
        
            button_id += 1
            
    def sign_up(self):

        State_value, Stream_value = None, None

        time.sleep(2)
        footer_name = self.driver.find_element(By.ID, "id_name_signup")
        footer_name.clear()
        time.sleep(1)
        footer_name.send_keys(random_names)
        self.logger.info(random_names)

        time.sleep(2)
        footer_email = self.driver.find_element(By.ID, "id_email_signup") 
        footer_email.clear()
        time.sleep(1)
        footer_email.send_keys(random_emails)
        self.logger.info(random_emails)

        time.sleep(2)
        footer_mobile = self.driver.find_element(By.ID, "id_phone_signup")
        footer_mobile.clear()
        time.sleep(1)
        footer_mobile.send_keys(randomnumber)
        self.logger.info(randomnumber)

        try:
            time.sleep(2)
            footer_stream = Select(self.driver.find_element(By.ID, "id_preferred_stream_signup"))
            footer_stream.select_by_index(1)
            Stream = footer_stream.first_selected_option
            Stream_value = Stream.text
            self.logger.info("Stream : " + Stream_value)
        except:
            pass
        
        try:
            footer_level = Select(self.driver.find_element(By.ID,"id_preferred_level_signup"))
            footer_level.select_by_index(1)
            level=footer_level.first_selected_option
            Level_value = level.text
            self.logger.info("Level : " + Level_value)
        except:
            pass

        time.sleep(2)
        footer_password = self.driver.find_element(By.ID, "password_signup")
        footer_password.clear()
        time.sleep(1)
        footer_password.send_keys(random_password)
        self.logger.info(random_password)
        
        footer_submitbutton = self.driver.find_element(By.ID,"gtm_signup")
        time.sleep(2)
        footer_submitbutton.click()

        try:

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
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
            time.sleep(2)
            profile_click = self.driver.find_element(By.XPATH,"(//img[@alt='profile image'])[1]")
            profile_click.click()
            self.driver.execute_script("window.scrollBy(0,100)","")
            time.sleep(2)
            logout_click=self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']")
            logout_click.click()
            time.sleep(5)
            
            
        except:
            pass

        return random_names, random_emails, randomnumber, Stream_value, State_value
            
    def exam_predictor(self):

        random_names = random_namee()
        randomnumber = random_phonenumber()
        random_emails = random_email()

        State_value, Stream_value = None, None

        try:
            time.sleep(2)
            footer_name = self.driver.find_element(By.ID, "id_name_college_predictor")
            footer_name.clear()
            time.sleep(1)
            footer_name.send_keys(random_names)
            self.logger.info(random_names)
        except:
            time.sleep(2)
            footer_name = self.driver.find_element(By.ID, "id_name_rank_predictor")
            footer_name.clear()
            time.sleep(1)
            footer_name.send_keys(random_names)
            self.logger.info(random_names)

        try:
            time.sleep(2)
            footer_email = self.driver.find_element(By.ID, "id_email_college_predictor") 
            footer_email.clear()
            time.sleep(1)
            footer_email.send_keys(random_emails)
            self.logger.info(random_emails)
        except:
            time.sleep(2)
            footer_email = self.driver.find_element(By.ID, "id_email_rank_predictor") 
            footer_email.clear()
            time.sleep(1)
            footer_email.send_keys(random_emails)
            self.logger.info(random_emails)

        try:
            time.sleep(2)
            footer_mobile = self.driver.find_element(By.ID, "id_phone_college_predictor")
            footer_mobile.clear()
            time.sleep(1)
            footer_mobile.send_keys(randomnumber)
            self.logger.info(randomnumber)
        except:
            time.sleep(2)
            footer_mobile = self.driver.find_element(By.ID, "id_phone_rank_predictor")
            footer_mobile.clear()
            time.sleep(1)
            footer_mobile.send_keys(randomnumber)
            self.logger.info(randomnumber)

        try:
            time.sleep(2)
            footer_stream = Select(self.driver.find_element(By.ID, "id_state_college_predictor"))
            footer_stream.select_by_index(1)
            Stream = footer_stream.first_selected_option
            Stream_value = Stream.text
            self.logger.info("Stream : " + Stream_value)
        except:
            try:
                time.sleep(2)
                footer_stream = Select(self.driver.find_element(By.ID, "id_state_rank_predictor"))
                footer_stream.select_by_index(1)
                Stream = footer_stream.first_selected_option
                Stream_value = Stream.text
                self.logger.info("Stream : " + Stream_value)
            except:
                pass    

        time.sleep(2)
        footer_submitbutton = self.driver.find_element(By.ID,"marks-enter")
        time.sleep(2)
        footer_submitbutton.click()

        return random_names, random_emails, randomnumber, Stream_value, State_value
    


