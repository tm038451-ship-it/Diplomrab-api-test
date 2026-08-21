from Pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_locked_out_user(driver) -> None:
    """TC-UI-01: Негативный логин заблокированного пользователя"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    error_text: str = login_page.get_error_message_text()
    assert "Epic sadface: Sorry, this user has been locked out." in error_text


def test_positive_login(driver) -> None:
    """TC-UI-02: Позитивный логин стандартного пользователя"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url


def test_add_product_to_cart(driver) -> None:
    """TC-UI-03: Добавление товара в корзину"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Добавляем рюкзак в корзину
    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    badge = driver.find_element("class name", "shopping_cart_badge")
    assert badge.text == "1"


def test_remove_product_from_cart(driver) -> None:
    """TC-UI-04: Удаление товара из корзины"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Ждем кнопку добавления и кликаем
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()

    # Ждем кнопку удаления и кликаем
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
    ).click()

    # Проверяем, что счетчик на иконке корзины исчез
    badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(badges) == 0


def test_navigate_to_checkout(driver) -> None:
    """TC-UI-05: Переход на страницу оформления заказа"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Переходим в саму корзину и кликаем на кнопку Checkout
    driver.find_element("class name", "shopping_cart_link").click()
    driver.find_element("id", "checkout").click()

    assert "checkout-step-one.html" in driver.current_url
