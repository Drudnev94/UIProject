import pytest
from playwright.sync_api import Page, sync_playwright

from pages.home_page import HomePage
from pages.main_page import MainPage
from pages.magazine_page import MagazinePage
from pages.about_page import AboutPage



@pytest.fixture(scope="module")
def playwright_instance():
    """Создаем инстансы playwright"""
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="module")
def browser(playwright_instance):
    """Создаем новый браузер"""
    # browser = playwright_instance.chromium.launch(headless=False, slow_mo=800)
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture(scope="module")
def context(browser):
    """Создаем контекст"""
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="module")
def page(context) -> Page:
    """Создаем страницу"""
    return context.new_page()


@pytest.fixture(scope="module")
def home_page(page):
    """Возвращаем класс HomePage"""
    return HomePage(page)


@pytest.fixture(scope="module")
def main_page(page):
    """Возвращаем класс MainPage"""
    return MainPage(page)


@pytest.fixture(scope="module")
def magazine_page(page):
    """Возвращаем класс MagazinePage"""
    return MagazinePage(page)

@pytest.fixture(scope="module")
def about_page(page):
    return AboutPage(page)

@pytest.fixture(scope="module")
def search(home_page):
    """Открываем страницу с home_page"""
    return home_page.open_page()


@pytest.fixture(scope="module")
def checking_magazine(magazine_page):
    """Открываем страницу с magazine_page"""
    return magazine_page.open_page()
