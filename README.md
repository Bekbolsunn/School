<h2 align="center">Task "School""</h2>

### Инструменты разработки

**Стек:**

- Python >= 3.9
- Django Rest Framework
- Postgres
- SimpleJWT

## Старт

##### 1) .env

    # Data Base
    SECRET_KEY=django-insecure-xsk(9whxpb1taa92t(op&)s2@y_=6=aw51ky0+lf%)6iqvz=#6
    DEBUG=True
    DB_NAME=school_db
    DB_USER=master
    DB_PASSWORD=master123
    DB_HOST=localhost
    DB_PORT=5432

    "Я не успел подключить почту"
    # Email
    DEFAULT_FROM_EMAIL=your@your.com  !
    EMAIL_USE_TLS=True                !
    EMAIL_HOST=your_smtp              !
    EMAIL_HOST_USER=your@your.com     !
    EMAIL_HOST_PASSWORD=pass          !
    EMAIL_PORT=587                    !

#### 2) Создать образ

    docker-compose build

##### 3) Запустить контейнер

    docker-compose up

##### 4) Перейти по адресу

    http://127.0.0.1:8000/
