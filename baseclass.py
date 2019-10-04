from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By



class base(object):


    def __init__(self):
         self.driver = None


    BASE_URL = 'https://go.discovery.com'

    def driverfactory(self):
        """Method initialize chrome driver and open web page"""
        self.driver = webdriver.Chrome()
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()
        return self.driver



    def waitTillElementVisible(self, locator,TIMEOUT):
        """Method to wait till WebElement is Visible on WebPage"""

        wait = WebDriverWait(self.driver, TIMEOUT)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))


    def scrollwindow(self,value):
        self.driver.execute_script("window.scrollTo(0, window.scrollY + "+str(value)+")")

    def scroll_to_element(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


