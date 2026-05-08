"""Tests for the search page functionality."""

from pages.header import HeaderPage


class TestSearchPage:
    """Test cases for search functionality."""

    def test_search_page(self, header: HeaderPage) -> None:
        """Test that search works with a specific query.
        
        Args:
            header: HeaderPage fixture
        """
        header.search("Электронный журнал. ВИП-версия 'Главбух' 12 мес.")