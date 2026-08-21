from selenium.webdriver.common.by import By
from config import SAUCEDEMO_URL


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Локаторы элементов страницы (Заданы стандартным способом через By)
        self.USERNAME_INPUT = (By.ID, "user-name")
        self.PASSWORD_INPUT = (By.ID, "password")
        self.LOGIN_BUTTON = (By.ID, "login-button")

        # ВНИМАНИЕ: Локатор для баг-репорта BUG-UI-01
        # Будет проверять наличие сообщения об ошибке при блокировке
        self.ERROR_CONTAINER = (By.CSS_SELECTOR, '[data-test="error"]')

    def open(self):
        """Открывает страницу авторизации Saucedemo."""
        self.driver.get(SAUCEDEMO_URL)

    def login(self, username, password):
        """Выполняет полный цикл авторизации пользователя."""
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message_text(self):
        """Возвращает текст ошибки при неудачном входе."""
        return self.driver.find_element(*self.ERROR_CONTAINER).text
