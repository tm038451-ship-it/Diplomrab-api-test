import os
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# Настройка путей для корректного импорта модулей проекта
sys.path.insert(0, os.path.path.abspath(os.path.path.dirname(
    os.path.path.dirname(__file__))))


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    # Инициализация веб-драйвера (например, Chrome)
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
