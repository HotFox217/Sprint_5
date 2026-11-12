from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import (
    AUTH_BUTTON,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
    LOGOUT_BUTTON,
    USER_AVATAR,
    USER_NAME,
)


BASE_URL = "https://qa-desk.education-services.ru/"

USER_EMAIL = "testbest@gmail.com"
USER_PASSWORD = "22882288"


class TestLogout:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_logout_success(self):
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
            expected_conditions.visibility_of_element_located(LOGOUT_BUTTON)
        )

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(LOGOUT_BUTTON)
        ).click()

        actual_avatar_hidden = WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(USER_AVATAR)
        )
        expected_avatar_hidden = True

        assert actual_avatar_hidden == expected_avatar_hidden

        actual_user_name_hidden = WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(USER_NAME)
        )
        expected_user_name_hidden = True

        assert actual_user_name_hidden == expected_user_name_hidden

        actual_auth_button_visible = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(AUTH_BUTTON)
        ).is_displayed()
        expected_auth_button_visible = True

        assert actual_auth_button_visible == expected_auth_button_visible
