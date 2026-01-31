from selene import browser
import allure


class CartPage:
    def __init__(self):
        self.electronics_tab = browser.element('a[href="/electronics"]')
        self.cell_phones_tab = browser.element('.sub-category-item a[href="/cell-phones"]')
        self.iphone_product = browser.element('[data-productid="21"] .product-box-add-to-cart-button')
        self.nokia_product = browser.element('[data-productid="20"] .product-box-add-to-cart-button')
        self.books_tab = browser.element('a[href="/books"]')
        self.fahrenheit_product = browser.element('[data-productid="36"] .product-box-add-to-cart-button')
        self.jewelry_tab = browser.element('a[href="/jewelry"]')
        self.bracelet_product = browser.element('[data-productid="41"] .product-box-add-to-cart-button')
        self.cart_tab = browser.element('a[href="/cart"]')



    @allure.step("Открываем страницу")
    def open(self):
        browser.open("/")
        return self

    @allure.step("Нажимаем таб Электроника")
    def click_electronics_tab(self):
        self.electronics_tab.click()
        return self

    @allure.step("Нажимаем таб Телефоны")
    def click_cell_phones_tab(self):
        self.cell_phones_tab.click()
        return self

    @allure.step("Добавляем Iphone в Корзину")
    def add_iphone_to_cart(self):
        self.iphone_product.click()
        return self

    @allure.step("Добавляем Nokia в Корзину")
    def add_nokia_to_cart(self):
        self.nokia_product.click()
        return self

    @allure.step("Нажимаем таб Книги")
    def click_books_tab(self):
        self.books_tab.click()
        return self

    @allure.step("Добавляем Fahrenheit в Корзину")
    def add_fahrenheit_to_cart(self):
        self.fahrenheit_product.click()
        return self

    @allure.step("Нажимаем таб Украшения")
    def click_jewelry_tab(self):
        self.jewelry_tab.click()
        return self

    @allure.step("Добавляем Bracelet в Корзину")
    def add_bracelet_to_cart(self):
        self.bracelet_product.click()
        return self

    @allure.step("Открывает Корзину")
    def open_cart(self):
        self.cart_tab.click()
        return self