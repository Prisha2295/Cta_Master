import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

name_negative = [' ','123','name@','  1name','@1name','name.com','.name']
name_positive = ['name','  name name','NAME','NaMe','Name nAmE']
phone_negative = ['5604403033','@@@@^&@^@&', 'name name ', 'name123', 'name@123.com', '0123456789']
phone_postive = ['6543210987','7383948473','8789012345','9012345678']
email_negative = ['emailtextaddress','@#@@##@%^%#$@#$@#.com','@email.com','email.email.com','email@example@email.com','.email@email.com','email@111.222.333.44444','”(),:;<>[\]@email.com','email@email…com','email”not”correct@email.com']
email_positive = ['email@email.com','email.first.middle.lastname@email.com','email@subdomain.email.com','email@234.234.234.234','“email”@email.com','0987654321@email.com','email@email-one.com','email@email.co.jp','email+firstname+lastname@email.com']
stream_negative = ['']
stream_positive = ['Design']
state_negative = ['']
state_positive = ['Delhi']
city_negative = ['']
city_positive = ['Delhi']


class commonfunctions():
    
    
    def test_name_negative(self,driver):
        self.logger.info("*******Name Negative Test Case*******")
        for negative_names in name_negative:
            footer_name = self.driver.find_element(By.ID, 'name') or self.driver.find_element(By.NAME, 'name')
            footer_name.send_keys(negative_names)
            time.sleep(1)
            footer_submitbutton = driver.find_element(By.NAME, 'submit')
            time.sleep(1)
            action = ActionChains(driver)
            action.double_click(footer_submitbutton)
            time.sleep(1)
            try:
                error_text = driver.find_element(By.XPATH, "(//label[normalize-space()='Enter a Valid Name'])[1]")
                if error_text.text == 'Enter a Valid Name':
                    self.logger.info(error_text.text + ' - ' + negative_names + ' ' + "Test Pass")
            except NoSuchElementException as e:
                error_text_name = driver.find_element(By.XPATH,"(//label[normalize-space()='Name'])[1]")
                self.logger.info(error_text_name.text +' - ' + negative_names +' - ' + "Test Fail")
            time.sleep(1)

            footer_name.clear()
            time.sleep(2)

    def test_name_positive(self,driver):
        self.logger.info("*******Name Postive Test Case*******")
        footer_name = self.driver.find_element(By.ID, 'name') or self.driver.find_element(By.NAME, 'name')
        for positive_names in name_positive:
            footer_name.send_keys(positive_names)
            time.sleep(1)
            footer_submitbutton = driver.find_element(By.NAME, 'submit')
            time.sleep(1)
            action = ActionChains(driver)
            action.double_click(footer_submitbutton)
            time.sleep(1)
            try:
                valid_text_name = driver.find_element(By.XPATH,"(//label[normalize-space()='Name'])[1]")
                if valid_text_name.text == "Name":
                   self.logger.info(valid_text_name.text + ' - ' + positive_names + ' ' + "Test Pass") 
                
            except NoSuchElementException as e:
                error_message = driver.find_element(By.XPATH, "(//label[normalize-space()='Enter a Valid Name'])[1]")
                self.logger.info(error_message.text + ' - ' + positive_names + ' ' + "Test Fail")
            
            time.sleep(1)

            footer_name.clear()
            time.sleep(2)

    def test_mobile_negative(self,driver):
        self.logger.info("*******Mobile Negative Test Case*******")
        footer_mobile = self.driver.find_element(By.ID,'phone') or self.driver.find_element(By.NAME,'phone')
        for negative_phone in phone_negative:
            footer_mobile.send_keys(negative_phone)
            time.sleep(1)
            footer_submitbutton = driver.find_element(By.NAME, 'submit')
            time.sleep(1)
            action = ActionChains(driver)
            action.double_click(footer_submitbutton)
            time.sleep(1)
            try:
                valid_phone = driver.find_element(By.XPATH,"(//label[normalize-space()='Mobile starts with 6,7,8,9'])[1]")
                if valid_phone.text == "Mobile starts with 6,7,8,9":
                   self.logger.info(valid_phone.text + ' - ' + negative_phone + ' ' + "Test Pass") 
                
            except NoSuchElementException as e:
                error_phone = driver.find_element(By.XPATH, "(//label[normalize-space()='Mobile'])[1]")
                self.logger.info(error_phone.text + ' - ' + negative_phone + ' ' + "Test Fail")
            
            time.sleep(1)

            footer_mobile.clear()
            time.sleep(2)
    def test_mobile_negative(self,driver):
        self.logger.info("*******Mobile Negative Test Case*******")
        footer_mobile = self.driver.find_element(By.ID,'phone') or self.driver.find_element(By.NAME,'phone')
        for negative_phone in phone_negative:
            footer_mobile.send_keys(negative_phone)
            time.sleep(1)
            footer_submitbutton = driver.find_element(By.NAME, 'submit')
            time.sleep(1)
            action = ActionChains(driver)
            action.double_click(footer_submitbutton)
            time.sleep(1)
            try:
                valid_phone = driver.find_element(By.XPATH,"(//label[normalize-space()='Mobile starts with 6,7,8,9'])[1]")
                if valid_phone.text == "Mobile starts with 6,7,8,9":
                   self.logger.info(valid_phone.text + ' - ' + negative_phone + ' ' + "Test Pass") 
                
            except NoSuchElementException as e:
                error_phone = driver.find_element(By.XPATH, "(//label[normalize-space()='Mobile'])[1]")
                self.logger.info(error_phone.text + ' - ' + negative_phone + ' ' + "Test Fail")
            
            time.sleep(1)

            footer_mobile.clear()
            time.sleep(2)


    def test_mobile_positive(self,driver):
        self.logger.info("*******Mobile Positive Test Case*******")
        footer_mobile = self.driver.find_element(By.ID,'phone') or self.driver.find_element(By.NAME,'phone')
        for positive_phone in phone_postive:
            footer_mobile.send_keys(positive_phone)
            time.sleep(1)
            footer_submitbutton = driver.find_element(By.NAME, 'submit')
            time.sleep(1)
            action = ActionChains(driver)
            action.double_click(footer_submitbutton)
            time.sleep(1)
            try:
                error_phone = driver.find_element(By.XPATH, "(//label[normalize-space()='Mobile'])[1]")
                self.logger.info(error_phone.text + ' - ' + positive_phone + ' ' + "Test Pass")
   
            except NoSuchElementException as e:
                valid_phone = driver.find_element(By.XPATH,"(//label[normalize-space()='Mobile starts with 6,7,8,9'])[1]")
                if valid_phone.text == "Mobile starts with 6,7,8,9":
                   self.logger.info(valid_phone.text + ' - ' + positive_phone + ' ' + "Test Fail") 
            
            time.sleep(1)

            footer_mobile.clear()
            time.sleep(2)

    def test_email_negative(self,driver):
        self.logger.info("*******Email Negative Test Case*******")
        footer_email = self.driver.find_element(By.ID,'email') or self.driver.find_element(By.Name,'email')
        for negative_email in email_negative:
            footer_email.send_keys(negative_email)
            time.sleep(1)
            footer_submitbutton = driver.find_element(By.NAME, 'submit')
            time.sleep(1)
            action = ActionChains(driver)
            action.double_click(footer_submitbutton)
            time.sleep(1)
            try:
                valid_email = driver.find_element(By.XPATH,"(//label[normalize-space()='Enter Your Email Address'])[1]")
                if valid_email.text == "Enter Your Email Address":
                   self.logger.info(valid_email.text + ' - ' + negative_email + ' ' + "Test Pass") 
                
            except NoSuchElementException as e:
                error_email = driver.find_element(By.XPATH, "(//label[normalize-space()='Email'])[1]")
                self.logger.info(error_email.text + ' - ' + negative_email + ' ' + "Test Fail")
   
                
            
            time.sleep(1)

            footer_email.clear()
            time.sleep(2)

    def test_email_positive(self,driver):
        self.logger.info("*******Email Positive Test Case*******")
        footer_email = self.driver.find_element(By.ID,'email') or self.driver.find_element(By.Name,'email')
        for positive_email in email_positive:
            footer_email.send_keys(positive_email)
            time.sleep(1)
            footer_submitbutton = driver.find_element(By.NAME, 'submit')
            time.sleep(1)
            action = ActionChains(driver)
            action.double_click(footer_submitbutton)
            time.sleep(1)
            try:
                error_email = driver.find_element(By.XPATH, "(//label[normalize-space()='Email'])[1]")
                self.logger.info(error_email.text + ' - ' + positive_email + ' ' + "Test Pass")
   
            except NoSuchElementException as e:
                valid_email = driver.find_element(By.XPATH,"(//label[normalize-space()='Enter Your Email Address'])[1]")
                if valid_email.text == "Mobile starts with 6,7,8,9":
                   self.logger.info(valid_email.text + ' - ' + positive_email + ' ' + "Test Fail") 
            
            time.sleep(1)

            footer_email.clear()
            time.sleep(2)


    def test_stream_negative(self,driver):
        self.logger.info("*******Stream Negative Test Case*******")
        try:
            time.sleep(1)
            footer_stream = Select(self.driver.find_element(By.NAME,'stream'))
            footer_stream.select_by_index(1)
            time.sleep(1)
            footer_submitbutton = driver.find_element(By.NAME, 'submit')
            time.sleep(1)
            footer_submitbutton.click()
            time.sleep(1)
            try:
                valid_stream = driver.find_element(By.XPATH,"(//div[@class='commonFooterForm_footerErrorMessage___ITjX'])[1]")
                if valid_stream.text == "Please choose your stream.":
                    self.logger.info('Stream '+ ' - '+ valid_stream.text + ' ' + "Test Pass") 
                
            except NoSuchElementException as e:
                error_stream = driver.find_element(By.XPATH, "(//div[@class='commonFooterForm_footerErrorMessage___ITjX'])[1]")
                self.logger.info(error_stream.text + ' - ' + "Test Fail")
        except:
            pass

        # for negative_stream in stream_negative:
            # footer_stream.select_by_visible_text(negative_stream)

        time.sleep(1)

       

    def test_stream_positive(self,driver):
        self.logger.info("*******Stream Positive Test Case*******")
        try:
            footer_stream = Select(self.driver.find_element(By.NAME,'stream'))
        except:
            pass

        for positive_stream in stream_positive:
            footer_stream.select_by_visible_text(positive_stream)
            time.sleep(1)
            footer_submitbutton = driver.find_element(By.NAME, 'submit')
            time.sleep(1)
            action = ActionChains(driver)
            action.double_click(footer_submitbutton)
            time.sleep(1)

            try:
                error_stream = driver.find_element(By.XPATH, "(//div[@class='commonFooterForm_footerErrorMessage___ITjX'])[1]")
                self.logger.info(error_stream.text + ' - ' + positive_stream + ' ' + "Test Pass")

            except NoSuchElementException as e:
                valid_stream = driver.find_element(By.XPATH,"(//div[@class='commonFooterForm_footerErrorMessage___ITjX'])[1]")
                if valid_stream.text == "Please choose your stream.":
                    self.logger.info(valid_stream.text + ' - ' + positive_stream + ' ' + "Test Fail") 
            
            time.sleep(1)

            footer_stream.clear()
            time.sleep(2)


    def test_state_negative(self,driver):
        self.logger.info("*******State Negative Test Case*******")
        try:
            footer_state = Select(self.driver.find_element(By.NAME,'state'))
        except:
            pass

        for negative_state in state_negative:
            footer_state.select_by_visible_text(negative_state)
            time.sleep(1)
            footer_submitbutton = driver.find_element(By.NAME, 'submit')
            time.sleep(1)
            action = ActionChains(driver)
            action.double_click(footer_submitbutton)
            time.sleep(1)
            try:
                valid_state = driver.find_element(By.XPATH,"(//div[@class='commonFooterForm_footerErrorMessage___ITjX'])[1]")
                if valid_state.text == "Please choose your state.":
                   self.logger.info(valid_state.text + ' - ' + negative_state + ' ' + "Test Pass") 
                
            except NoSuchElementException as e:
                error_state = driver.find_element(By.XPATH, "(//div[@class='commonFooterForm_footerErrorMessage___ITjX'])[1]")
                self.logger.info(error_state.text + ' - ' + negative_state + ' ' + "Test Fail")
   
            time.sleep(1)

            footer_state.clear()
            time.sleep(2)

    def test_state_positive(self,driver):
        self.logger.info("*******State Positive Test Case*******")
        try:
            footer_state = Select(self.driver.find_element(By.NAME,'state'))
        except:
            pass

        for positive_state in state_positive:
            footer_state.select_by_visible_text(positive_state)
            time.sleep(1)
            footer_submitbutton = driver.find_element(By.NAME, 'submit')
            time.sleep(1)
            action = ActionChains(driver)
            action.double_click(footer_submitbutton)
            time.sleep(1)

            try:
                error_state = driver.find_element(By.XPATH, "(//div[@class='commonFooterForm_footerErrorMessage___ITjX'])[1]")
                self.logger.info(error_state.text + ' - ' + positive_state + ' ' + "Test Pass")

            except NoSuchElementException as e:
                valid_state = driver.find_element(By.XPATH,"(//div[@class='commonFooterForm_footerErrorMessage___ITjX'])[1]")
                if valid_state.text == "Please choose your stream.":
                    self.logger.info(valid_state.text + ' - ' + positive_state + ' ' + "Test Fail") 
            
            time.sleep(1)

            footer_state.clear()
            time.sleep(2)

    
    def test_city_negative(self,driver):
        self.logger.info("*******City Negative Test Case*******")
        try:
            footer_city = Select(self.driver.find_element(By.NAME,'city'))
        except:
            pass

        for negative_city in city_negative:
            footer_city.select_by_visible_text(negative_city)
            time.sleep(1)
            footer_submitbutton = driver.find_element(By.NAME, 'submit')
            time.sleep(1)
            action = ActionChains(driver)
            action.double_click(footer_submitbutton)
            time.sleep(1)
            try:
                valid_city = driver.find_element(By.XPATH,"(//div[@class='commonFooterForm_footerErrorMessage___ITjX'])[1]")
                if valid_city.text == "Please choose your city.":
                   self.logger.info(valid_city.text + ' - ' + negative_city + ' ' + "Test Pass") 
                
            except NoSuchElementException as e:
                error_city = driver.find_element(By.XPATH, "(//div[@class='commonFooterForm_footerErrorMessage___ITjX'])[1]")
                self.logger.info(error_city.text + ' - ' + negative_city + ' ' + "Test Fail")
   
            time.sleep(1)

            footer_city.clear()
            time.sleep(2)

    def test_city_positive(self,driver):
        self.logger.info("*******City Positive Test Case*******")
        try:
            footer_city = Select(self.driver.find_element(By.NAME,'city'))
        except:
            pass

        for positive_city in city_positive:
            footer_city.select_by_visible_text(positive_city)
            time.sleep(1)
            footer_submitbutton = driver.find_element(By.NAME, 'submit')
            time.sleep(1)
            action = ActionChains(driver)
            action.double_click(footer_submitbutton)
            time.sleep(1)

            try:
                error_city = driver.find_element(By.XPATH, "(//div[@class='commonFooterForm_footerErrorMessage___ITjX'])[1]")
                self.logger.info(error_city.text + ' - ' + positive_city + ' ' + "Test Pass")

            except NoSuchElementException as e:
                valid_city = driver.find_element(By.XPATH,"(//div[@class='commonFooterForm_footerErrorMessage___ITjX'])[1]")
                if valid_city.text == "Please choose your city.":
                    self.logger.info(valid_city.text + ' - ' + positive_city + ' ' + "Test Fail") 
            
            time.sleep(1)

            footer_city.clear()
            time.sleep(2)

    time.sleep(5)

        
        
        
        
        
        
        
        

       

        
            
        
        


