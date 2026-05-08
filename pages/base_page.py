from playwright.sync_api import Page


class BasePage:
    """Base page object providing common functionality for all pages."""

    BASE_URL = "https://action-press.ru/"
    page_url = ""

    def __init__(self, page: Page):
        """Initialize base page with Playwright page instance.
        
        Args:
            page: Playwright Page instance
        """
        self.page = page

    def full_url(self) -> str:
        """Construct the full URL for the page.
        
        Returns:
            Complete URL string
        """
        return f"{self.BASE_URL}{self.page_url}"

    def open_page(self) -> None:
        """Navigate to the page's URL."""
        self.page.goto(self.full_url())

    def element(self, selector: str):
        """Get a locator for the given selector.
        
        Args:
            selector: CSS or XPath selector string
            
        Returns:
            Playwright Locator instance
        """
        return self.page.locator(selector)
