from selene import browser, have
import allure


class RegistrationPage:
    def __init__(self):
        self.first_name_input = browser.element('#FirstName')
        self.last_name_input = browser.element('#LastName')
        self.email_input = browser.element('#Email')
        self.company_name_input = browser.element('#Company')
        self.password_input = browser.element('#Password')
        self.confirm_password_input = browser.element('#ConfirmPassword')
        self.checkbox = browser.element('.form-check-input')
        self.gender = browser.element('#gender-male')
        self.register_button = browser.element('#register-button')
        self.registration_result = browser.element('.result')


    @allure.step("Открываем страницу регистрации")
    def open(self):
        browser.open("/register")
        return self

    @allure.step("Выбираем Пол")
    def check_gender(self):
        self.gender.click()
        return self

    @allure.step("Заполняем поле Имя")
    def fill_first_name(self, registered_user: dict):
        self.first_name_input.type(registered_user['first_name'])
        self.first_name_input.should(have.value(registered_user['first_name']))
        return self

    @allure.step("Заполняем поле Фамилия")
    def fill_last_name(self, registered_user: dict):
        self.last_name_input.type(registered_user['last_name'])
        self.last_name_input.should(have.value(registered_user['last_name']))
        return self

    @allure.step("Заполняем поле Почта")
    def fill_email(self, registered_user: dict):
        self.email_input.type(registered_user['email'])
        self.email_input.should(have.value(registered_user['email']))
        return self

    @allure.step("Заполняем поле Компания")
    def fill_company_name(self, registered_user: dict):
        self.company_name_input.type(registered_user['company_name'])
        self.company_name_input.should(have.value(registered_user['company_name']))
        return self

    @allure.step("Заполняем поле Пароль")
    def fill_password(self, registered_user: dict):
        self.password_input.type(registered_user['password'])
        self.password_input.should(have.value(registered_user['password']))
        return self

    @allure.step("Подтверждаем поле Пароль")
    def fill_confirm_password(self, registered_user: dict):
        self.confirm_password_input.type(registered_user['confirm_password'])
        self.confirm_password_input.should(have.value(registered_user['confirm_password']))
        return self

    @allure.step("Отключаем чекбокс Новости")
    def uncheck_checkbox(self):
        self.checkbox.click()
        return self

    @allure.step("Нажимаем кнопку Регистрация")
    def click_register_button(self):
        self.register_button.click()
        return self

    @allure.step("Проверяем текст об успешной регистрации")
    def have_success_message(self, message):
        self.registration_result.should(have.text(message))
        return self