from pages.base_page import BasePage


class AboutPage(BasePage):
    page_url = "about/"
    target_title = '"Актион-пресс" | О нас'
    target_url = f"{BasePage.BASE_URL}{page_url}"

    """Селекторы"""
    _nv_bar = "//*[contains(@class, 'navbar navbar-expand-lg navbar-sub-heade')]"
    _header_banner = "//*[contains(@class, 'img-fluid')]"
    _nv_bar_fix_top = "//*[contains(@class, 'navbar fixed-top')]"
    _sidebar_list_menu = ".sidebar_list_menu__SQXn2" #nth(0)
    _catalog = '//span[text()="Каталог"]'
    _news = '//span[text()="Новости"]'
    _new_block = ".our-adv-menu-block" #ntg(0)
    _all_new = '[data-qa-locator="allNewsLink"]'
    _our_advantages = "//span[text()='Наши преимущества']"
    _advantages_block = ".our-adv-menu-block" #nth(1)
    _article_title = "//h2[contains(., 'Официальный')]"
    _banner_content = "//*[contains(@class, 'banner__image_content')]"
    _banner_image_content = "//*[contains(@class, 'banner__image_content')]"
    _why_trust = "//div[text()='Почему нам доверяют']"
    _banner_content_list = "//*[contains(@class, 'content__list_image')]"
    _content_list = ".content__list" #nth(0)
    _guarantee_header = '//h2[text()="Гарантии качества"]'
    _bottom_list = "//*[contains(@class, 'content__BottomList')]"
    _bottom_title = "//*[contains(@class, 'bottom__title')"
    _bottom_devider = "//*[contains(@class, 'bottom__devider')]"
    _bottom_advantages = "//*[contains(@class, 'bottom__devider')]"
    _job_evaluation_link = "//*[contains(@class, 'pl-4 pt-4 pb-4')]"
    _additional_products = "//*[contains(@class, 'row p-3 bg-white')]"
    _footer_desktop = "//*[contains(@class, 'footer-new-desktop')]"

    """Локаторы"""

    def nv_bar(self):
        return self.element(self._nv_bar)

    def about_header_banner(self):
        return self.element(self._header_banner)

    def nv_bar_fix_top(self):
        return self.element(self._nv_bar_fix_top)

    def sidebar_list_menu(self):
        return self.element(self._sidebar_list_menu).nth(0)

    def catalog(self):
        return self.element(self._catalog)

    def news(self):
        return self.element(self._news)

    def news_block(self):
        return self.element(self._new_block).ntg(0)

    def all_news(self):
        return self.element(self._all_new)

    def our_advantages(self):
        return self.element(self._our_advantages)

    def advantages_block(self):
        return self.element(self._advantages_block).nth(1)

    def article_title(self):
        return self.element(self._article_title)

    def banner_content(self):
        return self.element(self._banner_content)

    def banner_image_content(self):
        return self.element(self._banner_image_content)

    def why_trust(self):
        return self.element(self._why_trust)

    def banner_content_list(self):
        return self.element(self._banner_content_list)

    def content_list(self):
        return self.element(self._content_list).nth(0)

    def guarantee_header(self):
        return self.element(self._guarantee_header)

    def bottom_list(self):
        return self.element(self._bottom_list)

    def bottom_title(self):
        return self.element(self._bottom_title)

    def bottom_devider(self):
        return self.element(self._bottom_devider)

    def bottom_advantages(self):
        return self.element(self._bottom_advantages)

    def job_evaluation_link(self):
        return self.element(self._job_evaluation_link)

    def about_additional_products(self):
        return self.element(self._additional_products)

    def footer_desktop(self):
        return self.element(self._footer_desktop)


    """Методы"""

    def return_about_page(self):
        """Возвращает загруженную страницу в тест"""
        self.open_page()
        self.page.wait_for_load_state("domcontentloaded")
        return self

