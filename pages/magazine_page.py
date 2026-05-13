from .base_page import BasePage


class MagazinePage(BasePage):
    page_url = "product/glavbukh/"
    target_title = 'Журнал "Главбух" | подписка онлайн'
    target_url = f"{BasePage.BASE_URL}{page_url}"

    """Селекторы"""

    _page_section = "//a[text()='Журнал \"Главбух\"']"
    _nv_bar_fix_top = "//*[contains(@class, 'navbar fixed-top')]"
    _header_banner = "//*[contains(@class, 'img-fluid')]"  # nth(0)
    _nv_bar = " //*[contains(@class, 'navbar navbar-expand-lg navbar-sub-heade')] "
    _subscription_options = "//th[text()='Варианты подписки']"
    _subscription_for_6_months = "//th[text()='6 месяцев']"
    _subscription_for_12_months = "//th[text()='12 месяцев']"
    _printed_magazine = "//span[text()='Печатный журнал']"
    _electronic_journal = "//span[text()='Электронный журнал']"
    _electronic_journal_vip = "//span[text()='Электронный журнал. ВИП-версия']"
    _set_printed_electronic = "//span[text()='Комплект (печатный + электронный)']"
    _chief_accountant = "[data-qa-locator='productName']"
    _magazine_picture = "[data-qa-locator='coverMagazine']"
    _add_to_basket = ".im-add-to-cart-btn"
    _buy_in_1_click = "//button[text()='Купить в 1 клик']"
    _subscription_form = ".cb-subscription-form"
    _description_title = "//h2[contains(., 'положиться')]"
    _description_paragraph = "//p[contains(., 'залог успеха')]"
    _description_body = "//p[contains(., 'законодательства')]"
    _announcement = "//*[contains(@class, 'dark_box')]"
    _description_title_2 = "//h2[contains(., 'Оформив')]"
    _description2_paragraph1 = "//h3[contains(., 'разъяснения')]"
    _description2_paragraph2 = "//h3[contains(., 'Спецвыпуск')]"
    _description2_paragraph3 = "//h3[contains(., 'чиновников')]"
    _description2_paragraph4 = "//h3[contains(., 'памятки')]"
    _description2_paragraph5 = "//h3[contains(., 'Пожизненный')]"
    _review_block = (
        " //*[contains(@class, 'col-sm-12 col-lg-9 offset-lg-3 p-4')] "  # nth(0)
    )
    _might_like = (
        " //*[contains(@class, 'col-sm-12 col-lg-9 offset-lg-3 p-4')] "  # nth(1)
    )
    _additional_products = ".nav-pills"
    # _get_promo_code = "//*[contains(@class,'hoverArea__uCpXp')]"

    """Локаторы"""

    def subscription_options(self):
        return self.element(self._subscription_options)

    def chief_accountant(self):
        return self.element(self._chief_accountant)

    def magazine_picture(self):
        return self.element(self._magazine_picture)

    def add_to_basket(self):
        return self.element(self._add_to_basket)

    def page_section(self):
        return self.element(self._page_section)

    def nv_bar_fix_top(self):
        return self.element(self._nv_bar_fix_top)

    def header_banner(self):
        return self.element(self._header_banner).nth(0)

    def nv_bar(self):
        return self.element(self._nv_bar)

    def subscription_for_6_months(self):
        return self.element(self._subscription_for_6_months)

    def subscription_for_12_months(self):
        return self.element(self._subscription_for_12_months)

    def printed_magazine(self):
        return self.element(self._printed_magazine)

    def electronic_journal(self):
        return self.element(self._electronic_journal)

    def electronic_journal_vip(self):
        return self.element(self._electronic_journal_vip)

    def set_printed_electronic(self):
        return self.element(self._set_printed_electronic)

    def buy_in_1_click(self):
        return self.element(self._buy_in_1_click)

    def subscription_form(self):
        return self.element(self._subscription_form)

    def description_title(self):
        return self.element(self._description_title)

    def description_paragraph(self):
        return self.element(self._description_paragraph)

    def description_body(self):
        return self.element(self._description_body)

    def announcement(self):
        return self.element(self._announcement)

    def description_title_2(self):
        return self.element(self._description_title_2)

    def description2_paragraph1(self):
        return self.element(self._description2_paragraph1)

    def description2_paragraph2(self):
        return self.element(self._description2_paragraph2)

    def description2_paragraph3(self):
        return self.element(self._description2_paragraph3)

    def description2_paragraph4(self):
        return self.element(self._description2_paragraph4)

    def description2_paragraph5(self):
        return self.element(self._description2_paragraph5)

    def review_block(self):
        return self.element(self._review_block).nth(0)

    def might_like(self):
        return self.element(self._might_like).nth(1)

    def additional_products(self):

        return self.element(self._additional_products)

    def get_promo_code(self):
        return self.element(self._get_promo_code)

    """Методы"""

    def checking_the_store_page(self):
        """Возвращает загруженную страницу в тест"""
        self.open_page()
        self.page.wait_for_load_state("domcontentloaded")
        return self
