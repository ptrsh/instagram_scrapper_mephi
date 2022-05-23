from controller import Controller


class Application:
    def __init__(self, mode):
        self.controller = Controller(mode)

    def start(self):
        self.controller.login()
        while True:
            self.controller.view.print_menu()
            command = self.controller.view.get_command()
            getattr(self, f'func_{command}')()

    def func_1(self):
        self.controller.scrape_followers()

    def func_2(self):
        self.controller.follow()

    def func_3(self):
        self.controller.get_posts()

    def func_4(self):
        self.controller.like()

    @staticmethod
    def func_5():
        exit(0)
