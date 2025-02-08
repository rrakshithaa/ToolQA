import time
from multiprocessing.spawn import spawn_main

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger


class select_card:

    def __init__(self, driver):
        self.driver = driver

    def select_element_card(self, select_element, radio_button):
        try:
            action = ActionChains(self.driver)
            time.sleep(5)
            elements_card = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[1]')))
            elements_card.click()
            time.sleep(5)

            logger.info("Please select element: Text Box, Check Box, Radio Button, Web Table, Buttons ")
            time.sleep(5)
            if select_element == "textbox":
                text_box_click = self.driver.find_element(By.XPATH, "//*[contains(text(),'Text Box')]")
                text_box_click.click()
                time.sleep(5)
                # fill data
                full_name = self.driver.find_element(By.ID, "userName")
                full_name.send_keys("Rakshitha")
                email = self.driver.find_element(By.ID, "userEmail")
                email.send_keys("example@gmail.com")
                current_address = self.driver.find_element(By.ID, "currentAddress")
                current_address.send_keys("RT Nagar, Bengaluru")
                permanent_address = self.driver.find_element(By.ID, "permanentAddress")
                permanent_address.send_keys("RT Nagar, Bengaluru!!")

                submit = self.driver.find_element(By.XPATH, '//*[@id="submit"]')
                submit.click()
                time.sleep(5)
                logger.info("Successfully completed filling textboxes!!!")

            elif select_element == "checkbox".lower():
                check_box_click = self.driver.find_element(By.ID, 'id="item-1"')
                check_box_click.click()

                # check box action
                select_check_box = self.driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/label')
                select_check_box.click()
                result = self.driver.find_element(By.XPATH, '//*[@id="result"]')
                logger.info(f"element selected{result}")

            elif select_element == "radiobutton".lower():
                radio_button_click = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Radio Button')]")))
                radio_button_click.click()

                time.sleep(10)
                # radio button operations
                logger.info("Do you like the site?  \n Yes \n Impressive \n No ")
                yes = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'Yes')]")))
                do = self.driver.find_element(By.XPATH, "//*[contains(text(),'Yes')]").click()
                action.move_to_element(do).click().perform()
                logger.info("radio button")
                time.sleep(4)
                impressive = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="impressiveRadio"]')))
                no = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="noRadio"]')))
                if radio_button == "yes":
                    yes.click()
                elif radio_button == "impressive":
                    impressive.click()
                else:
                    no.click()
                result = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/p')
                logger.info(f"selected: {result}")

            elif select_element == 'webtable':
                web_tables_click = self.driver.find_element(By.ID, 'id="item-3"')
                web_tables_click.click()

                # add table
                add_button = self.driver.find_element(By.XPATH, '//*[@id="addNewRecordButton"]')
                add_button.click()
                first_name = self.driver.find_element(By.XPATH, '//*[@id="firstName"]')
                first_name.send_keys("Rakshitha")
                last_name = self.driver.find_element(By.XPATH, '//*[@id="lastName"]')
                last_name.send_keys("R")
                table_email = self.driver.find_element(By.XPATH, '//*[@id="userEmail"]')
                table_email.send_keys("example@gmail.com")
                age = self.driver.find_element(By.XPATH, '//*[@id="age"]')
                age.send_keys("22")
                salary = self.driver.find_element(By.XPATH, '//*[@id="salary"]')
                salary.send_keys("100000")
                department = self.driver.find_element(By.XPATH, '//*[@id="department"]')
                department.send_keys("IT")
                submit = self.driver.find_element(By.ID, "submit")
                submit.click()
                logger.info("Data added to table successfully!!!")

            else:
                buttons_click = self.driver.find_element(By.ID, 'id="item-4"')
                buttons_click.click()

                double_click_button = self.driver.find_element(By.XPATH, '//*[@id="doubleClickBtn"]')
                action.double_click(double_click_button).perform()
                double_click_result = self.driver.find_element(By.XPATH, '//*[@id="doubleClickMessage"]')
                logger.info(f"single click buttons: {double_click_result}")

                right_click_button = self.driver.find_element(By.XPATH, '//*[@id="rightClickBtn"]')
                action.context_click(right_click_button).perform()
                right_click_result = self.driver.find_element(By.XPATH, '//*[@id="rightClickMessage"]')
                logger.info(f"single click buttons: {right_click_result}")

                single_click = self.driver.find_element(By.XPATH, '//*[@id="qP1En"]')
                single_click.click()
                single_click_result = self.driver.find_element(By.XPATH, '//*[@id="dynamicClickMessage"]')
                logger.info(f"single click buttons: {single_click_result}")
        except Exception as e:
            logger.error(f"Error: {e}")

    def select_forms_card(self):
        try:
            forms_card = self.driver.find_element(By.XPATH, '//*[contains(text(),"Forms")]')
            forms_card.click()
            time.sleep(5)
            practice_form = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[2]/div')
            practice_form.click()
            time.sleep(5)
            # fill
            # WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '')))
            first_name = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="firstName"]')))
            first_name.send_keys("Rakshitha")
            email = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="userEmail"]')))
            email.send_keys("example@gmail.com")
            mobile_num = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="userNumber"]')))
            mobile_num.send_keys("9876543210")
            time.sleep(5)

        except Exception as e:
            logger.error(f"Error: {e}")


    def select_Alerts_frames_windows(self, select_option):
        try:
            alerts_frames_windows_card = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[3]')
            alerts_frames_windows_card.click()
            time.sleep(5)

            logger.info("Please select option: \nbrowser window \nalerts \nframes \nnested frames \nmodal dialogs")

            if select_option == "window":
                logger.info("gng to window")
                browser_window = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "(//li[@id='item-0']/span)[3]")))
                browser_window.click()

                new_tab = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tabButton"]')))
                new_tab.click()
                window_handles = self.driver.window_handles
                original_tab = self.driver.current_window_handle
                self.driver.switch_to.window(window_handles[-1])
                logger.info("Now on new tab:", self.driver.current_url)
                self.driver.close()
                time.sleep(5)
                self.driver.switch_to.window(original_tab)

                new_tab_result = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sampleHeading"]')))
                logger.info(f"new_tab: {new_tab_result}")

                new_window = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="windowButton"]')))
                new_window.click()
                new_window_result = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sampleHeading"]')))
                logger.info(f"new window: {new_window_result}")

                new_win_msg = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="messageWindowButton"]')))
                new_win_msg.click()
                new_window_result = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/text()')))
                logger.info(f"new window: {new_window_result}")

            elif select_option == "alerts":
                alerts = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/div/ul/li[2]')))
                alerts.click()

                alert_1 = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="alertButton"]')))
                alert_1.click()
                Alert(self.driver).accept()

                alert_5sec = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="timerAlertButton"]')))
                alert_5sec.click()
                time.sleep(5)
                Alert(self.driver).accept()
                # confirm_result_ok = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="confirmResult"]')))
                # logger.info(f"alert confirmed ok: {confirm_result_ok}")
                # confirm_result_cancel = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="confirmResult"]')))
                # logger.info(f"alert confirmed cancel: {confirm_result_cancel}")

                prompt_text_box = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="promtButton"]')))
                prompt_text_box.click()
                Alert(self.driver).send_keys("rakshitha")
                Alert(self.driver).accept()

            else:
                model = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/div/ul/li[5]')))
                model.click()

                small_model = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="showSmallModal"]')))
                small_model.click()
                alert_small_model = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div')))
                close_button = alert_small_model.find_element(By.XPATH, '//*[@id="closeSmallModal"]')
                close_button.click()

                large_model = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="showLargeModal"]')))
                large_model.click()
                alert_large_model = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div')))
                close_button = alert_large_model.find_element(By.XPATH, '//*[@id="closeLargeModal"]')
                close_button.click()

        except Exception as e:
            logger.error(f"Error: {e}")



    # def select_widgets_card(self):
    #     widgets_card = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[4]')
    #     widgets_card.click()
    #
    #
    # def select_Interaction_card(self):
    #     interactions_card = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[5]')
    #     interactions_card.click()
    #
    #
    # def select_Book_store_application(self):
    #     book_store_application_card = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[6]')
    #     book_store_application_card.click()

