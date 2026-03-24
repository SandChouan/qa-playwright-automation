from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import *

def test_add_to_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.navigate(BASE_URL)
    login.login(USERNAME, PASSWORD)

    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    assert "cart" in page.url