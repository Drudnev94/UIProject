from pages.home_page import HomePage


class CatalogPage(HomePage):

    # селекторы переделать

    _directory_title = "//span[text()='Каталог']"
    _list_menu = ".sidebar_list_menu__SQXn2"
    _printed_and_electronic = " //li[contains(., 'Печатные')]"
    _for_chef = "//a[@data-qa-locator='leftMenuItem' and contains(., 'Для руководителя')]" #nth(0)
    _for_economist = "//a[@data-qa-locator='leftMenuItem' and contains(., 'Для финансиста')]" #nth(0)
    _for_accountant = "//a[@data-qa-locator='leftMenuItem' and contains(., 'Для бухгалтера')]" #nth(0)






    _content_wrapper = ".l-ss-c-search-popup-content-wrapper"
    _search_category = ".l-ss-c-filter-title"  # nth(2)
    _search_brand = ".l-ss-c-filter-title"  # nth(3)
    _title_text = ".l-ss-c-results-categories-category-title-text"
    _thumbnail_image = ".l-ss-c-offer-thumbnail-image"

    # локаторы

    def content_wrapper(self):
        return self.element(self._content_wrapper)

    def search_category(self):
        return self.element(self._search_category)

    def search_brand(self):
        return self.element(self._search_brand)

    def title_text(self):
        return self.element(self._title_text)

    def thumbnail_image(self):
        return self.element(self._thumbnail_image)


# прописать методы -> добавить в фикстуры и тесты
