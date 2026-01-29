from selene import browser
import allure


class RegistrationPage:
    def __init__(self):
        self.first_name_input = browser.element('#FirstName')
        self.last_name_input = browser.element('#LastName')
        self.email_input = browser.element('#Email')

    @allure.step("Открываем страницу регистрации")
    def open(self):
        browser.open("/register")
        return self

    @allure.step("Заполняем поле Имя значением из словаря")
    def fill_first_name(self, registered_user: dict):
        self.first_name_input.type(registered_user['first_name'])
        return self

    @allure.step("Заполняем поле Фамилия значением из словаря")
    def fill_last_name(self, registered_user: dict):
        self.last_name_input.type(registered_user['last_name'])
        return self

    @allure.step("Заполняем поле Почта значением из словаря")
    def fill_email(self, registered_user: dict):
        self.email_input.type(registered_user['email'])
        return self
