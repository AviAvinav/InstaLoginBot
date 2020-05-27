from selenium import webdriver
from time import sleep


#chromedriver = "C:\\Users\\HARENDRA\\Downloads\\chromedriver.exe"
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

class InstaBot:
    def __init__(self, username, pwd):
        #self.driver = webdriver.Chrome(chromedriver, options=chrome_options)
        self.driver = webdriver.Firefox()
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        sleep(3)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pwd)
        sleep(3)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .clear()
        sleep(120)



InstaBot('theconcealedgenius@gmail.com', 'aviaviavi1212')