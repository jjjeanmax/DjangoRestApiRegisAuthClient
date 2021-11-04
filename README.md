# DjangoRestApiRegisAuthClient
Django RestApi Для Авторизации и регистрации клиента

Django REST - API, с методами:
- Авторизация и регистрация клиента
- Просмотр и редактирование персональной информации (имя, фамилия, адрес, фотография)
- Выход из ситсемы.

## Старт

1. Создать и активировать виртуальное окружение:

    `python -m venv venv`

2. Установить пакеты:

    `pip install -r requirements.txt`

3. Выполнить команду для выполнения миграций :

    `python manage.py migrate`

4. Создать статичные файлы: 

    `python manage.py collectstatic`

5. Создать суперпользователя:

    `python manage.py createsuperuser`


7. Запустить сервер:

    `$ python manage.py runserver`
