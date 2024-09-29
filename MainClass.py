import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class VisitUrlTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://mysitebook.io/")

    def test_login(self):
        time.sleep(10)
        close_button = self.driver.find_element(By.XPATH, '//div[@class="close"]')
        close_button.click()
        time.sleep(2)
        login_button = self.driver.find_element(By.XPATH, '//a[@data-event-name="LOGIN"]')
        login_button.click()
        time.sleep(20)
        mobile_number_field = self.driver.find_element(By.XPATH,'//input[@id="mobileNumber"]')
        time.sleep(5)
        mobile_number_field.send_keys('9970539817')
        continue_button_field = self.driver.find_element(By.XPATH, '//button[text()=" Continue"]')
        continue_button_field.click()
        password_field = self.driver.find_element(By.XPATH,'//input[@id="password"]')
        password_field.send_keys("Nikita@123")
        login_button_field = self.driver.find_element(By.XPATH, '//button[text()=" Login"]')
        login_button_field.click()

    def test_sample_project(self):
        time.sleep(10)
        sample_project_element = self.driver.find_element(By.XPATH, '//span[text()=" Sample bungalow project"]')
        sample_project_element.click()
        first_project = self.driver.find_element(By.XPATH,'//*[@id="quotes-list"]/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper[1]/datatable-body-row/div[2]/datatable-body-cell[2]')
        first_project.click()




def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
