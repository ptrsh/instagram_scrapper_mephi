import sys
from driver import Controller


def main():
    insta_tool = Controller()
    insta_tool.selenium.driver.implicitly_wait(3)
    login = "superusername2022"
    password = "superpassword2022"
    insta_tool.login(login, password)
    #insta_tool.follow("https://www.instagram.com/s1mpleo/")
    #urls = ["https://www.instagram.com/p/CZC0mWnNDQu/", "https://www.instagram.com/p/CYJngNlt6qD/", "https://www.instagram.com/p/CV_eUt1NV6n/"]
    #insta_tool.like_posts(urls)
    test = insta_tool.scrape_followers("https://www.instagram.com/krasnopolskaya1980/")
    for i in test:
        print(i)

if __name__ == '__main__':
    main()
