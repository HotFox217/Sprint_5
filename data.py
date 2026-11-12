from uuid import uuid4


EXISTING_USER_EMAIL = "testbest@gmail.com"
EXISTING_USER_PASSWORD = "22882288"


ADVERTISEMENT_USER_EMAIL = "testakyla@gmail.com"
ADVERTISEMENT_USER_PASSWORD = "qwerty123"


REGISTRATION_PASSWORD = "Test1234!"


def generate_registration_email():
    return f"autotest_{uuid4().hex[:10]}@mail.ru"


def generate_invalid_email():
    return f"invalid_{uuid4().hex[:10]}"


ADVERTISEMENT_DESCRIPTION = "Тестовое описание объявления"
ADVERTISEMENT_PRICE = "5555"


def generate_advertisement_name():
    return f"Автотестовая крутая книга {uuid4().hex[:8]}"


EXPECTED_USER_NAME = "User."