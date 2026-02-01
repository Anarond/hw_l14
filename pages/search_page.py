from selene import browser, have
import allure

class SearchPage:
    def __init__(self):
        self.search_input = browser.element('#search input[name="search"]')
        self.search_button = browser.element('[data-id="217822"] .search-button')
        self.search_result = browser.all('[data-id="212469"] h4.title').first


    @allure.step("Открываем главную страницу")
    def open(self):
        browser.open("/")
        return self

    @allure.step("Нажимаем на поиск")
    def open_search(self):
        self.search_input.click()
        return self

    @allure.step("Вводим название товара '{product_name}' в поиск")
    def send_product_search(self, product_name):
        self.search_input.send_keys(product_name)
        return self

    @allure.step("Нажимаем кнопку поиска")
    def click_search_button(self):
        self.search_button.click()
        return self

    @allure.step("Проверяем наличие товара '{product_name}' в результатах поиска")
    def check_search_result(self, product_name):
        self.search_result.should(have.text(product_name))
        return self

    # @allure.step("Ищем товар: {query}")
    # def search_for(self, query):
    #     self.search_input.should(be.visible).set_value(query)
    #     self.search_button.click()
    #     return self
    #
    # @allure.step("Проверяем, что в результатах поиска есть товар: {expected_text}")
    # def should_find_product(self, expected_text):
    #     # Проверяем, что хотя бы один товар из списка содержит искомый текст
    #     self.products.element_by(have.text(expected_text)).should(be.visible)
    #     return self
    #
    # @allure.step("Проверяем заголовок страницы поиска")
    # def should_have_header(self, query):
    #     self.search_header.should(have.text(f"Search - {query}"))
    #     return self