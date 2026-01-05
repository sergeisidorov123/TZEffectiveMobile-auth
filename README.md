Проект использует:

- FastAPI  
- PostgreSQL  
- SQLAlchemy  
- JWT для аутентификации  
- bcrypt для хеширования паролей  

Запуск проекта(требует докер):

1.
```commandline
git clone https://github.com/sergeisidorov123/TZEffectiveMobile-auth
cd TZEffectiveMobile
```

2. Создание .env файла, вот какой использовал я:
```commandline
DEBUG=true

# Database
DB_HOST=postgres
DB_PORT=5432
DB_NAME=tzeffectivemobile
DB_USER=postgres
DB_PASSWORD=postgres

SECRET_KEY=AAAAAAAAAAABBBBBBBB
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Но все будет работать и без него, в конфиге прописаны дефолтные значения.

3. Поднятие контейнеров через Docker compose:
```commandline
docker-compose up --build
```

В init.sql зашиты дефолтные значения ролей и прав для теста

4. API по адресу:
```commandline
http://localhost:8000
```

5. Swagger:
```commandline
http://localhost:8000
```

При тестировании в поле username - нужно вводить email, введенный при регистрации, 
т.к. именно он используется в качестве "юзернейма". В UI сваггера, нет возможности  
поменять поля на ввод данных авторизации