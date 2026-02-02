from selene import browser
from data.users import registered_user
import allure
from selene import have


class AccountPage:
    def __init__(self):
        self.logout_button = browser.element('#column-right a[href*="logout"]')
        self.forgotten_password_button = browser.element('#column-right a[href*="forgotten"]')
        self.email_input = browser.element('#input-email')
        self.submit_button = browser.element('.buttons.clearfix [type="submit"]')
        self.success_message = browser.element('#account-login .alert-success')

    @allure.step("Открываем страницу аккаунта")
    def open(self):
        browser.open("/index.php?route=account/login")
        return self

    @allure.step("Разлогиниваемся из аккаунта")
    def click_logout_button(self):
        self.logout_button.click()
        return self

    @allure.step("Нажимаем кнопку Восстановить пароль")
    def click_forgotten_password_button(self):
        self.forgotten_password_button.click()
        return self

    @allure.step("Вводим значение в поле Email")
    def fill_email_input(self):
        self.email_input.click().send_keys(registered_user['email'])
        return self

    @allure.step("Нажимаем кнопку подтверждения")
    def click_submit_button(self):
        self.submit_button.click()
        return self

    @allure.step("Проверяем текст подтверждения о восстановлении пароля")
    def check_success_message(self):
        self.success_message.should(have.text("An email with a confirmation link has been sent your email address."))
        return self

