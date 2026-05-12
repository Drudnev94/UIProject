"""Tests for the search page functionality."""



class TestSearchPage:
    """Test cases for search functionality."""

    def test_search_page(self,home_page,search):
        home_page.search_megazin('Электронный журнал. ВИП-версия "Главбух" 12 мес.')