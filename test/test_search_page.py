"""Tests for the search page functionality."""
from time import sleep
from playwright.sync_api import expect


class TestSearchPage:
    """Test cases for search functionality."""

    def test_search_page(self,home_page,search,magazine_page):
        result_page =  home_page.search_megazin('Электронный журнал. ВИП-версия "Главбух" 12 мес.')
        # sleep(3)
        # print(result_page.page.title())
        print(result_page.page.url())
        expect(result_page.subscription_options()).to_be_visible(timeout=100000)

    def test_magazine_page(self,magazine_page):
        magazine_page.checking_the_store_page()
        print(page.url())
