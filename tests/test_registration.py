from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import BASE_URL, WAIT_TIMEOUT
from data import (
    EXISTING_USER_EMAIL,
    EXISTING_USER_PASSWORD,
    REGISTRATION_PASSWORD,
    EXPECTED_USER_NAME,
    generate_registration_email,
    generate_invalid_email,
)
from locators import AuthLocators, RegistrationLocators


class TestRegistration:

    def test_registration_success(self, driver):
        email = generate_registration_email()
        password = REGISTRATION_PASSWORD

        driver.get(BASE_URL)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AuthLocators.AUTH_BUTTON
            )
        ).click()

        login_email = WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.EMAIL_INPUT
            )
        )

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                RegistrationLocators.NO_ACCOUNT_BUTTON
            )
        ).click()

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.staleness_of(login_email)
        )

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AuthLocators.EMAIL_INPUT
            )
        ).send_keys(email)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.PASSWORD_INPUT
            )
        ).send_keys(password)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                RegistrationLocators.REPEAT_PASSWORD_INPUT
            )
        ).send_keys(password)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                RegistrationLocators.CREATE_ACCOUNT_BUTTON
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

    def test_registration_invalid_email(self, driver):
        email = generate_invalid_email()
        password = REGISTRATION_PASSWORD

        driver.get(BASE_URL)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AuthLocators.AUTH_BUTTON
            )
        ).click()

        login_email = WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.EMAIL_INPUT
            )
        )

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                RegistrationLocators.NO_ACCOUNT_BUTTON
            )
        ).click()

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.staleness_of(login_email)
        )

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AuthLocators.EMAIL_INPUT
            )
        ).send_keys(email)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.PASSWORD_INPUT
            )
        ).send_keys(password)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                RegistrationLocators.REPEAT_PASSWORD_INPUT
            )
        ).send_keys(password)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                RegistrationLocators.CREATE_ACCOUNT_BUTTON
            )
        ).click()

        assert all((
            WebDriverWait(driver, WAIT_TIMEOUT).until(
                expected_conditions.visibility_of_element_located(
                    RegistrationLocators.EMAIL_ERROR_FIELD
                )
            ).is_displayed(),

            WebDriverWait(driver, WAIT_TIMEOUT).until(
                expected_conditions.visibility_of_element_located(
                    RegistrationLocators.PASSWORD_ERROR_FIELD
                )
            ).is_displayed(),

            WebDriverWait(driver, WAIT_TIMEOUT).until(
                expected_conditions.visibility_of_element_located(
                    RegistrationLocators.REPEAT_PASSWORD_ERROR_FIELD
                )
            ).is_displayed(),

            WebDriverWait(driver, WAIT_TIMEOUT).until(
                expected_conditions.visibility_of_element_located(
                    RegistrationLocators.ERROR_MESSAGE
                )
            ).is_displayed()
        ))

    def test_registration_existing_user(self, driver):
        password = EXISTING_USER_PASSWORD

        driver.get(BASE_URL)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AuthLocators.AUTH_BUTTON
            )
        ).click()

        login_email = WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.EMAIL_INPUT
            )
        )

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                RegistrationLocators.NO_ACCOUNT_BUTTON
            )
        ).click()

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.staleness_of(login_email)
        )

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AuthLocators.EMAIL_INPUT
            )
        ).send_keys(EXISTING_USER_EMAIL)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.PASSWORD_INPUT
            )
        ).send_keys(password)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                RegistrationLocators.REPEAT_PASSWORD_INPUT
            )
        ).send_keys(password)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                RegistrationLocators.CREATE_ACCOUNT_BUTTON
            )
        ).click()

        assert all((
            WebDriverWait(driver, WAIT_TIMEOUT).until(
                expected_conditions.visibility_of_element_located(
                    RegistrationLocators.EMAIL_ERROR_FIELD
                )
            ).is_displayed(),

            WebDriverWait(driver, WAIT_TIMEOUT).until(
                expected_conditions.visibility_of_element_located(
                    RegistrationLocators.PASSWORD_ERROR_FIELD
                )
            ).is_displayed(),

            WebDriverWait(driver, WAIT_TIMEOUT).until(
                expected_conditions.visibility_of_element_located(
                    RegistrationLocators.REPEAT_PASSWORD_ERROR_FIELD
                )
            ).is_displayed(),

            WebDriverWait(driver, WAIT_TIMEOUT).until(
                expected_conditions.visibility_of_element_located(
                    RegistrationLocators.ERROR_MESSAGE
                )
            ).is_displayed()
        ))
