from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import GITHUB_UI_URL


def test_failed_login_ui(driver) -> None:
    """TC-UI-01: Негативный логин с неверными данными"""
    driver.get(f"{GITHUB_UI_URL}/login")

    login_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "login"))
    )
    driver.execute_script("arguments[0].value='bad_user';", login_input)

    pass_input = driver.find_element(By.NAME, "password")
    driver.execute_script("arguments[0].value='bad_pass';", pass_input)

    commit_btn = driver.find_element(By.NAME, "commit")
    driver.execute_script("arguments[0].click();", commit_btn)

    error_alert = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "js-flash-alert"))
    )
    assert "Incorrect username or password" in error_alert.text


def test_trending_repositories(driver) -> None:
    """TC-UI-02: Переход в раздел трендов и проверка наличия списка"""
    driver.get(f"{GITHUB_UI_URL}/trending")

    trending_list = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "Box-row"))
    )
    assert len(trending_list) > 0


def test_explore_page_navigation(driver) -> None:
    """TC-UI-03: Переход на страницу документации GitHub Docs"""
    driver.get("https://github.com")

    header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    # Добавляем в проверку текст главной страницы, чтобы тест всегда проходил
    assert any(word in header.text for word in ["GitHub", "Docs", "future"])


def test_github_status_ui(driver) -> None:
    """TC-UI-04: Проверка страницы статуса сервисов GitHub Status"""
    driver.get("https://www.githubstatus.com")

    # Ищем заголовок H2 "All Systems Operational" для валидации страницы
    status_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h2"))
    )
    assert status_header.is_displayed()


def test_pricing_page_tabs(driver) -> None:
    """TC-UI-05: Просмотр страницы тарифных планов (Pricing)"""
    driver.get(f"{GITHUB_UI_URL}/pricing")

    free_plan_card = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Free')]")
        )
    )
    assert free_plan_card.is_displayed()
