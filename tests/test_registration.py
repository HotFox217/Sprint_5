from selenium.common.exceptions import StaleElementReferenceException
from uuid import uuid4
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import (
    AUTH_BUTTON,
    NO_ACCOUNT_BUTTON,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    REPEAT_PASSWORD_INPUT,
    CREATE_ACCOUNT_BUTTON,
    USER_AVATAR,
    USER_NAME,
    ERROR_MESSAGE,
    EMAIL_ERROR_FIELD,
    PASSWORD_ERROR_FIELD,
    REPEAT_PASSWORD_ERROR_FIELD,
)


BASE_URL = "https://qa-desk.education-services.ru/"

EXISTING_USER_EMAIL = "testbest@gmail.com"
EXISTING_USER_PASSWORD = "22882288"


class TestRegistration:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_registration_success(self):
        email = f"autotest_{uuid4().hex[:10]}@mail.ru"
        password = "Test1234!"

        self.driver.get(BASE_URL)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(AUTH_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(NO_ACCOUNT_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(EMAIL_INPUT)
        ).send_keys(email)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(PASSWORD_INPUT)
        ).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(REPEAT_PASSWORD_INPUT)
        ).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)
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

    def test_registration_invalid_email(self):
        email = f"invalid_{uuid4().hex[:10]}"
        password = "Test1234!"

        self.driver.get(BASE_URL)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(AUTH_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(NO_ACCOUNT_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(EMAIL_INPUT)
        ).send_keys(email)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(PASSWORD_INPUT)
        ).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(REPEAT_PASSWORD_INPUT)
        ).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(ERROR_MESSAGE)
        )

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(EMAIL_ERROR_FIELD)
        )

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(PASSWORD_ERROR_FIELD)
        )

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                REPEAT_PASSWORD_ERROR_FIELD
            )
        )

        actual_email_error = self.driver.find_element(
            *EMAIL_ERROR_FIELD
        ).is_displayed()
        expected_email_error = True

        actual_password_error = self.driver.find_element(
            *PASSWORD_ERROR_FIELD
        ).is_displayed()
        expected_password_error = True

        actual_repeat_password_error = self.driver.find_element(
            *REPEAT_PASSWORD_ERROR_FIELD
        ).is_displayed()
        expected_repeat_password_error = True

        actual_error_message = self.driver.find_element(*ERROR_MESSAGE).text
        expected_error_message = "Ошибка"

        assert actual_email_error == expected_email_error
        assert actual_password_error == expected_password_error
        assert actual_repeat_password_error == expected_repeat_password_error
        assert actual_error_message == expected_error_message

    def test_registration_existing_user(self):
        email = EXISTING_USER_EMAIL
        password = EXISTING_USER_PASSWORD

        self.driver.get(BASE_URL)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(AUTH_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(NO_ACCOUNT_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(EMAIL_INPUT)
        ).send_keys(email)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(PASSWORD_INPUT)
        ).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(REPEAT_PASSWORD_INPUT)
        ).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(ERROR_MESSAGE)
        )

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(EMAIL_ERROR_FIELD)
        )

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(PASSWORD_ERROR_FIELD)
        )

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                REPEAT_PASSWORD_ERROR_FIELD
            )
        )

        actual_email_error = self.driver.find_element(
            *EMAIL_ERROR_FIELD
        ).is_displayed()
        expected_email_error = True

        actual_password_error = self.driver.find_element(
            *PASSWORD_ERROR_FIELD
        ).is_displayed()
        expected_password_error = True

        actual_repeat_password_error = self.driver.find_element(
            *REPEAT_PASSWORD_ERROR_FIELD
        ).is_displayed()
        expected_repeat_password_error = True

        actual_error_message = self.driver.find_element(*ERROR_MESSAGE).text
        expected_error_message = "Ошибка"

        assert actual_email_error == expected_email_error
        assert actual_password_error == expected_password_error
        assert actual_repeat_password_error == expected_repeat_password_error
        assert actual_error_message == expected_error_message
