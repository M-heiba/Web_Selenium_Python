# inherit TestCase Class and create a new test class
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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

    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


# execute the script
if __name__ == "__main__":
    unittest.main()
