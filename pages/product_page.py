from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import LoginPageLocators

class ProductPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), \
            "Login link is not presented"

    def go_to_login_page(self):
        link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        link.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_product_added_message(self):
        product_name = self.get_product_name()
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == message, f"Expected '{product_name}' in message, got '{message}'"

    def should_be_basket_total_message(self):
        product_price = self.get_product_price()
        total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == total, f"Expected '{product_price}' in total, got '{total}'"


