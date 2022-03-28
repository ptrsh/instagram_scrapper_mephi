import sys
from driver import Controller


def main():
    insta_tool = Controller()
    insta_tool.selenium.driver.implicitly_wait(3)
    login = sys.argv[1]
    password = sys.argv[2]
    insta_tool.login(login, password)
    #insta_tool.follow(follow_url)
    #insta_tool.like(like_url)
    print('Exiting...')

if __name__ == '__main__':
    main()
