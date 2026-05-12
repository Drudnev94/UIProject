import pytest
from playwright.sync_api import Page, sync_playwright

from pages.home_page import HomePage
from pages.main_page import MainPage
from  pages.magazine_page import MagazinePage


@pytest.fixture(scope="module")
def playwright_instance():
    """Create a Playwright instance."""
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="module")
def browser(playwright_instance):
    """Create a new browser instance.
    
    Args:
        playwright_instance: Playwright instance
        
    Yields:
        Browser instance
    """
    browser = playwright_instance.chromium.launch(headless=True, slow_mo=800)
    yield browser
    browser.close()


@pytest.fixture(scope="module")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="module")
def page(context) -> Page:
    return context.new_page()


@pytest.fixture(scope="module")
def home_page(page):
    return HomePage(page)


@pytest.fixture(scope="module")
def main_page(page):
    return MainPage(page)

@pytest.fixture(scope="module")
def magazine_page(page):
    return MagazinePage(page)

@pytest.fixture(scope="module")
def search(home_page):
    return home_page.open_page()
