import pytest
from playwright.sync_api import Page, sync_playwright

from pages.home_page import HomePage
from pages.main_page import MainPage


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
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=500)
    yield browser
    browser.close()


@pytest.fixture(scope="module")
def context(browser):
    """Create a new browser context.
    
    Args:
        browser: Browser instance
        
    Yields:
        Browser context
    """
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="module")
def page(context) -> Page:
    """Create a new page in the context.
    
    Args:
        context: Browser context
        
    Returns:
        Page instance
    """
    return context.new_page()


@pytest.fixture(scope="module")
def header(page):
    """Create a HeaderPage instance.
    
    Args:
        page: Page instance
        
    Returns:
        HeaderPage instance
    """
    return HomePage(page)


@pytest.fixture(scope="module")
def main_page(page):
    """Create a MainPage instance.
    
    Args:
        page: Page instance
        
    Returns:
        MainPage instance
    """
    return MainPage(page)

