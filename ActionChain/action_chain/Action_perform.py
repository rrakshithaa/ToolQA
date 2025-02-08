from selenium.webdriver.common.action_chains import ActionChains
from pages.DemoQA import ToolsQA


class Actionchain('setup'):
    def __init__(self, driver, action):
        self.action = action
        self.driver = driver

    def actions(self):
        self.action = ActionChains(self.driver)


