from playwright.async_api import async_playwright
from UIProject.test.conftest import header
from UIProject.pages.header import HeaderPage
class TestSearchPage():

    def test_search_page(self,header):
         header.search("Электронный журнал. ВИП-версия 'Главбух' 12 мес.")