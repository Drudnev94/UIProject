import pytest
from playwright.async_api import Page
from playwright.sync_api import Playwright, sync_playwright
from UIProject.pages.header import HeaderPage
from UIProject.pages.main_pag import MainPage


@pytest.fixture(scope="module")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="module")
def browser(playwright_instance, request):
    """Создает браузер, каждый раз новый"""
    browser = playwright_instance.chromium.launch(headless=False,slow_mo=500)
    # browser = playwright_instance.chromium.launch()
    yield browser
    browser.close()

@pytest.fixture(scope="module")
def context(browser):
    """Создает контент в браузере, каждый раз новый"""
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="module")
def page(context) -> Page:
    """Создает новую вкладку в контексте, принимает  контекст возвращает page"""
    page: Page = context.new_page()
    return page

@pytest.fixture(scope="module")
def header(page):
    """Возврашаем класс HeaderPage"""
    return HeaderPage(page)

@pytest.fixture(scope="module")
def mai_npage(page):
    return MainPage(page)

