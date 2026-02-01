import time

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


    #registration_page.check_gender.should(have.value('true'))
    # registration_page.first_name_input.should(have.value(registered_user['first_name']))
    # registration_page.last_name_input.should(have.value(registered_user['last_name']))
    # registration_page.email_input.should(have.value(registered_user['email']))
    # registration_page.company_name_input.should(have.value(registered_user['company_name']))
    # registration_page.password_input.should(have.value(registered_user['password']))
    # registration_page.confirm_password_input.should(have.value(registered_user['password']))
    #registration_page.checkbox.should(have.value('true'))
    #registration_page.have_success_message('Your registration completed')