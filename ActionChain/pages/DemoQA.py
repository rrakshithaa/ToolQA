import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ToolsQA:
    def __init__(self, driver):
        self.driver = driver


    def open_toolsqa(self):
        # action = ActionChains(self.driver)
        demoqa_link = f"https://demoqa.com/"
        self.driver.get(demoqa_link)
        # self.driver.find_element(By.XPATH, '//*[contains(text(),"Male")]').click()
        time.sleep(10)
