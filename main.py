import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from dotenv import load_dotenv

class Selenium:
    """Класс для реализации базовых функций"""
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self, login, password):
        driver = self.driver
        url = 'https://www.instagram.com'

        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)

        cookie_permission = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div/button[1]')
        if len(cookie_permission)>0:
            cookie_permission[0].click()
        driver.implicitly_wait(20)
        
        driver.find_element(By.NAME, 'username').send_keys(login)
        driver.find_element(By.NAME, 'password').send_keys(password)
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        driver.implicitly_wait(10)

        driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/section/main/div/div/div/div/button").click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]").click()


        print("logged in successfully")
        

    def refresh_page(self):
        """Пример базовой функции"""
        print(f'{self.driver} делает refresh_page')


class Scrapper:
    """Класс для реализации функций парсера"""
    def __init__(self, selenium):
        self.selenium = selenium

    def scrape_followers(self, target_url):
        driver = self.selenium.driver
        driver.get(target_url)
        driver.implicitly_wait(5)

        followers = int(driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a/div/span").text) 
        driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a/div/span").click()

        list_of_followers = 0
        
        self.selenium.refresh_page()
        print('[+] scrape_followers')


class Bot:
    "Класс для реализации функций бота"
    def __init__(self, selenium):
        self.selenium = selenium

    def follow(self):
        self.selenium.refresh_page()
        print('[+] follow')
    
    def like(self, post_url):
        driver = self.selenium.driver
        driver.get(post_url)
        driver.implicitly_wait(5)

        driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button").click()

        pass


class Controller:
    def __init__(self):
        self.selenium = Selenium()
        self.bot = Bot(self.selenium)
        self.scrapper = Scrapper(self.selenium)

    def login(self, login, password):
        self.selenium.login(login, password)

    def scrape_followers(self, target_url):
        self.scrapper.scrape_followers(target_url)

    def follow(self):
        self.bot.follow()
    
    def like(self, post_url):
        self.bot.like(post_url)

def main():

    options = webdriver.ChromeOptions()
    options.add_argument('--allow-profiles-outside-user-dir')
    options.add_argument('--enable-profile-shortcut-manager')
    options.add_argument(r'user-data-dir=.\User')
    options.add_argument('--profile-directory=Profile 1')


    load_dotenv()

    insta_tool = Controller()

    login = os.environ.get('LOGIN')
    password = os.environ.get('PASSWORD')
    target_url = os.environ.get('TARGET_URL')
    post_url = os.environ.get('POST_URL')

    insta_tool.login(login, password)
    insta_tool.like(post_url)

    #insta_tool.scrape_followers(target_url)


    time.sleep(1000)
    #insta_tool.follow()


if __name__ == '__main__':
    main()
