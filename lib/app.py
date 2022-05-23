from controller import Controller


class Application:
    
    def __init__(self):
        self.controller = Controller()

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

    def func_5(self):
        self.controller.write_message()

    def func_6(self):
        exit(0)
        



