import time
import random
import string
import mysql.connector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select




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
    
invalid_names = ['','8764876','@@name',"@@@@@","name"]

valid_names = ['name','  name name','NAME','NaMe','Name nAmE','name.com','.name']

invalid_phones = ["",'5604403033','@@@@^&@^@&']

valid_phones = ['6543210987','7383948473','8789012345','9012345678']

invalid_emails = ['emailtextaddress','@#@@##@%^%#$@#$@#.com']

valid_emails = ['email@email.com','email.first.middle.lastname@email.com']

invalid_city = ['']

valid_cities = ['Delhi']

invalid_level = ['']

valid_level = ['Studying/Completed Graduation']

invalid_course = [""]

valid_course = ["MBA in Data"]



class commonfunctions:
    
    def gmu_happyflow(self):
        self.logger.info("*******GMU Happy Flow*******")
        
        name_input = self.driver.find_element(By.ID, "formName")
        email_input = self.driver.find_element(By.ID, "formEmail")
        city_input = self.driver.find_element(By.ID, "select2-leadform-interested_location-container")
        course_input = self.driver.find_element(By.ID,"select2-interested_course_lead-container") 
        mobile_input = self.driver.find_element(By.ID,"formMobile")
        
        name_input.send_keys(random_names)
        self.logger.info(random_names)

        email_input.send_keys(random_emails)
        self.logger.info(random_emails)
        time.sleep(2)
        
        self.logger.info("Clicking on city dropdown")
        city_input.click()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "select2-search__field"))).send_keys(Keys.ENTER)
        time.sleep(2)
        
        self.logger.info("Clicking on course dropdown")
        course_input.click()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "select2-search__field"))).send_keys(Keys.ENTER)
        time.sleep(2)

        self.logger.info("Adding Phone Number")
        mobile_input.send_keys(randomnumber)
        self.logger.info(randomnumber)
        time.sleep(2)

        conn = mysql.connector.connect(host='10.0.140.123', database='getmyuni_v2_test', user='cld_ro', password='yA#9Yo$un3SEzK3F')
   
        self.logger.info(conn)
        
        query = ("""SELECT sto.otp 
                    FROM student AS st 
                    LEFT JOIN student_otp AS sto ON sto.student_id = st.id 
                    WHERE st.phone = {}""").format(randomnumber)
                            
        cursor = conn.cursor()
        
        cursor.execute(query)
        time.sleep(2)
        otp = cursor.fetchone()
        time.sleep(10)
        otp_list = list(otp)
        self.logger.info(otp_list)
        time.sleep(10)
        
        # Close the cursor and database connection
        cursor.close()
        conn.close()
        
        otp_input = None

        if otp_list[0] is not None:
            otp_input = self.driver.find_element(By.ID, "OTPField")
            time.sleep(0.5)
            otp_input.send_keys(otp_list[0])
        else:
            # Wait for the element to be present or until a timeout is reached
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "OTPField"))
                )
                otp_input = self.driver.find_element(By.ID, "OTPField")
                otp_input.send_keys(otp_list[0])
            except Exception as e:
                print(f"Error: {e}")

        try:
            error_elements = [
            self.driver.find_element(By.XPATH,"//p[@class='error validationError'")]

            test_failed = False

            for error_element in error_elements:
                if error_element.is_displayed():
                    test_failed = True
                    self.logger.info(f"Test failed. Error text: {error_element.text}")

            if test_failed:
                
                self.logger.error("Test failed due to visible error elements.")
                self.driver.save_screenshot("test_failure_screenshot.png")
                self.logger.info("Screenshot saved for reference.")
                raise Exception("Test failed due to visible error elements.")
            else:
                self.logger.info("Test passed. No error elements found.")
        except:
             pass

        time.sleep(5)
        second_form_heading = self.driver.find_element(By.XPATH,"//h3[contains(text(),'Add Your Exam Details To Get Personalized Recommen')]")
        self.logger.info(second_form_heading.text)
        assert second_form_heading.text == "Add Your Exam Details To Get Personalized Recommendations"

        budget = self.driver.find_element(By.XPATH,"(//span[@role='combobox'])[4]")
        budget.click()
        time.sleep(2)
        budget.send_keys(Keys.ENTER)
        time.sleep(5)

        next_button = self.driver.find_element(By.ID,"secondScreenSubmit")
        next_button.click()
        time.sleep(0.5)

        third_screen_heading = self.driver.find_element(By.XPATH,"//h3[contains(text(),'Add Your Academic Details To Improve Your Admissio')]")
        self.logger.info(third_screen_heading.text)
        assert third_screen_heading.text == "Add Your Academic Details To Improve Your Admission Chances"

        standard_heading = self.driver.find_element(By.XPATH,"//p[normalize-space()='12th Standard Details']")
        self.logger.info(standard_heading.text)
        assert standard_heading.text == "12th Standard Details"

        cbse_box = self.driver.find_element(By.XPATH,"(//span[@role='combobox'])[6]")
        cbse_box.click()
        time.sleep(0.5)
        cbse_box.send_keys(Keys.ENTER)
        time.sleep(1)

        year_box = Select(self.driver.find_element(By.ID,"errortwelve"))
        year_box.select_by_index(1)
        time.sleep(1)

        percentage_box = self.driver.find_element(By.XPATH,"//input[@placeholder='Enter 12th Percentage']")
        percentage_box.send_keys(98)
        time.sleep(0.5)

        stream_box = Select(self.driver.find_element(By.ID,"errortwelveSpecialization"))
        stream_box.select_by_index(1)
        time.sleep(5)

        graduation_heading = self.driver.find_element(By.XPATH,"//p[normalize-space()='Graduation Details']")
        self.logger.info(graduation_heading.text)
        time.sleep(0.5)
        assert graduation_heading.text == "Graduation Details"
        time.sleep(0.5)

        graduation_course = self.driver.find_element(By.XPATH,"(//span[@id='select2-errorgraduationCollege-container'])[1]")
        time.sleep(0.5)
        graduation_course.click()
        time.sleep(1)
        graduation_course_search = self.driver.find_element(By.XPATH,'//input[@aria-label="Search"]')
        time.sleep(0.5)
        graduation_course_search.send_keys("IIT")
        time.sleep(1)
        graduation_course_search.send_keys(Keys.ENTER)
        time.sleep(1)

        graduation_year = Select(self.driver.find_element(By.ID,"errorgraduation"))
        graduation_year.select_by_index(1)
        time.sleep(0.5)

        graduation_marks = self.driver.find_element(By.NAME,"graduationMarks")
        graduation_marks.send_keys(67)
        time.sleep(1)

        graduation_specialization = self.driver.find_element(By.ID,"select2-errorgraduationCourse-container")
        time.sleep(1)
        graduation_specialization.click()
        time.sleep(0.5)
        graduation_specialization_search = self.driver.find_element(By.XPATH,"(//input[@aria-label='Search'])[1]")
        time.sleep(1)
        graduation_specialization_search.send_keys("ANM")
        time.sleep(0.5)
        graduation_specialization_search.send_keys(Keys.ENTER)
        time.sleep(1)

        submit_button = self.driver.find_element(By.ID,"fourthScreenSubmit")
        time.sleep(0.5)
        submit_button.click()
        time.sleep(5)

        register_new_button = self.driver.find_element(By.XPATH,"//li[@class='sa_dropdown registerNew']")
        time.sleep(0.5)
        self.logger.info(register_new_button.text)
        assert register_new_button.text == "Hi " + random_names
        time.sleep(0.5)
        register_new_button.click()
        time.sleep(1)

        logout_button = self.driver.find_element(By.XPATH,"(//li[normalize-space()='Logout'])[1]")
        time.sleep(0.5)
        logout_button.click()
        time.sleep(1)

        conn = mysql.connector.connect(host='10.0.140.123', database='getmyuni_v2_test', user='cld_ro', password='yA#9Yo$un3SEzK3F')
   
        self.logger.info(conn)
        
        query = ("""SELECT * FROM `student` as st 
                    left join student_preference as stp on stp.student_id = st.id
                    where st.phone = {}""").format(randomnumber)
                            
        cursor = conn.cursor()
        
        cursor.execute(query)
        time.sleep(2)
        lead_detail = cursor.fetchone()
        time.sleep(10)
        lead_detail_list = list(lead_detail)
        self.logger.info(lead_detail_list)
        time.sleep(10)

        

        
        
        



    

        
            

                