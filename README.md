# InstaTool

### Программа, которая позволит автоматизировать выполнение некоторых действий в социальной сети Instagram


#### Установка:

* Клонируйте репозиторий
```
git clone https://github.com/ptrsh/instagram_scrapper_mephi.git
```

* Перейдите в рабочую папку
```
cd instagram_scrapper_mephi
```

* Активируйте виртуальное окружение
```
python -m venv venv
source venv/bin/activate
```

* Установите зависимости
```
pip install -r requirements.txt
```

#### Использование:

* Запустите программу с флагом debug, если хотите наблюдать за ходом работы программы
```
python main.py debug
```

* Или используйте флаг release, тогда действия будут выполняться в фоне
```
python main.py release
```

