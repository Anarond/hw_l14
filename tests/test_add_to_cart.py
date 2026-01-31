from pages.cart_page import CartPage


def test_add_to_card(browser_set):
    cart_page = CartPage()

    cart_page.open()

    cart_page.click_electronics_tab()
    cart_page.click_cell_phones_tab()
    cart_page.add_iphone_to_cart()
    cart_page.add_nokia_to_cart()
    cart_page.click_books_tab()
    cart_page.add_fahrenheit_to_cart()
    cart_page.click_jewelry_tab()
    cart_page.add_bracelet_to_cart()
    cart_page.open_cart()