from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import BASE_URL, WAIT_TIMEOUT
from data import (
    EXISTING_USER_EMAIL,
    EXISTING_USER_PASSWORD,
    EXPECTED_USER_NAME,
)
from locators import AuthLocators


class TestLogin:

    def test_login_success(self, driver):
        driver.get(BASE_URL)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AuthLocators.AUTH_BUTTON
            )
        ).click()

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.EMAIL_INPUT
            )
        ).send_keys(EXISTING_USER_EMAIL)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.PASSWORD_INPUT
            )
        ).send_keys(EXISTING_USER_PASSWORD)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AuthLocators.LOGIN_BUTTON
            )
        ).click()

        assert WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.USER_AVATAR
            )
        ).is_displayed()

        assert WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.USER_NAME
            )
        ).text == EXPECTED_USER_NAME
