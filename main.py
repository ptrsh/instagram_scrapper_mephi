import sys
from driver import Controller


def main():
    insta_tool = Controller()
    insta_tool.selenium.driver.implicitly_wait(3)
    insta_tool.login(login, password)

if __name__ == '__main__':
    main()
