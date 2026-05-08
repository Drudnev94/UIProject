from playwright.sync_api import expect
from UIProject.pages.base_page import BasePage

class HeaderPage(BasePage):
    page_url = "https://action-press.ru/"
    # селекторы
    _search_selector = "input[placeholder = 'Поиск']"  # .nth(1)
    _search_input_selector = "input[placeholder = 'Что вы хотите найти?']"
    _search_button_selector = "l-ss-c-button l-ss-c-search-input-action-search"

    # локаторы
    def search_locator(self):
        return self.element(self._search_selector)

    def search_input_selector(self):
        return self.element(self._search_input_selector)

    def search_button_selector(self):
        return self.element(self._search_button_selector)


    # методы
    def search(self, text:str):
        self.search_locator().click()
        self.search_input_selector().fill(text)
        self.search_button_selector().click()


