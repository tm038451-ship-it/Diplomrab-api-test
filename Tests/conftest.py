import os
import sys
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 1. Сначала настраиваем пути для импорта, чтобы Python видел корень проекта
root_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.insert(0, root_dir)

# 2. И только ПОСЛЕ этого импортируем токен из config
from config import GITHUB_TOKEN  # noqa: E402


@pytest.fixture(scope="function")
def driver():
    """Фикстура для UI-тестов (Selenium)"""
    options = Options()
    options.add_argument("--headless=new")

    # Добавляем реальный User-Agent, чтобы GitHub не выдавал капчу боту
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    # Отключение автоматизации для обхода базовой защиты
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def api_session():
    """Фикстура для API-тестов (Requests)"""
    session = requests.Session()
    session.headers.update({
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    })
    yield session
    session.close()
