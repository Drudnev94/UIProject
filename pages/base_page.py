from playwright.sync_api import Page

class BasePage:
    BASE_URL = "https://action-press.ru/"
    page_url = ""

    def __init__(self, page: Page):
        self.page = page

    def full_url(self):
        return f"{self.BASE_URL}{self.page_url}"
"""Метод который позволяет нам открыть старницу, должен быть на всех страницах
            передаем в него урл"""
    def open_page(self):
        self.page.goto(self.full_url())

    def element(self,selector):
        return self.page.locator(selector)
