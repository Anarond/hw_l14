from pages.registration_page import RegistrationPage
from pages.account_page import AccountPage
from data.users import registered_user


def test_user_recovery_password(browser_set):
    registration_page = RegistrationPage()
    account_page = AccountPage()

    registration_page.open()

    registration_page.full_register_user(registered_user)
    account_page.click_logout_button()
    account_page.click_forgotten_password_button()
    account_page.fill_email_input()
    account_page.click_submit_button()
    account_page.check_success_message()