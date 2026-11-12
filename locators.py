from selenium.webdriver.common.by import By


AUTH_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")

NO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']")

EMAIL_INPUT = (By.NAME, "email")

PASSWORD_INPUT = (By.NAME, "password")

REPEAT_PASSWORD_INPUT = (By.NAME, "submitPassword")

CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")

USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")

USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")

ERROR_MESSAGE = (By.XPATH, ".//span[text()='Ошибка']")

EMAIL_ERROR_FIELD = (
    By.XPATH,
    ".//input[@name='email']/parent::div[contains(@class, 'input_inputError')]"
)

PASSWORD_ERROR_FIELD = (
    By.XPATH,
    ".//input[@name='password']/parent::div[contains(@class, 'input_inputError')]"
)

REPEAT_PASSWORD_ERROR_FIELD = (
    By.XPATH,
    ".//input[@name='submitPassword']/parent::div[contains(@class, 'input_inputError')]"
)

LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")

AUTHORIZATION_REQUIRED_TITLE = (
    By.XPATH,
    ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']"
)

PLACE_ADVERTISEMENT_BUTTON = (
    By.XPATH,
    ".//button[text()='Разместить объявление']"
)

ADVERTISEMENT_NAME_INPUT = (By.NAME, "name")

ADVERTISEMENT_CATEGORY_DROPDOWN = (By.NAME, "category")

ADVERTISEMENT_CATEGORY_ARROW = (
    By.XPATH,
    ".//input[@name='category']/following-sibling::button"
)

ADVERTISEMENT_CATEGORY_BOOKS = (
    By.XPATH,
    ".//button[span[text()='Книги']]"
)

ADVERTISEMENT_CITY_DROPDOWN = (By.NAME, "city")

ADVERTISEMENT_CITY_ARROW = (
    By.XPATH,
    ".//input[@name='city']/following-sibling::button"
)

ADVERTISEMENT_CITY_MOSCOW = (
    By.XPATH,
    ".//button[span[text()='Москва']]"
)

ADVERTISEMENT_CONDITION_USED = (
    By.XPATH,
    ".//div[contains(@class, 'radioUnput_shell')][.//input[@name='condition' and @value='Б/У']]"
)

ADVERTISEMENT_CONDITION_USED_LABEL = (
    By.XPATH,
    ".//div[contains(@class, 'radioUnput_shell')][.//input[@name='condition' and @value='Б/У']]//label[normalize-space()='Б/У']"
)

ADVERTISEMENT_CONDITION_USED_INPUT = (
    By.XPATH,
    ".//input[@name='condition' and @value='Б/У']"
)

ADVERTISEMENT_CONDITION_USED_CONTROL = (
    By.XPATH,
    ".//div[contains(@class, 'radioUnput_shell')][.//input[@name='condition' and @value='Б/У']]//div[contains(@class, 'radioUnput_inputRegular')]"
)

ADVERTISEMENT_CONDITION_USED_ACTIVE = (
    By.XPATH,
    ".//div[contains(@class, 'radioUnput_shell')][.//input[@name='condition' and @value='Б/У']]//div[contains(@class, 'radioUnput_inputActive')]"
)

ADVERTISEMENT_DESCRIPTION_INPUT = (By.NAME, "description")

ADVERTISEMENT_PRICE_INPUT = (By.NAME, "price")

PUBLISH_BUTTON = (By.XPATH, ".//button[text()='Опубликовать']")

MY_ADVERTISEMENTS_TITLE = (
    By.XPATH,
    ".//h1[text()='Мои объявления']"
)

MY_ADVERTISEMENT_TITLES = (
    By.CSS_SELECTOR,
    "div.description div.about h2.h2"
)
