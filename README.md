# Сервис-справочник курса валют

## Базовые технологии проекта

- Python 3.11
- Flask 3
- 
## Инструкция по развертыванию тестового проекта

### Настройка проекта

Склонируйте репозиторий:

```bash
git clone https://github.com/dvkuzmin/currency_catalog.git
```

Создайте виртуальное окружение, затем выполните команду:

```bash
pip install -r requirements.txt
```


Разверните приложение через docker-compose:
```bash
docker-compose up --build
```

Перейдите в терминал контейнера приложения flask и выполните миграции:

```bash
docker ps -a
docker exec -it {имя или номер контейнера} bash
alembic update head
```

Можете переходить к тестированию API

### HTTP API

#### POST
- /tasks - Post-запрос на добавление объекта Task

BODY: {'title': str, 'descrition': str}


#### GET
- /tasks - Get-запрос на получение списка объектов Task
- /tasks/id - Get-запрос на получение объекта Task по его id

#### PUT
- /tasks/id - Put-запрос на обновление объекта Task по id

BODY: {'title': str[Optional] = None,
       'descrition': str[Optional] = None}


#### DELETE
- /tasks/id - Delete-запрос на удаление объекта Task по его id

### Автотесты

В корне проекта запустите команду
```bash
pytest
```
для проведения тестирования