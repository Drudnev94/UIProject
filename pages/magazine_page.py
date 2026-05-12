from .base_page import BasePage

class MagazinePage(BasePage):

    #Selectors
    _subscription_options = "//th[text()='Варианты подписки']"

    #Locators

    def subscription_options(self):
        return self.element(self._subscription_options)


