from uuid import uuid4
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import (
    PLACE_ADVERTISEMENT_BUTTON,
    AUTHORIZATION_REQUIRED_TITLE,
    AUTH_BUTTON,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
    LOGOUT_BUTTON,
    ADVERTISEMENT_NAME_INPUT,
    ADVERTISEMENT_CATEGORY_ARROW,
    ADVERTISEMENT_CATEGORY_BOOKS,
    ADVERTISEMENT_CONDITION_USED_CONTROL,
    ADVERTISEMENT_CONDITION_USED_ACTIVE,
    ADVERTISEMENT_CITY_ARROW,
    ADVERTISEMENT_CITY_MOSCOW,
    ADVERTISEMENT_DESCRIPTION_INPUT,
    ADVERTISEMENT_PRICE_INPUT,
    PUBLISH_BUTTON,
    MY_ADVERTISEMENTS_TITLE,
    MY_ADVERTISEMENT_TITLES,
)


BASE_URL = "https://qa-desk.education-services.ru/"

USER_EMAIL = "testbest@gmail.com"
USER_PASSWORD = "22882288"


class TestAdvertisement:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_unauthorized_user_cannot_create_advertisement(self):
        self.driver.get(BASE_URL)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                PLACE_ADVERTISEMENT_BUTTON
            )
        ).click()

        actual_title = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                AUTHORIZATION_REQUIRED_TITLE
            )
        ).text

        expected_title = "Чтобы разместить объявление, авторизуйтесь"

        assert actual_title == expected_title

    def test_authorized_user_creates_advertisement(self):
        advertisement_name = f"Автотестовая крутая книга {uuid4().hex[:8]}"
        description = "Тестовое описание объявления"
        price = "5555"

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
            expected_conditions.visibility_of_element_located(
                LOGOUT_BUTTON
            )
        )

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                PLACE_ADVERTISEMENT_BUTTON
            )
        ).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                ADVERTISEMENT_NAME_INPUT
            )
        ).send_keys(advertisement_name)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                ADVERTISEMENT_CATEGORY_ARROW
            )
        ).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                ADVERTISEMENT_CATEGORY_BOOKS
            )
        ).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                ADVERTISEMENT_CONDITION_USED_CONTROL
            )
        ).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                ADVERTISEMENT_CONDITION_USED_ACTIVE
            )
        )

        actual_condition_selected = self.driver.find_element(
            *ADVERTISEMENT_CONDITION_USED_ACTIVE
        ).is_displayed()

        expected_condition_selected = True

        assert actual_condition_selected == expected_condition_selected



        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                ADVERTISEMENT_CITY_ARROW
            )
        ).click()


        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                ADVERTISEMENT_CITY_MOSCOW
            )
        ).click()


        description_elements = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_any_elements_located(
                ADVERTISEMENT_DESCRIPTION_INPUT
            )
        )

        description_elements[0].send_keys(description)


        price_elements = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_any_elements_located(
                ADVERTISEMENT_PRICE_INPUT
            )
        )

        price_elements[0].send_keys(price)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(PUBLISH_BUTTON)
        ).click()

        self.driver.get(f"{BASE_URL}profile")

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                MY_ADVERTISEMENTS_TITLE
            )
        )

        WebDriverWait(self.driver, 10).until(
            lambda driver: advertisement_name in [
                element.text.strip()
                for element in driver.find_elements(
                    *MY_ADVERTISEMENT_TITLES
                )
            ]
        )

        actual_advertisement_titles = [
            element.text.strip()
            for element in self.driver.find_elements(
                *MY_ADVERTISEMENT_TITLES
            )
        ]

        assert advertisement_name in actual_advertisement_titles