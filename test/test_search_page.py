"""Tests for the search page functionality."""
from time import sleep
from playwright.sync_api import expect


class TestSearchPage:
    """Test cases for search functionality."""

    def test_search_page(self,home_page,search,magazine_page):
        target_page = home_page.search_megazin('Электронный журнал. ВИП-версия "Главбух" 12 мес.')
        expect(target_page.page).to_have_title(home_page.target_title)
        # expect(target_page.page).to_have_url(home_page.target_url)

    def test_magazine_page(self,magazine_page):
       target_page = magazine_page.checking_the_store_page()
       expect(target_page.page).to_have_title(magazine_page.target_title)
       expect(target_page.subscription_options()).to_be_visible()
       expect(target_page.chief_accountant()).to_be_visible()
       expect(target_page.magazine_picture()).to_be_visible()
       expect(target_page.add_to_basket()).to_be_visible()
       expect(target_page.page_section()).to_be_visible()
       expect(target_page.nv_bar_fix_top()).to_be_visible()
       expect(target_page.header_banner()).to_be_visible()
       expect(target_page.nv_bar()).to_be_visible()
       expect(target_page.subscription_for_6_months()).to_be_visible()
       expect(target_page.subscription_for_12_months()).to_be_visible()
       expect(target_page.printed_magazine()).to_be_visible()
       expect(target_page.electronic_journal()).to_be_visible()
       expect(target_page.electronic_journal_vip()).to_be_visible()
       expect(target_page.set_printed_electronic()).to_be_visible()
       expect(target_page.buy_in_1_click()).to_be_visible()
       expect(target_page.subscription_form()).to_be_visible()
       expect(target_page.description_title()).to_be_visible()
       expect(target_page.description_paragraph()).to_be_visible()
       expect(target_page.description_body()).to_be_visible()
       expect(target_page.announcement()).to_be_visible()
       expect(target_page.description_title_2()).to_be_visible()
       expect(target_page.description2_paragraph1()).to_be_visible()
       expect(target_page.description2_paragraph2()).to_be_visible()
       expect(target_page.description2_paragraph3()).to_be_visible()
       expect(target_page.description2_paragraph4()).to_be_visible()
       expect(target_page.description2_paragraph5()).to_be_visible()
       expect(target_page.review_block()).to_be_visible()
       expect(target_page.might_like()).to_be_visible()
       expect(target_page.additional_products()).to_be_visible()
       # expect(target_page.get_promo_code()).to_be_visible()






