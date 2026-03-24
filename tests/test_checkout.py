from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from config.config import *

def test_checkout(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    checkout = CheckoutPage(page)

    login.navigate(BASE_URL)
    login.login(USERNAME, PASSWORD)

    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    checkout.checkout()

    assert "checkout-complete" in page.url