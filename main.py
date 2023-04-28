import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


##############################
class HomePage:
    TITLE = "МГУ им.\xa0Н.\xa0П.\xa0Огарёва"
    MAIN_URL = 'https://mrsu.ru/ru/'
    UNIVERSITY = (By.XPATH, '/html/body/div/div[2]/header/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/p[1]/a')
    MAIN_CORPUS = (By.CLASS_NAME, 'main__corpus')
    LOGO = (By.XPATH, '/html/body/div/div[2]/div[1]/div/div[1]/div/div/a')

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://mrsu.ru/ru/")
        
    def get_title(self):
        return self.driver.title
        
    def get_current_url(self):
        return self.driver.current_url

    def is_title_correct(self):
        return self.driver.title == self.TITLE
    
    
    def is_link_work(self):
        link = self.driver.find_element(*self.UNIVERSITY)
        link.click()
        return self.get_current_url() != self.MAIN_URL
    
    def is_text_correct(self):
        element = self.driver.find_element(*self.MAIN_CORPUS)
        return element.get_attribute('innerHTML') == "Главный корпус"
    
    def get_logo_url(self):
        element = self.driver.find_element(*self.LOGO)
        return element.get_attribute('href')
        
    

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

    def tearDown(self):
        self.driver.quit()

    def test_title(self):
        home_page = HomePage(self.driver)
        assert home_page.is_title_correct()
        
    def test_title_spaces(self):
        home_page = HomePage(self.driver)
        title = home_page.get_title()
        assert title == 'МГУ им. Н. П. Огарёва'
         
    def test_link(self):
        home_page = HomePage(self.driver)
        assert home_page.is_link_work()
        
    def test_p_text(self):
        home_page = HomePage(self.driver)
        assert home_page.is_text_correct()
        
    def test_logo_link(self):
        home_page = HomePage(self.driver)
        print(home_page.get_logo_url())
        assert home_page.get_logo_url()=='https://mrsu.ru/ru/'
        

###############################
if __name__ == '__main__':
    unittest.main()
