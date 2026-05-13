
from playwright.sync_api import expect

from pages.about_page import AboutPage


class TestAboutPage():

    def test_about_page(self,about_page):
        """Проверка элементов страницы"""
        target_page = about_page.return_about_page()
        expect(target_page.page).to_have_title(about_page.target_title)
        expect(target_page.page).to_have_url(about_page.target_url)
        expect(target_page.nv_bar()).to_be_visible()
        expect(target_page.about_header_banner()).to_be_visible()
        expect(target_page.nv_bar_fix_top()).to_be_visible()
        expect(target_page.sidebar_list_menu()).to_be_visible()
        expect(target_page.catalog()).to_be_visible()
        expect(target_page.news()).to_be_visible()
        # expect(target_page.news_block()).to_be_visible()
        expect(target_page.all_news()).to_be_visible()
        expect(target_page.our_advantages()).to_be_visible()
        expect(target_page.all_news()).to_be_visible()
        expect(target_page.advantages_block()).to_be_visible()
        expect(target_page.article_title()).to_be_visible()
        expect(target_page.banner_content()).to_be_visible()
        expect(target_page.banner_image_content()).to_be_visible()
        expect(target_page.why_trust()).to_be_visible()
        expect(target_page.banner_content()).to_be_visible()
        expect(target_page.banner_content_list()).to_be_visible()
        expect(target_page.content_list()).to_be_visible()
        expect(target_page.guarantee_header()).to_be_visible()
        expect(target_page.bottom_list()).to_be_visible()
        # expect(target_page.bottom_title()).to_be_visible()
        expect(target_page.bottom_devider()).to_be_visible()
        expect(target_page.bottom_advantages()).to_be_visible()
        expect(target_page.job_evaluation_link()).to_be_visible()
        expect(target_page.about_additional_products()).to_be_visible()
        expect(target_page.footer_desktop()).to_be_visible()





