from selene import browser
import allure


class CartPage:
    def __init__(self):
        self.menu_tab = browser.element('#entry_217832')
        self.mp3_tab = browser.element('#widget-navbar-217841 .navbar-nav .nav-item a[href*="path=34"]')
        self.macbook_product = browser.element('[data-id="212408"] #mz-product-grid-image-60-212408')
        self.add_product_to_cart_button = browser.element('#entry_216842')
        self.page_2 = browser.element('ul.pagination li.page-item a[href*="page=2"]')
        self.hp_lp3065_product = browser.element('[data-id="212408"] #mz-product-grid-image-47-212408')

    @allure.step("Открываем страницу")
    def open(self):
        browser.open("/")
        return self

    @allure.step("Открываем боковое меню")
    def open_menu_tab(self):
        self.menu_tab.click()
        return self

    @allure.step("Нажимаем на категорию MP3 Players")
    def open_mp3_tab(self):
        self.mp3_tab.click()
        return self

    @allure.step("Добавляем продукт в корзину")
    def add_product_to_cart(self):
        self.add_product_to_cart_button.click()
        return self

    @allure.step("Переходим на 2 страницу каталога")
    def open_page_2(self):
        self.page_2.click()
        return self

    @allure.step("Открываем карточку товара HP LP3065")
    def open_hp_lp3065_product(self):
        self.hp_lp3065_product.click()
        return self

    @allure.step("Открываем карточку товара MacBook")
    def open_macbook_product(self):
        self.macbook_product.click()
        return self
