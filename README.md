# проверка уроков и информирование через ТГ бота

[TODO: Бот отслеживает отправленные на проверку уроки и присылает уведомления о результатах данной проверки]

### Как установить

Python3 должен быть установлен.
Затем используйте 'pip' (или 'pip3'если есть конфликт с Python2) для установки зависимостей:

```
pip install -r requiriments.txt
```

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

### Пример выполнения программы

запуск 

```bash
python3 main.py 654213745
```

Принимает обязательный аргумент: 
* chat id, - id вашего чата с ботом.

Выводит информацию в табличной форме о средней зарплате и количестве просмотренных вакансий в разрезе указанных языков программирования на HeadHunter (г.Москва).




### Настройка окружения

Перед запуском необходимо создать файл ```.env``` и внести в него переменные:
1. `DVMN_TOKEN` с вашим кодом авторизации на сайте [dvmn.org](https://dvmn.org/)
2. `TG_TOKEN` с токеном вашего бота

### Цель проекта

Проект написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
