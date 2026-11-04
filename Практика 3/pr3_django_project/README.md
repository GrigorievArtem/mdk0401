# Практическая работа № 3 — установка окружения и первый запуск

Проект подготовлен по загруженному заданию: Windows, VS Code, Django 5.1.4,
PostgreSQL, Redis/Memurai, пользовательская модель и справочники Location,
Category, Vendor, Model с регистрацией в Django Admin.

## 1. Что входит в проект

- `config/` — настройки Django, маршруты, WSGI/ASGI.
- `apps/accounts/` — пользовательская модель на базе `AbstractUser` и админка.
- `apps/catalog/` — модели справочников и их регистрация в админке.
- `.env.example` — пример переменных окружения.
- `requirements.txt` — версии библиотек из задания.
- `.gitignore` — исключения для Git.

## 2. Требования

Установите Python, PostgreSQL и Memurai Developer. Для PostgreSQL создайте
пользователя/пароль `postgres` либо укажите свои параметры в `.env`.
Memurai по умолчанию слушает порт `6379`.

## 3. Запуск в Windows PowerShell

Откройте папку проекта в VS Code и выполните в терминале:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
Copy-Item .env.example .env
```

Откройте `.env` и укажите пароль PostgreSQL. Сгенерируйте секретный ключ:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Скопируйте результат в значение `SECRET_KEY` файла `.env`.

## 4. Создание базы PostgreSQL

В терминале PostgreSQL выполните (имя базы `ams`):

```sql
CREATE DATABASE ams;
```

Если команда `psql` не находится, добавьте каталог `bin` вашей установки
PostgreSQL в PATH. В задании показан пример пути для PostgreSQL 18.

## 5. Миграции и первый запуск

```powershell
python manage.py makemigrations accounts catalog
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Откройте `http://127.0.0.1:8000/admin/` и войдите под созданным суперпользователем.

## 6. Заполнение справочников

В админ-панели последовательно добавьте:
1. Локацию (например, «Главный склад»).
2. Категорию (например, «Комплектующие»).
3. Поставщика (например, «ООО Поставщик»).
4. Модель, выбрав созданные категорию, поставщика и локацию.

## 7. Redis / Memurai

Проверьте, что служба Memurai запущена и доступна на `127.0.0.1:6379`.
Настройка кэша уже добавлена в `config/settings.py`. Если Redis/Memurai
не установлен или не запущен, операции кэширования могут выдавать ошибку;
для полного выполнения задания запустите службу.

## 8. VS Code Debug (необязательно)

Создайте `.vscode/launch.json` со следующим содержимым:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Django",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["runserver"],
      "django": true,
      "justMyCode": true
    }
  ]
}
```

## 9. Git

```powershell
git init
git add .
git commit -m "Практическая работа №3: начальная настройка Django"
```

## 10. Контрольный список

- [ ] Виртуальное окружение создано и активировано.
- [ ] Зависимости установлены из `requirements.txt`.
- [ ] PostgreSQL доступен, база `ams` создана.
- [ ] Memurai запущен на порту 6379.
- [ ] `.env` заполнен, секретный ключ заменён.
- [ ] Миграции применены без ошибок.
- [ ] Суперпользователь создан.
- [ ] Сервер открывается по адресу `http://127.0.0.1:8000/`.
- [ ] В админке доступны User, Location, Category, Vendor и Model.
- [ ] Справочники заполнены тестовыми данными.

**Важно:** это исходный учебный проект. Его запуск и подключение к вашей локальной
установке PostgreSQL/Memurai выполняются на вашем компьютере; параметры доступа
и секретный ключ индивидуальны и не включены в архив.
