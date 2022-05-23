import time
from model import Selenium, Bot, Scrapper
from view import View


class Controller:
    def __init__(self, mode):
        self.view = View()
        self.selenium = Selenium(mode)
        self.bot = Bot(self.selenium)
        self.scrapper = Scrapper(self.selenium)
        self.view.presentation()

    def login(self):
        login, password = self.view.login()
        
        if self.selenium.login(login, password):
            self.view.success()
        else:
            self.view.error()
            exit(0)

    def scrape_followers(self):
        target_url = self.view.get_url("Введите ссылку на аккаунт")
        followers = self.scrapper.scrape_followers(target_url)
        f = open("./data/followers.txt", "w")

        with self.view.console.status("[bold green]Парсинг подписчиков в followers.txt...") as status:
            for follower in followers:
                f.write(follower)
                self.view.console.print(f"[green] [+] Подписчик {follower.rstrip()} записан[/green]")

        f.close()

    def follow(self):
        url_list_file = self.view.get_url_list("Укажите имя файла из каталога data/, в котором находится список пользователей, на которых необходимо подписаться", "users.txt")
        f = open(f"./data/{url_list_file}", "r")

        for user in self.view.track(f.readlines(), "Идёт подписка..."):
            self.bot.follow(user)
            print(f'[+] {user}')
            time.sleep(1)

        f.close()

    
    def like(self):
        url_list_file = self.view.get_url_list("Укажите имя файла из каталога data/, в котором находится список постов, которые необходимо пролайкать", "posts_to_like.txt")
        f = open(f"./data/{url_list_file}", "r")
        
        for post in self.view.track(f.readlines(), "Идёт проставление лайков..."):
            self.bot.like(post)
            print(f'[+] {post}')
            time.sleep(1)

        f.close()

    def get_posts(self):    
        target_url = self.view.get_url("Введите ссылку на аккаунт")
        posts = self.scrapper.get_posts(target_url)
        f = open("./data/posts.txt", "w")

        with self.view.console.status("[bold green]Парсинг постов в post.txt...") as status:
            for post in posts:
                f.write(post)
                self.view.console.print(f"[green] [+] Пост {post.rstrip()} записан[/green]")

        f.close()
     

