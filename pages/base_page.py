from playwright.sync_api import Page


class BasePage:
    """Базовые методы"""

    BASE_URL = "https://action-press.ru/"
    page_url = ""

    def __init__(self, page: Page):
        self.page = page

    def full_url(self) -> str:
        """Формирует полный Url"""
        return f"{self.BASE_URL}{self.page_url}"

    def open_page(self) -> None:
        """Открывает страницу с полным url"""
        self.page.goto(self.full_url())

    def element(self, selector: str):
        """Оборачивает селектор  в локатор"""
        return self.page.locator(selector)
