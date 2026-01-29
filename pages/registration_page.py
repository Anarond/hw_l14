from selene import browser


class RegistrationPage:
    def __init__(self):
        self.first_name_input = browser.element('#FirstName')
        self.last_name_input = browser.element('#LastName')
        self.email_input = browser.element('#Email')

    def open(self):
        browser.open("/register")
        return self

    def fill_first_name(self, user_data: dict):
        self.first_name_input.type(user_data['first_name'])
        return self

    def fill_last_name(self, user_data: dict):
        self.last_name_input.type(user_data['last_name'])
        return self

    def fill_email(self, user_data: dict):
        self.email_input.type(user_data['email'])
        return self
