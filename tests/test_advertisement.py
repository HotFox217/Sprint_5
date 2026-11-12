from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import BASE_URL, PROFILE_URL, WAIT_TIMEOUT
from data import (
    ADVERTISEMENT_USER_EMAIL,
    ADVERTISEMENT_USER_PASSWORD,
    ADVERTISEMENT_DESCRIPTION,
    ADVERTISEMENT_PRICE,
    generate_advertisement_name,
)
from locators import AuthLocators, AdvertisementLocators


class TestAdvertisement:

    def test_unauthorized_user_cannot_create_advertisement(self, driver):
        driver.get(BASE_URL)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AdvertisementLocators.PLACE_ADVERTISEMENT_BUTTON
            )
        ).click()

        assert WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AdvertisementLocators.AUTHORIZATION_REQUIRED_TITLE
            )
        ).is_displayed()

    def test_authorized_user_selects_used_condition(self, driver):
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
        ).send_keys(ADVERTISEMENT_USER_EMAIL)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.PASSWORD_INPUT
            )
        ).send_keys(ADVERTISEMENT_USER_PASSWORD)

        login_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AuthLocators.LOGIN_BUTTON
            )
        )
        login_button.click()

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.invisibility_of_element_located(
                AuthLocators.LOGIN_BUTTON
            )
        )

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.USER_AVATAR
            )
        )

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AdvertisementLocators.PLACE_ADVERTISEMENT_BUTTON
            )
        ).click()

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AdvertisementLocators.ADVERTISEMENT_CATEGORY_ARROW
            )
        ).click()

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AdvertisementLocators.ADVERTISEMENT_CATEGORY_BOOKS
            )
        ).click()

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AdvertisementLocators.ADVERTISEMENT_CONDITION_USED_CONTROL
            )
        ).click()

        assert WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AdvertisementLocators.ADVERTISEMENT_CONDITION_USED_ACTIVE
            )
        ).is_displayed()

    def test_authorized_user_creates_advertisement(self, driver):
        advertisement_name = generate_advertisement_name()

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
        ).send_keys(ADVERTISEMENT_USER_EMAIL)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.PASSWORD_INPUT
            )
        ).send_keys(ADVERTISEMENT_USER_PASSWORD)

        login_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AuthLocators.LOGIN_BUTTON
            )
        )
        login_button.click()

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.invisibility_of_element_located(
                AuthLocators.LOGIN_BUTTON
            )
        )

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.USER_AVATAR
            )
        )

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AdvertisementLocators.PLACE_ADVERTISEMENT_BUTTON
            )
        ).click()

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AdvertisementLocators.ADVERTISEMENT_NAME_INPUT
            )
        ).send_keys(advertisement_name)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AdvertisementLocators.ADVERTISEMENT_CATEGORY_ARROW
            )
        ).click()

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AdvertisementLocators.ADVERTISEMENT_CATEGORY_BOOKS
            )
        ).click()

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AdvertisementLocators.ADVERTISEMENT_CONDITION_USED_CONTROL
            )
        ).click()

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AdvertisementLocators.ADVERTISEMENT_CONDITION_USED_ACTIVE
            )
        )

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AdvertisementLocators.ADVERTISEMENT_CITY_ARROW
            )
        ).click()

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AdvertisementLocators.ADVERTISEMENT_CITY_MOSCOW
            )
        ).click()

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.text_to_be_present_in_element_value(
                AdvertisementLocators.ADVERTISEMENT_CITY_DROPDOWN,
                "Москва"
            )
        )

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AdvertisementLocators.ADVERTISEMENT_DESCRIPTION_INPUT
            )
        ).send_keys(ADVERTISEMENT_DESCRIPTION)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AdvertisementLocators.ADVERTISEMENT_PRICE_INPUT
            )
        ).send_keys(ADVERTISEMENT_PRICE)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.text_to_be_present_in_element_value(
                AdvertisementLocators.ADVERTISEMENT_PRICE_INPUT,
                ADVERTISEMENT_PRICE
            )
        )

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                AdvertisementLocators.PUBLISH_BUTTON
            )
        ).click()

        driver.get(PROFILE_URL)

        assert WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                AdvertisementLocators.advertisement_title(
                    advertisement_name
                )
            )
        ).is_displayed()
