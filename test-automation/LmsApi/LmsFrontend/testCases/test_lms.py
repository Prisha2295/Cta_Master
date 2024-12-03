import time
import os
import requests
from dotenv import load_dotenv
from LmsApi.LmsFrontend.testCases.password_reset import handle_url_conditions
from LmsApi.LmsFrontend.testCases.add_leadremark import lead_remark
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from customLogger import get_logger
from conftest import setup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    TimeoutException
)

load_dotenv()

lms_preprod_user = os.getenv("lms_preprod_user")
lms_preprod_pass = os.getenv("lms_preprod_pass")
lms_profile_url = os.getenv("lms_profile_url")
lms_url = os.getenv("lms_url")




class Test_Leadfrontend():

    def test_ctalmsfrontend(self, setup):
        self.logger = get_logger(test_name='lmssanity')
        self.logger.info("******* Starting Lms frontend*********")

        self.driver = setup
        if not self.driver:
            self.logger.error("Driver setup failed. Exiting test.")
            return

        # Navigate to the URL
        self.driver.get(lms_url)

        # Retrieve the actual title and log it
        actual_title = self.driver.title
        self.logger.info(f"Page Title: {actual_title}")

        current_url = self.driver.current_url
        self.logger.info("Current URL: " + current_url)
        response = requests.get(current_url)
        self.logger.info("Response: " + str(response.status_code))
        time.sleep(2)
        
        # Wait until the username field is visible and then input the username
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
        

        #handle url condition for /lead-dashboard and /reset-password
        handle_url_conditions(self)
        time.sleep(5)

        try:
            start_time = time.time()
            WebDriverWait(self.driver, 100).until(
                EC.visibility_of_element_located((By.XPATH, "(//div[contains(@class,'leadCardDetails')])[1]"))
            )
            end_time = time.time()
            
            # Calculate load time
            load_time = end_time - start_time
            self.logger.info(f"Element load time: {load_time} seconds")
            print(f"Element load time: {load_time} seconds")

        except TimeoutException:
            self.logger.info("Element not visible within the given time frame")
            print("Element not visible within the given time frame")

        # Get all nav tabs
        nav_tabs = self.driver.find_elements(By.XPATH, "(//ul[contains(@class,'nav-justified mb-3 tabsBox text-primary nav')])[1]/li")

        # Loop through tabs by index to avoid stale element exceptions
        for index in range(len(nav_tabs)):
            # Re-fetch the tabs list to avoid stale references
            nav_tabs = self.driver.find_elements(By.XPATH, "(//ul[contains(@class,'nav-justified mb-3 tabsBox text-primary nav')])[1]/li")
            
            # Get current tab element based on index
            tab = nav_tabs[index]
            
            # Get tab name and count
            tab_name = tab.text.strip()
            badge_count = tab.find_element(By.XPATH, ".//span").text.strip()
            self.logger.info(f"Tab: {tab_name}, Count: {badge_count}")
            print(f"Tab: {tab_name}, Count: {badge_count}")
            
            # Click on each tab
            tab.click()
            
            # Measure load time of leadCardDetails
            try:
                start_time = time.time()
                
                # Wait for either 'leadCardDetails' or 'tabsPaginationBox' to appear
                load_leadcard = WebDriverWait(self.driver, 20).until_not(
                    EC.visibility_of_element_located((By.XPATH, "(//div[contains(@class,'leadCardDetails')])[1]"))
                )
                
                end_time = time.time()
                load_time = end_time - start_time
                
                self.logger.info(f"Load time for '{tab_name}' tab: {load_time:.2f} seconds")
                print(f"Load time for '{tab_name}' tab: {load_time:.2f} seconds")
                time.sleep(3)
                
            except Exception:
                try:
                    start_time = time.time()
                    # If 'leadCardDetails' is not visible, check for 'tabsPaginationBox'
                    no_leads_element = WebDriverWait(self.driver, 20).until_not(
                        EC.visibility_of_element_located((By.XPATH, "(//div[@class='tabsPaginationBox shadow-none mb-0 mt-0 card'])[1]"))
                    )
                    end_time = time.time()
                    load_time = end_time - start_time
                    self.logger.info(f"0 Lead found for '{tab_name}' tab and {load_time:.2f} seconds")
                    print(f"0 Lead found for '{tab_name}' tab")
                    time.sleep(3)
                
                except Exception as e:
                    # Handle the case where neither element is found
                    self.logger.info(f"Failed to load 'leadCardDetails' and no 'tabsPaginationBox' found for '{tab_name}' tab: {e}")
                    print(f"Failed to load 'leadCardDetails' and no 'tabsPaginationBox' found for '{tab_name}' tab: {e}")
                    time.sleep(3)
        
        # Click back on L2 Fresh tab
        l2_fresh_tab = self.driver.find_element(By.XPATH, "//a[contains(text(),'L2 Fresh')]")
        l2_fresh_tab.click()
        self.logger.info("Returned to 'L2 Fresh' tab.")
        print("Returned to 'L2 Fresh' tab.")
        time.sleep(4)

        # search_lead = self.driver.find_element(By.XPATH, "//input[@id='search-task-options']")
        # search_lead.send_keys('test')
        # time.sleep(2)

        self.logger.info("******* Collecting Lead Details*********")
        find_name = self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[1]/div/div[2]/p[1]")
        self.logger.info("Lead Name: " + find_name.text)
        time.sleep(5)

        find_lead_id = self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[1]/div/div[2]/p[2]/span")
        time.sleep(5)
        find_lead_id_text = find_lead_id.text
        self.logger.info(find_lead_id_text)
        time.sleep(5)
        
        lead_id_number = find_lead_id_text.split(": ")[1] 
        self.logger.info(lead_id_number)
        time.sleep(2)

        lead_id_click = self.driver.find_element(By.XPATH, "(//button[contains(@type,'button')][normalize-space()='Lead Details'])[1]")
        lead_id_click.click()
        time.sleep(5)

        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
            lead_url = self.driver.current_url
            self.logger.info("Lead URL: " + lead_url)
        else:
            self.logger.error("New window did not open. Unable to switch.")

        test_url = f"{lms_profile_url}lead-dashboard/{lead_id_number}"
        self.logger.info(test_url)


        assert lead_url == f"{lms_profile_url}lead-dashboard/{lead_id_number}", f"URL does not match the expected URL"
        time.sleep(4)
        
        #Add lead remark
        update_callback = self.driver.find_element(By.XPATH,"//img[@class='update-remarks-icon']")
        time.sleep(2)
        update_callback.click()
        time.sleep(2)

        lead_remark(self)
        time.sleep(5)

        self.logger.info("******* Saving Profile Changes*********")

        profile_tab_click=self.driver.find_element(By.XPATH,"//a[normalize-space()='Profile']")
        profile_tab_click.click()
        time.sleep(4)

        save_profile_changes=self.driver.find_element(By.XPATH,"//button[normalize-space()='Save Changes']")
        save_profile_changes.click()
        time.sleep(4)

        lead_url = self.driver.current_url
        self.logger.info("Lead URL: " + lead_url)

        assert lead_url == f"{lms_url}lead-dashboard/{lead_id_number}", f"URL does not match the expected URL"

        self.logger.info("******* Checking Number of Shortlisted Colleges before shortlisting one*********")
        shortist_colleges_tab=self.driver.find_element(By.XPATH,"//a[normalize-space()='Shortlisted']")
        shortist_colleges_tab.click()
        time.sleep(4)

        no_of_elements_shortlisttab=self.driver.find_elements(By.CSS_SELECTOR,".cohort-card-box.card-shortlist.card")
        No_of_colleges_in_shortlisted=len(no_of_elements_shortlisttab)
        self.logger.info("Number of Shortlisted Colleges: " + str(No_of_colleges_in_shortlisted))


        recommended_colleges_tab=self.driver.find_element(By.XPATH,"//a[normalize-space()='Recommended']")
        recommended_colleges_tab.click()
        time.sleep(4)

        no_of_colleges_recommended=self.driver.find_elements(By.CSS_SELECTOR,".cohort-card-box.card")
        No_of_colleges_in_recom_tab=len(no_of_colleges_recommended)
        self.logger.info("No of colleges recommended: " +str(No_of_colleges_in_recom_tab))
        time.sleep(4)

        recommeneded_shortlisted_name=self.driver.find_element(By.XPATH,"(//div[@class='college-name-head'])[1]")
        shortlisted_college_name=recommeneded_shortlisted_name.text
        self.logger.info("Name of 1st college in recommendation: " +shortlisted_college_name)
        time.sleep(4)

        recommeneded_shortlisting_1=self.driver.find_element(By.XPATH,"(//i[contains(@class,'bx bx-heart text-white')])[1]")
        recommeneded_shortlisting_1.click()
        time.sleep(10)

        recommeneded_shortlisting_2=self.driver.find_element(By.XPATH,"(//div[@class='relevent-course mt-2']/div[1])[1]")
        recommeneded_shortlisting_2.click()
        time.sleep(4)

        recommended_submit=self.driver.find_element(By.XPATH,"//div[@class='modal-footer']//button[@class='btn btn-success'][normalize-space()='Shortlist']")
        recommended_submit.click()
        time.sleep(3)

        shortlist_message=self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[2]/div/div/div[1]/div[2]")
        time.sleep(1)
        self.logger.info(shortlist_message.text)
        assert shortlist_message.text == "College name shortlisted"
        time.sleep(4)
        
        shortist_colleges_tab.click()
        time.sleep(4)
        
        lead_url = self.driver.current_url
        self.logger.info("Lead URL: " + lead_url)

        assert lead_url == f"{lms_url}lead-dashboard/{lead_id_number}", f"URL does not match the expected URL"

        no_of_colleges_shortlisted=self.driver.find_elements(By.CSS_SELECTOR,".lead-recom-college-inner")
        no_of_colleges_in_shortlisted2=len(no_of_colleges_shortlisted)
        self.logger.info("Number of Shortlisted Colleges after shortlisting one: " + str(no_of_colleges_in_shortlisted2))
        time.sleep(4)

        shortisted_college_name=self.driver.find_element(By.XPATH,"(//div[@class='college-name-head'])[1]")
        shortlisted_college_namee=shortisted_college_name.text
        self.logger.info("Name of College Shortlisted: " + shortlisted_college_namee)
        time.sleep(4)

        self.logger.info("**********Send For Reconciliation************")
        try:
            send_for_recon = self.driver.find_element(By.XPATH,"//button[normalize-space()='Send colleges for reconciliation']")
            self.logger.info(send_for_recon.text)
            time.sleep(1)
            send_for_recon.click()
            time.sleep(5)

            recon_institute_name = self.driver.find_element(By.XPATH,"//*[@id='shortlist-modal-wrap']/div/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/label")
            self.logger.info(recon_institute_name.text)
            time.sleep(1)

            try:
                # Locate the checkbox element
                recon_checkbox = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/input")
                
                # Wait briefly before interacting
                time.sleep(2)
                
                # Check if the checkbox is selected (activated)
                if recon_checkbox.is_selected():
                    self.logger.info("Checkbox is already selected.")
                else:
                    # Click the checkbox if it's not selected
                    recon_checkbox.click()
                    self.logger.info("Checkbox was not selected and is now activated.")
                
                # Verify the checkbox state after interaction
                if recon_checkbox.is_selected():
                    self.logger.info("Checkbox is now selected.")
                else:
                    self.logger.warning("Checkbox is still not selected after clicking.")
                
                time.sleep(2)
            except (NoSuchElementException, ElementNotInteractableException) as e:
                self.logger.error(f"Error handling the checkbox: {e}")

            click_recon = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Send for Recon'])[1]")
            if click_recon.is_enabled():
                self.logger.info("The reconciliation element is enabled.")
                time.sleep(2)
                click_recon.click()
                time.sleep(2)
            else:
                self.logger.info("The reconciliation element not enabled")
            
            try:
                reconciliation_message=self.driver.find_element(By.ID,"error-msg")
                self.logger.info(reconciliation_message.text)
                assert reconciliation_message.text == "College sent for reconciliation."
                time.sleep(4)
            
            except:
                self.logger.warning("The reconciliation message element is not enabled.")
                
                
        except Exception as e:
            self.logger.info(e)               
        
        self.logger.info("******* Updating Recon Status*********")
        self.driver.refresh()
        time.sleep(4)
        shortist_colleges_tab_1=self.driver.find_element(By.XPATH,"//a[normalize-space()='Shortlisted']")
        shortist_colleges_tab_1.click()
        time.sleep(4)
        recon_status=self.driver.find_element(By.XPATH,"(//div[@class='bottom-line'])[2]/span") 
        self.logger.info("Recon Status : " + recon_status.text)
        time.sleep(3)
        
        self.logger.info("******* Updating Product Status to NI*********")
        updating_status=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Update'])[1]")
        updating_status.click()
        time.sleep(4)
        product_status=Select(self.driver.find_element(By.XPATH,"//select[@aria-label='Product status']"))
        product_status.select_by_index(2)
        
        Product_status = product_status.first_selected_option
        self.logger.info("Product Status : " + Product_status.text)
        time.sleep(4)
        status_submit=self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div/div[3]/button[2]")
        status_submit.click()
        time.sleep(1)

        NI_message=self.driver.find_element(By.XPATH,"//div[contains(text(),'Product Stage Updated!')]")
        self.logger.info(NI_message.text)
        assert NI_message.text == "Product Stage Updated!"
        time.sleep(4)

        
        Ni_colleges_tab=self.driver.find_element(By.XPATH,"//a[normalize-space()='NI/DNP']")
        Ni_colleges_tab.click()
        time.sleep(4)

        lead_url = self.driver.current_url
        self.logger.info("Lead URL: " + lead_url)

        assert lead_url == f"{lms_url}lead-dashboard/{lead_id_number}", f"URL does not match the expected URL"

        No_of_colleges_NI=self.driver.find_elements(By.CSS_SELECTOR,".lead-recom-college-inner")
        Number_of_colleges_NI=len(No_of_colleges_NI)
        self.logger.info("Number of colleges marked NI: " + str(Number_of_colleges_NI))
        time.sleep(4)
        Ni_college_name=self.driver.find_element(By.XPATH," (//div[@class='college-name-head'])[1]")
        Ni_marked_college=Ni_college_name.text
        self.logger.info("Name of the college marked Ni: " + Ni_marked_college)
        time.sleep(4)
        Moving_Ni_to_Shortlist= self.driver.find_element(By.XPATH,"//button[normalize-space()='Move to shortlist']")
        time.sleep(2)
        Moving_Ni_to_Shortlist.click()
        time.sleep(1)

        success_msg = self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[2]/div/div/div[1]/div[2]")
        self.logger.info(success_msg.text)
        time.sleep(7)
        
        send_button = self.driver.find_element(By.XPATH,"//button[normalize-space()='Send']")
        send_button.click()
        self.logger.info("clicking on CAF Link")

        caflink_button = self.driver.find_element(By.XPATH,"//button[normalize-space()='CAF (Cart Link)']")
        caflink_button.click()
        time.sleep(2)

        check_box = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/input")
        check_box.click()
        time.sleep(2)

        self.logger.info("Selecting course group")
        selecting_course_grp=self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/input")
        selecting_course_grp.click()
        time.sleep(2)

        send_cart_button = self.driver.find_element(By.XPATH,"//button[normalize-space()='Send CAF Cart Link']")
        send_cart_button.click()
        time.sleep(1)

        success_msg_caf=self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[2]/div/div/div[1]/div[2]")
        self.logger.info(success_msg_caf.text)
        time.sleep(2)
        assert success_msg_caf.text == "CAF Cart link sent to the Lead"

        
