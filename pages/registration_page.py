from selene import browser, have
import allure


class RegistrationPage:
    def __init__(self):
        self.first_name_input = browser.element('#input-firstname')
        self.last_name_input = browser.element('#input-lastname')
        self.email_input = browser.element('#input-email')
        self.phone_input = browser.element('#input-telephone')
        self.password_input = browser.element('#input-password')
        self.confirm_password_input = browser.element('#input-confirm')
        self.newsletter_checkbox_yes = browser.element('label[for="input-newsletter-yes"]')
        self.privacy_policy_checkbox = browser.element('label[for="input-agree"]')
        self.register_button = browser.element('input[value="Continue"]')


    @allure.step("Открываем страницу регистрации")
    def open(self):
        browser.open('/index.php?route=account/register')
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

    @allure.step("Заполняем поле Телефон")
    def fill_phone(self, registered_user: dict):
        self.phone_input.type(registered_user['phone'])
        self.phone_input.should(have.value(registered_user['phone']))
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

    @allure.step("Соглашаемся на рассылку Новостей")
    def check_newsletter_checkbox(self):
        self.newsletter_checkbox_yes.click()
        return self

    @allure.step("Соглашаемся с Privacy Policy")
    def check_privacy_policy_checkbox(self):
        self.privacy_policy_checkbox.click()
        return self

    @allure.step("Нажимаем кнопку Регистрация")
    def click_register_button(self):
        self.register_button.click()
        return self
