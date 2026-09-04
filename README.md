markdown# Homework Automated Testing Project (Diplomrab-api-test)

Проект автоматизации тестирования UI (Saucedemo) и API (GitHub API) с использованием Python, Pytest, Selenium, Requests и Allure-отчетов.

## 📁 Структура проекта

```text
homework_project/
│
├── config.py              # Конфигурация, чтение токенов и URL
├── requirements.txt       # Список всех библиотек проекта
├── .gitignore             # Исключение мусорных файлов из Git
├── README.md              # Инструкция по запуску и описание дефектов
│
├── pages/                 # Паттерн Page Object для UI-тестов
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
└── tests/                 # Папка с тестами
    ├── __init__.py
    ├── conftest.py        # Общие фикстуры (driver, сессия API)
    ├── test_ui_shop.py    # 5 UI автотестов (Saucedemo)
    └── test_api_github.py # 5 API автотестов (GitHub)
```

## 🛠️ Требования и установка

1. Клонируйте репозиторий и перейдите в корневую папку проекта.
2. Установите необходимые библиотеки и зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Для работы API-тестов установите ваш личный GitHub токен в переменные окружения:
   * **Windows (cmd):** `set GITHUB_TOKEN=ваш_токен`
   * **Linux / macOS / Git Bash:** `export GITHUB_TOKEN="ваш_токен"`

## 🚀 Запуск тестов

* **Запуск всей коллекции тестов:**
  ```bash
  pytest
  ```
* **Запуск только UI автотестов (Saucedemo):**
  ```bash
  pytest tests/test_ui_shop.py
  ```
* **Запуск только API автотестов (GitHub API):**
  ```bash
  pytest tests/test_api_github.py
  ```
* **Запуск тестов сбором результатов для Allure-отчета:**
  ```bash
  pytest --alluredir=allure-results
  ```
* **Просмотр локального Allure-отчета после прогона:**
  ```bash
  allure serve allure-results
  ```

## 📋 Смоделированные дефекты (Bug Tracking)

Автотесты в данном проекте настроены на выявление 10 смоделированных критических дефектов интеграции. При обнаружении этих несоответствий тесты будут падать, генерируя баг-репорт в Allure.

### 🛍️ Дефекты UI (Saucedemo)
* **BUG-UI-01:** Ошибка авторизации заблокированного пользователя на `login_page.py` не содержит обязательный атрибут `data-test="error"`.
* **BUG-UI-02:** Сортировка товаров по цене `Price (low to high)` на `inventory_page.py` некорректно сортирует элементы как строки вместо чисел.
* **BUG-UI-03:** Изображение товара "Sauce Labs Backpack" на главной странице возвращает ошибку 404 (битая ссылка).
* **BUG-UI-04:** При удалении товара кнопкой "Remove" на `cart_page.py` счетчик на иконке корзины не уменьшается.
* **BUG-UI-05:** Поле ввода "Zip/Postal Code" на `checkout_page.py` уязвимо к XSS-инъекциям (отсутствует валидация спецсимволов).

### 🐙 Дефекты API (GitHub API)
* **BUG-API-01:** Эндпоинт `POST /user/repos` при создании репозитория с пустым именем возвращает код `201 Created` вместо `422 Unprocessable Entity`.
* **BUG-API-02:** Запрос приватного репозитория без токена авторизации через `GET /repos/{owner}/{repo}` ошибочно возвращает статус `404 Not Found` вместо `401 Unauthorized`.
* **BUG-API-03:** При обновлении описания через `PATCH /repos/{owner}/{repo}` заголовок ответа `Content-Type` равен `text/html`, а не `application/json`.
* **BUG-API-04:** Попытка удаления несуществующего репозитория `DELETE /repos/{owner}/{repo}` приводит к падению сервера со статусом `500 Internal Server Error` вместо `404`.
* **BUG-API-05:** Параметр пагинации 
`per_page=1` в эндпоинте 
`GET /user/repos`.
