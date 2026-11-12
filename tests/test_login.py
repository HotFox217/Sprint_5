from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import (
    AUTH_BUTTON,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
    USER_AVATAR,
    USER_NAME,
)


BASE_URL = "https://qa-desk.education-services.ru/"

USER_EMAIL = "testbest@gmail.com"
USER_PASSWORD = "22882288"


class TestLogin:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_login_success(self):
        self.driver.get(BASE_URL)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(AUTH_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(EMAIL_INPUT)
        ).send_keys(USER_EMAIL)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(PASSWORD_INPUT)
        ).send_keys(USER_PASSWORD)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(LOGIN_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(USER_AVATAR)
        )

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(USER_NAME)
        )

        actual_avatar_visible = self.driver.find_element(
            *USER_AVATAR
        ).is_displayed()
        expected_avatar_visible = True

        assert actual_avatar_visible == expected_avatar_visible

        actual_user_name = self.driver.find_element(*USER_NAME).text
        expected_user_name = "User."

        assert actual_user_name == expected_user_name
