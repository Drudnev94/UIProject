from playwright.sync_api import expect

from .base_page import BasePage


class HomePage(BasePage):
    """Page object for the header section of the website."""

    #page_url = "https://action-press.ru/"

    # Selectors
    _search_selector = "input[placeholder='Поиск']"
    _search_input_selector = "input[placeholder='Что вы хотите найти?']"
    _search_button_selector = '[href="https://action-press.ru/product/glavbukh/"]'

    def search_locator(self):
        return self.element(self._search_selector).nth(1)

    def search_input_selector(self):
        return self.element(self._search_input_selector)

    def search_button_selector(self):
        return self.element(self._search_button_selector).nth(0)

    def search_megazin(self, text: str):
        """Поиск через строку поиска"""
        self.search_locator().click()
        self.search_input_selector().fill(text)
        self.search_button_selector().click()


