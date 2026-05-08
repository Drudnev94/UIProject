"""Main page object for the homepage."""

from .base_page import BasePage


class MainPage(BasePage):
    """Page object for the main homepage."""

    page_url = BasePage.BASE_URL

    # Header selectors
    _logo = "[alt='Актион-пресс']"
    _registration_button = "[dataqa= 'SSOAuthButton']"
    _cart_counter = "[data-qa-locator = 'basketCount']"
    _basket_img = ".basket"
    _phone_number = "[data-qa-locator='phoneNumber']"
    _telegram = "[data-qa-locator= 'actionTelegramm']"
    _what_sap = "[data-qa-locator='actionWhatsAp']"
    _max = "[data-qa-locator='actionMax']"
    _about_as = "//span[text() = 'О нас']"
    _contacts = "//span[text() = 'Контакты']"
    _payment_method = "//span[text() = 'Способы оплаты']"
    _delivery_methods = "//span[text() = 'Способы доставки']"
    _search_input_selector = "//*[@placeholder='Поиск']"
    _banner = ".img-fluid"

    # Section selectors
    _title_text_selector = "//div[text()='Рекомендованные издания']"
    _title_catalog_selector = "//span[text() = 'Каталог']"
    _link = "//a[text()='Печатные и электронные издания']"
    _news = "//span[text()='Новости']"
    _advantages = "//span[text()='Наши преимущества']"

    # Product link selectors
    _glavbux = "//a[text()='Главбух']"
    _uprashenka = "//a[text()='Упрощёнка']"
    _kadrovoe_delo = "//a[text()='Кадровое дело']"
    _urist_kompani = "//a[text()='Юрист компании']"
    _zarplata = "//a[text()='Зарплата']"
    _ushet_nalogi = "//a[text()='Учёт. Налоги. Право']"
    _gen_dir = "//a[text()='Генеральный директор']"
    _fin_dir = "//a[text()='Финансовый директор']"
    _ros_nalog_kurer = "//a[text()='Российский налоговый курьер']"

    # Banner selectors
    _glavbux_baner = "[src='https://fb.action-press.ru/docs/ecm/images/glavbuh.png']"
    _gen_dir_baner = "[src='https://fb.action-press.ru/docs/ecm/images/genDir.png']"
    _zarplata_baner = "[src='https://fb.action-press.ru/docs/ecm/images/zarp.png']"
    _uprashenka_baner = "[src='https://fb.action-press.ru/docs/ecm/images/upr.png']"
    _ros_nalog_kurer_baner = (
        "[src='https://fb.action-press.ru/docs/ecm/images/rnk.png']"
    )
    _ushet_nalogi_baner = (
        "[src='https://fb.action-press.ru/docs/ecm/images/uchNalPravo.png']"
    )
    _kadrovoe_delo_baner = (
        "[src='https://fb.action-press.ru/docs/ecm/images/kadrDel.png']"
    )
    _urist_kompani_baner = (
        "[src='https://fb.action-press.ru/docs/ecm/images/urComp.png']"
    )
    _fin_dir_baner = "[src='https://fb.action-press.ru/docs/ecm/images/finDir.png']"
    _trud_spor = "[src='https://fb.action-press.ru/docs/ecm/images/trudSpor.png']"

    # Footer selectors
    _logo2 = "[alt='Action logo']"
    _logo3 = "//div[text()='Официальный интернет-магазин группы Актион']"
    _column1 = "[data-qa-locator='column1']"
    _column2 = "[data-qa-locator='column2']"
    _column3 = "[data-qa-locator='column3']"
    _column4 = "//h5[text()= 'Свяжитесь' ]"
    _column5 = "//a[text()='Электронные ']"

    _label_data = ".footer-copyright"
    _label_data1 = ".footer-copyright"

    _footer_payment_method1 = (
        "[src='https://fb.action-press.ru/docs/ecm/images/visa.png']"
    )
    _footer_payment_method2 = (
        "[src='https://fb.action-press.ru/docs/ecm/images/mastercard-icon.png']"
    )
    _footer_payment_method3 = (
        "[src='https://fb.action-press.ru/docs/ecm/images/mir-2.png']"
    )
    _button_up = "//button[text() = 'ВВЕРХ ']"
    _bot_chat = "hoverArea__bKo37"

    # Header locators
    def logo_locator(self):
        return self.element(self._logo)

    def registration_button_locator(self):
        return self.element(self._registration_button)

    def cart_counter_locator(self):
        return self.element(self._cart_counter)

    def basket_img_locator(self):
        return self.element(self._basket_img)

    def phone_number_locator(self):
        return self.element(self._phone_number)

    def tekegram_locator(self):
        return self.element(self._telegram)

    def what_sap_locator(self):
        return self.element(self._what_sap)

    def max_locator(self):
        return self.element(self._max)

    def about_as_locator(self):
        return self.element(self._about_as)

    def contacts_locator(self):
        return self.element(self._contacts)

    def payment_method_locator(self):
        return self.element(self._payment_method)

    def delivery_methods_locator(self):
        return self.element(self._delivery_methods)

    def search_input_selector_locator(self):
        return self.element(self._search_input_selector)

    def banner_locator(self):
        return self.element(self._banner)

    # Section locators
    def title_text_selector_locator(self):
        return self.element(self._title_text_selector)

    def title_catalog_selector_locator(self):
        return self.element(self._title_catalog_selector)

    def link_locator(self):
        return self.element(self._link)

    def news_locator(self):
        return self.element(self._news)

    def advantages_locator(self):
        return self.element(self._advantages)

    # Product locators
    def glavbux_locator(self):
        return self.element(self._glavbux)

    def uprashenka_locator(self):
        return self.element(self._uprashenka)

    def kadrovoe_delo_locator(self):
        return self.element(self._kadrovoe_delo)

    def urist_kompani_locator(self):
        return self.element(self._urist_kompani)

    def zarplata_locator(self):
        return self.element(self._zarplata_baner)

    def ushet_nalogi_locator(self):
        return self.element(self._ushet_nalogi)

    def gen_dir_locator(self):
        return self.element(self._gen_dir)

    def fin_dir_locator(self):
        return self.element(self._fin_dir)

    def ros_nalog_kurer_locator(self):
        return self.element(self._ros_nalog_kurer)

    # Banner locators
    def glavbux_baner_locator(self):
        return self.element(self._glavbux_baner)

    def gen_dir_baner_locator(self):
        return self.element(self._gen_dir_baner)

    def zarplata_baner_locator(self):
        return self.element(self._zarplata_baner)

    def uprashenka_baner_locator(self):
        return self.element(self._uprashenka_baner)

    def ros_nalog_kurer_baner_locator(self):
        return self.element(self._ros_nalog_kurer_baner)

    def ushet_nalogi_baner_locator(self):
        return self.element(self._ushet_nalogi_baner)

    def kadrovoe_delo_baner_locator(self):
        return self.element(self._kadrovoe_delo_baner)

    def urist_kompani_baner_locator(self):
        return self.element(self._urist_kompani_baner)

    def fin_dir_baner_locator(self):
        return self.element(self._fin_dir_baner)

    def trud_spor_locator(self):
        return self.element(self._trud_spor)

    # Footer locators
    def logo2_locator(self):
        return self.element(self._logo2)

    def column1_locator(self):
        return self.element(self._column1)

    def column2_locator(self):
        return self.element(self._column2)

    def column3_locator(self):
        return self.element(self._column3)

    def column4_locator(self):
        return self.element(self._column4)

    def column5_locator(self):
        return self.element(self._column5)

    def label_data_locator(self):
        return self.element(self._label_data)

    def label_data1_locator(self):
        return self.element(self._label_data1)

    def footer_payment_method1_locator(self):
        return self.element(self._footer_payment_method1)

    def footer_payment_method2_locator(self):
        return self.element(self._footer_payment_method2)

    def footer_payment_method3_locator(self):
        return self.element(self._footer_payment_method3)

    def button_up_locator(self):
        return self.element(self._button_up)

    def bot_chat_locator(self):
        return self.element(self._bot_chat)
