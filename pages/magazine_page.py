from .base_page import BasePage

class MagazinePage(BasePage):

    #Selectors
    _subscription_options = "//th[text()='Варианты подписки']"
    _chief_accountant = "[data-qa-locator='productName']"
    _cover_magazine = "[data-qa-locator='coverMagazine']"
    _add = "btn float-right im-add-to-cart-btn"

    #Locators

    def subscription_options(self):
        return self.element(self._subscription_options)

    def chief_accountant(self):
        return self.element(self._chief_accountant)

    def cover_magazine(self):
        return self.element(self._cover_magazine)

    def add(self):
        return self.element(self._add)



