from .base_page import BasePage

class MagazinePage(BasePage):
    page_url = "product/glavbukh/"
    CLOSE_BANNER = "[data-qa-locator= 'buttonCloseLastHope']"


    #Selectors
    _subscription_options = "//th[text()='Варианты подписки']"
    _chief_accountant = "[data-qa-locator='productName']"
    _magazine_picture = "[data-qa-locator='coverMagazine']"
    _add_to_basket= ".im-add-to-cart-btn"
    # _close_last_hope = "[data-qa-locator= 'buttonCloseLastHope']"

    #Locators

    def subscription_options(self):
        return self.element(self._subscription_options)

    def chief_accountant(self):
        return self.element(self._chief_accountant)

    def magazine_picture(self):
        return self.element(self._magazine_picture)

    def add_to_basket(self):
       return self.element(self._add_to_basket)



    def checking_the_store_page(self,text: str):
        self.page.open_page
        return result_page.open_page()
