# tron_info_service

## Запуска проекта


* Клонировать репозиторий и перейти в него

```bash 
git clone https://github.com/licaro-1/tron_info_service.git
cd tron_info_service/
```

* Установить зависимости

```bash 
pip install -r requirements.txt
```

* Залогиниться на https://www.trongrid.io/ и получить API_KEY
* Создать файл .env в корневой директории и указать полученный API ключ в переменную TRON_API_KEY
Пример:

```bash
TRON_API_KEY=68f2319b-10ff-4258-9c5a-e2812
```
* Запустить тесты
```bash
pytest -v
```
* Применить миграции и запустить uvicorn
```bash
alembic upgrade head
python main.py
```
