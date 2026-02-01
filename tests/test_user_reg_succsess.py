from pages.registration_page import RegistrationPage
from data.users import registered_user


def test_user_registration(browser_set):
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.fill_first_name(registered_user)
    registration_page.fill_last_name(registered_user)
    registration_page.fill_email(registered_user)
    registration_page.fill_phone(registered_user)
    registration_page.fill_password(registered_user)
    registration_page.fill_confirm_password(registered_user)
    registration_page.check_newsletter_checkbox()
    registration_page.check_privacy_policy_checkbox()
    registration_page.click_register_button()
