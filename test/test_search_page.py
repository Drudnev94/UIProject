"""Tests for the search page functionality."""

from pages.home_page import HomePage


class TestSearchPage:
    """Test cases for search functionality."""

    def test_search_page(self, header: HomePage) -> None:
        header.search("Электронный журнал. ВИП-версия 'Главбух' 12 мес.")