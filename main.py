import sys
import time

from selenium import webdriver
import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException, MoveTargetOutOfBoundsException
from webdriver_manager.chrome import ChromeDriverManager
from random import randint

class Selenium:
    """Класс для реализации базовых функций"""
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def click_if_exist(self, element, timeout = 3, error_message = ''):
        try: 
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, element)))
            self.driver.find_element(By.XPATH, element).click()
        except TimeoutException:
            if len(error_message) < 1:
                return False
            print(error_message)

    def imitate_user_actions(self):
        action = ActionChains(self.driver)
        offsets = [randint(100,700) for _ in range(10)]
        try:
            action.scroll(offsets[0], offsets[1], offsets[2], offsets[3]).perform()
            time.sleep(0.5)
            action.scroll(offsets[4], offsets[5], offsets[6], offsets[7]).perform()
            action.move_by_offset(offsets[8], offsets[9])
        except MoveTargetOutOfBoundsException:
            pass

    def login(self, login, password):
        driver = self.driver
        driver.get('https://www.instagram.com')
        driver.maximize_window()
        time.sleep(1.5)
        self.imitate_user_actions()
        driver.find_element(By.NAME, 'username').send_keys(login)
        driver.find_element(By.NAME, 'password').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        
        cookie_permission = '/html/body/div[4]/div/div/button[1]'
        self.click_if_exist(cookie_permission)

        driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/section/main/div/div/div/div/button").click()
    
        enable_notifications = '/html/body/div[6]/div/div/div/div[3]/button[1]'
        self.click_if_exist(enable_notifications)

        print('logged in succesfully')

class Scrapper:
    """Класс для реализации функций парсера"""
    def __init__(self, selenium):
        self.selenium = selenium

    def scrape_followers(self, target_url):
        driver = self.selenium.driver
        driver.get(target_url)

        followers = int(driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a/div/span").text) 
        driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a/div/span").click()

        list_of_followers = 0
        
        print('[+] scrape_followers')


class Bot:
    "Класс для реализации функций бота"
    def __init__(self, selenium):
        self.selenium = selenium

    def follow(self, follow_url):
        driver = self.selenium.driver
        driver.get(follow_url)
       
        follow_button ="/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button"
        self.selenium.click_if_exist(follow_button)        


    def like(self, post_url):
        driver = self.selenium.driver
        driver.get(post_url)

        driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button").click()


class Controller:
    def __init__(self):
        self.selenium = Selenium()
        self.bot = Bot(self.selenium)
        self.scrapper = Scrapper(self.selenium)

    def login(self, login, password):
        self.selenium.login(login, password)

    def scrape_followers(self, target_url):
        self.scrapper.scrape_followers(target_url)

    def follow(self, follow_url):
        self.bot.follow(follow_url)
    
    def like(self, post_url):
        self.bot.like(post_url)

def main():
    insta_tool = Controller()
    insta_tool.selenium.driver.implicitly_wait(10)

    login = sys.argv[1]
    password = sys.argv[2]
    insta_tool.login(login, password)

    #insta_tool.like(post_url)
    #insta_tool.follow(follow_url)
    #insta_tool.scrape_followers(target_url)
    time.sleep(1000)


if __name__ == '__main__':
    main()
