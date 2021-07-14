# Описание
Решение тестового задания для Xsolla Summer School 2021 на направление [back-end](https://github.com/xsolla/xsolla-school-backend-2021)

Solving the Xsolla Summer School 2021 Test Assignment on [back-end](https://github.com/xsolla/xsolla-school-backend-2021)

# Что реализовано

* API-методы для управлениями товарами - [операции CRUD](https://ru.wikipedia.org/wiki/CRUD)
* Фильтрация товаров по их типу и стоимости в методе получения каталога товаров.

# Требования
* python v3.x
* django v3.2.5
* djangorestframework v3.12.4
* djoser v2.1.0
* uritemplate v3.0.1


Для установки django и djangorestframework, djoser, uritemplate использовать: `pip install django==3.2.5` `pip install djangorestframework==3.12.4` `pip install djoser==2.1.0` `pip install pyyaml uritemplate==3.0.1`

# Запуск
В папке с файлом *manage.py* выполнить команду: `python manage.py runserver`. Приложение будет запущено по адресу http://localhost:8000/.

# API
* OpenAPI-спецификация API, предоставляемого сервером, доступна по адресу https://localhost:8000/api/v1/demoApi/openapi/

# Доступные пользователи (логин, пароль):
* admin, admin
