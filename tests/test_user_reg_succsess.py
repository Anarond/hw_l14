import allure
from pages.registration_page import RegistrationPage
from data.users import registered_user
from selene import have

def test_user_registration(browser_set):
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.fill_first_name(registered_user)
    registration_page.fill_last_name(registered_user)
    registration_page.fill_email(registered_user)

    registration_page.first_name_input.should(have.value(registered_user['first_name']))