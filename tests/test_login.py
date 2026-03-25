#from pages.login_page import LoginPage
#from config.config import BASE_URL, USERNAME, PASSWORD
#def test_login(page):
   # login = LoginPage(page)

    #login.navigate(BASE_URL)
    #login.login(USERNAME, PASSWORD)

    #assert "inventory" in page.url

import pytest

from utils.data_loader import load_test_data


def test_login_success(page, login_page):
    # Load test data
    data = load_test_data()

    # Perform login
    login_page.login(
        data["login"]["username"],
        data["login"]["password"]
    )

    # Verify successful login (URL contains inventory page)
    assert "inventory" in page.url


def test_login_failed(page, login_page):
    # Load test data
    data = load_test_data()

    # Perform login with invalid password
    login_page.login(
        data["login"]["username"],
        "wrong_password"
    )

    # Verify error message is displayed
    error_message = page.locator('[data-test="error"]')
    assert error_message.is_visible()