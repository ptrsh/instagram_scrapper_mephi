class Selenium:
    """Класс для реализации базовых функций"""
    def __init__(self, driver_path):
        self.driver = driver_path

    def login(self):
        pass

    def refresh_page(self):
        """Пример базовой функции"""
        print(f'{self.driver} делает refresh_page')


class Scrapper:
    """Класс для реализации функций парсера"""
    def __init__(self, selenium):
        self.selenium = selenium

    def scrape_followers(self):
        self.selenium.refresh_page()
        print('[+] scrape_followers')


class Bot:
    "Класс для реализации функций бота"
    def __init__(self, selenium):
        self.selenium = selenium

    def follow(self):
        self.selenium.refresh_page()
        print('[+] follow')


class Controller:
    def __init__(self, driver_path):
        self.selenium = Selenium(driver_path)
        self.bot = Bot(self.selenium)
        self.scrapper = Scrapper(self.selenium)

    def login(self):
        self.selenium.login()

    def scrape_followers(self):
        self.scrapper.scrape_followers()

    def follow(self):
        self.bot.follow()


def main():
    insta_tool = Controller(driver_path='driver')
    insta_tool.login()
    insta_tool.scrape_followers()
    insta_tool.follow()


if __name__ == '__main__':
    main()
