import time

import pytest
from selenium import webdriver
from pages.DemoQA import ToolsQA
from selenium.webdriver.common.action_chains import ActionChains
from pages.select_cards import select_card


@pytest.mark.usefixtures("setup")
class TestActions:

    def test_open_link(self):
        open_link = ToolsQA(self.driver)
        open_link.open_toolsqa()


    def test_element_card(self):
        self.test_open_link()
        selecting_card = select_card(self.driver)
        time.sleep(5)
        selecting_card.select_element_card("textbox", "yes")

    def test_forms_card(self):
        self.test_open_link()
        selecting_card = select_card(self.driver)
        time.sleep(5)
        selecting_card.select_forms_card()

    def test_alerts_frames_windows(self):
        self.test_open_link()
        select_alerts_frames = select_card(self.driver)
        time.sleep(5)
        select_alerts_frames.select_Alerts_frames_windows("alerts")
