from pages.cart_page import CartPage


def test_add_to_card(browser_set):
    cart_page = CartPage()

    cart_page.open()

    cart_page.open_menu_tab()
    cart_page.open_mp3_tab()
    cart_page.open_page_2()
    cart_page.open_macbook_product()
    cart_page.add_product_to_cart()
    cart_page.open_menu_tab()
    cart_page.open_mp3_tab()
    cart_page.open_page_2()
    cart_page.open_hp_lp3065_product()
    cart_page.add_product_to_cart()
