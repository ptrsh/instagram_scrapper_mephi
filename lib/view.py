from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.progress import track

class View:
    def __init__(self):
        self.console = Console()
        self.prompt = Prompt()
        self.table = Table()
        self.table.add_column("№ команды", style="cyan")
        self.table.add_column("Команда", style="cyan")
        self.table.add_row("    1", "Получить список подписчиков")
        self.table.add_row("    2", "Подписаться")
        self.table.add_row("    3", "Получить список постов")
        self.table.add_row("    4", "Лайкнуть пост(ы)")
        self.table.add_row("    5", "Написать сообщение")
        self.table.add_row("    6", "Выйти из программы")

    def get_command(self):
        return self.prompt.ask("Введите команду", choices=["1", "2", "3", "4", "5", "6"])    

    def get_url(self, message):
        return self.prompt.ask(message, default="Пример: https://www.instagram.com/mephi_official") 

    def get_url_list(self, message, default_file):
        return self.prompt.ask(message, default=f"По умолчанию {default_file}") 

    def print_menu(self):
        self.console.print(self.table)
    
    def login(self):
        self.console.print("Необходимо авторизоваться в Инстаграм!", style="bold")
        username = self.prompt.ask("Введите имя пользователя")    
        password = self.prompt.get_input(self.console, "Введите пароль: ", password=True)
        return username, password

    def presentation(self):
        self.console.rule("InstaTool")

    def track(self, items, message):
        return track(items, description=f'[green]{message}')

    def success(self):
        self.console.print("Операция выполнена успешно!", style="green")

    def error(self):
        self.console.print("Операция не выполнена!", style="red bold")




