# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_(self):
        self.driver.get("https://baike.baidu.com/")
        self.driver.find_element(By.LINK_TEXT, "新闻").click()