import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


##############################
class HomePage:
    TITLE = "МГУ им.\xa0Н.\xa0П.\xa0Огарёва"
    MAIN_URL = 'https://mrsu.ru/ru/'
    UNIVERSITY = (By.XPATH, '/html/body/div/div[2]/header/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/p[1]/a')
    MAIN_CORPUS = (By.CLASS_NAME, 'main__corpus')

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://mrsu.ru/ru/")
        
    def get_current_url(self):
        return self.driver.current_url

    def is_title_correct(self):
        return self.driver.title == self.TITLE
    
    
    def is_link_work(self):
        link = self.driver.find_element(*self.UNIVERSITY)
        link.click()
        return self.get_current_url() != self.MAIN_URL
    
    def is_text_correct(self):
        return self.driver.find_element(*self.MAIN_CORPUS) == "Главный корпус"
        
    

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

    def tearDown(self):
        time.sleep(0.5)
        self.driver.quit()

    def test_title(self):
        home_page = HomePage(self.driver)
        assert home_page.is_title_correct()
        
    #def test_title_spaces(self):
    #    home_page = HomePage(self.driver)
    #    assert home_page.is_title_correct()
        
    def test_link(self):
        home_page = HomePage(self.driver)
        assert home_page.is_link_work()
        
    #def test_p_text(self):
     #   home_page = HomePage(self.driver)
     #   assert home_page.is_text_correct()

###############################
if __name__ == '__main__':
    unittest.main()
