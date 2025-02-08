import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.DemoQA import ToolsQA
from pages.select_cards import select_card


class main:
    def __init__(self, driver, action):
        self.driver = driver
        self.action = action

    def main(self):
        # driver = webdriver.Chrome()
        action = ActionChains(self.driver)

        # open ToolQA link
        open_link = ToolsQA(self.driver)
        open_link.open_toolsqa()

        # select cards
        selecting_card = select_card(self.driver)
        time.sleep(5)
        selecting_card.select_element_card("radiobutton", "yes")

        # Fill forms
        selecting_card = select_card(self.driver)
        time.sleep(5)
        selecting_card.select_forms_card()


        # Alerts Frames and Windows
        select_alerts_frames = select_card(self.driver)
        time.sleep(5)
        select_alerts_frames.select_Alerts_frames_windows("alerts")



