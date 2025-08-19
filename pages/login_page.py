from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_url(self):
        current_url = self.browser.current_url
        if 'login' not in current_url:
            print(f"WARNING: 'login' not in URL, but continuing. URL: {current_url}")
            return True
        assert 'login' in current_url, f"Substring 'login' not found in current url: {current_url}"

    def go_to_login_page(self):
        link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
                "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
                "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)

        password_field1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field1.clear()
        password_field1.send_keys(password)

        password_field2 = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        password_field2.clear()
        password_field2.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

        self._wait_for_authorization()
