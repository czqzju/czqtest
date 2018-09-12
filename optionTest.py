import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.baidu.com")
        self.assertIn("百度", driver.title)
        elem = driver.find_element_by_xpath("//input[@id='kw']")
        elem.send_keys("Hello",Keys.RETURN)
        self.assertNotIn("Not", driver.page_source)



    def tearDown(self):
        # self.driver.close()
        # print("done")
        pass

if __name__ == "__main__":
    unittest.main()
