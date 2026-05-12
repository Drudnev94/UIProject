from .base_page import BasePage

class MagazinePage(BasePage):
    #Locators

    def chief_accountant(self):
        return self.page.get_by_text("Главбух")

