from playwright.sync_api import expect

from .base_page import BasePage


class HeaderPage(BasePage):
    """Page object for the header section of the website."""

    page_url = "https://action-press.ru/"

    # Selectors
    _search_selector = "input[placeholder='Поиск']"
    _search_input_selector = "input[placeholder='Что вы хотите найти?']"
    _search_button_selector = "l-ss-c-button l-ss-c-search-input-action-search"

    def search_locator(self):
        """Get locator for the search input field.
        
        Returns:
            Playwright Locator for search field
        """
        return self.element(self._search_selector)

    def search_input_selector(self):
        """Get locator for the search text input.
        
        Returns:
            Playwright Locator for search text input
        """
        return self.element(self._search_input_selector)

    def search_button_selector(self):
        """Get locator for the search button.
        
        Returns:
            Playwright Locator for search button
        """
        return self.element(self._search_button_selector)

    def search(self, text: str) -> None:
        """Perform a search with the given text.
        
        Args:
            text: Search query string
        """
        self.search_locator().click()
        self.search_input_selector().fill(text)
        self.search_button_selector().click()


