import string
import time
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, MoveTargetOutOfBoundsException
from webdriver_manager.chrome import ChromeDriverManager
from random import randint

class Selenium:
    """Класс для реализации базовых функций"""
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        #options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

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
        cookie_permission_1 = "/html/body/div[4]/div/div/button[1]"
        self.click_if_exist(cookie_permission_1)
        time.sleep(3)
        driver.find_element(By.NAME, 'username').send_keys(login)
        driver.find_element(By.NAME, 'password').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        
        try: 
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/nav/div[2]/div")))
            print('logged in succesfully')
        except TimeoutException:
            print('log in failed')  
            sys.exit()
        
        cookie_permission_2 = '/html/body/div[4]/div/div/button[1]'
        self.click_if_exist(cookie_permission_2)
    
        enable_notifications = '/html/body/div[5]/div/div/div/div[3]/button[2]'
        self.click_if_exist(enable_notifications)

        another_notification = '/html/body/div[6]/div/div/div/div[3]/button[1]'
        self.click_if_exist(another_notification)


class Scrapper:
    """Класс для реализации функций парсера"""
    def __init__(self, selenium):
        self.selenium = selenium

    def scrape_followers(self, target_url):
        driver = self.selenium.driver
        driver.get(target_url)
        count = int(driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a/div/span").text)
        driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a/div").click()
        time.sleep(5)
        list_of_followers = []
        while True:
            driver.execute_script('''
                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                fDialog.scrollTop = fDialog.scrollHeight
            ''')

            list_of_followers = driver.find_elements(By.XPATH, "/html/body/div[6]/div/div/div/div[2]/ul/div/li/div/div[1]/div[2]/div[1]/span/a/span")
            if len(list_of_followers) == count:
                break
        return [i.text for i in list_of_followers]
        
class Bot:
    "Класс для реализации функций бота"
    def __init__(self, selenium):
        self.selenium = selenium

    def follow(self, follow_url):
        driver = self.selenium.driver
        driver.get(follow_url)
       
        follow_button ="//*[@id=\"react-root\"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button"
        self.selenium.click_if_exist(follow_button, error_message = 'Incorrect follow_url!')

        try: 
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div/div[3]/button[1]")))
            print('You have already followed')
            return 0
        except TimeoutException:
            print('Followed succesfully')

    def like(self, post_url):
        driver = self.selenium.driver
        driver.get(post_url)
        self.selenium.click_if_exist("/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button", error_message = 'Incorrect like_url!') 

    def like_posts(self, post_urls):
        for url in post_urls:
            self.like(url)
        

class Controller:
    def __init__(self):
        self.selenium = Selenium()
        self.bot = Bot(self.selenium)
        self.scrapper = Scrapper(self.selenium)

    def login(self, login, password):
        self.selenium.login(login, password)

    def scrape_followers(self, target_url):
        return self.scrapper.scrape_followers(target_url)

    def follow(self, follow_url):
        self.bot.follow(follow_url)
    
    def like(self, post_url):
        self.bot.like(post_url)

    def like_posts(self, post_urls):
        self.bot.like_posts(post_urls)


