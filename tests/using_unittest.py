import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class PythonOrgSearch(unittest.TestCase):

    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Test case method. It should always start with test_
    def test_search_in_python_org(self):
        # get driver
        driver = self.driver
        # get python.org using selenium
        driver.get("http://www.python.org")

        # assertion to confirm if title has python keyword in it
        self.assertIn("Python", driver.title)

        # locate element using name
        elem = driver.find_element(By.NAME, "q")

        # send data
        elem.send_keys("pycon")

        # receive data
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_action_chaining_in_Geek_2_Geeks(self):
        driver = self.driver

        # create action chain object
        action = ActionChains(driver)

        driver.get("https://www.geeksforgeeks.org/")
        driver.maximize_window()
        # get element
        time.sleep(3)
        element = driver.find_element(By.XPATH, "//*[text()='Courses']")

        # create action chain object
        action = ActionChains(driver)

        # click the item
        action.click(on_element=element)

        # perform the operation
        action.perform()

        ################
        #### Example of Action chains
        # menu = driver.find_element(By.CSS_SELECTOR, ".nav")
        # hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav # submenu1")
        #
        # ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

        ################

        # menu = driver.find_element_by_css_selector(".nav")
        # hidden_submenu = driver.find_element_by_css_selector(".nav # submenu1")
        #
        # actions = ActionChains(driver)
        # actions.move_to_element(menu)
        # actions.click(hidden_submenu)
        # actions.perform()

    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


# execute the script
if __name__ == "__main__":
    unittest.main()
