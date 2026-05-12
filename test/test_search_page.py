"""Tests for the search page functionality."""
from playwright.sync_api import expect


class TestSearchPage:
    """Test cases for search functionality."""

    def test_search_page(self,home_page,search,magazine_page):
        result_page =  home_page.search_megazin('Электронный журнал. ВИП-версия "Главбух" 12 мес.')
        expect (result_page.subscription_options).to_be_visible()

