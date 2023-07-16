# Crawler Controller
link = "https://www.amazon.com/"
item = "iphone"

popup_path = '//*[@id="nav-main"]/div[1]/div/div/div[3]/span[1]/span/input'

search_id1 = "twotabsearchtextbox"
search_id2 = 'nav-bb-search'

product_path = '//*[contains(concat( " ", @class, " " ), concat( " ", "a-link-normal", " " )) and ' \
                     'contains(concat( " ", @class, " " ), concat( " ", "s-link-style a-text-normal", " " ))]'

price_path1 = '//span[contains(@class, "apexPriceToPay")]'
price_path2 = '//div[contains(@id, "corePrice_feature_div")]'

description_id = 'feature-bullets'

rating_path = '//span[@data-hook = "rating-out-of-text"]'
total_reviews_id = 'acrCustomerReviewText'

asin_path = '//td[@class = "a-size-base prodDetAttrValue"]'

next_element_path = '//a[contains(@class, "s-pagination-next")]'


class Controller:
    @staticmethod
    def get_url_link():
        return link

    @staticmethod
    def get_user_search():
        return item

    @staticmethod
    def get_popup_path():
        return popup_path

    @staticmethod
    def get_search_id(arg):
        if arg == 1:
            return search_id1
        if arg == 2:
            return search_id2

    @staticmethod
    def get_product_links():
        return product_path

    @staticmethod
    def get_price_path(arg):
        if arg == 1:
            return price_path1
        if arg == 2:
            return price_path2

    @staticmethod
    def get_description():
        return description_id

    @staticmethod
    def get_rating():
        return rating_path

    @staticmethod
    def get_total_reviews_id():
        return total_reviews_id

    @staticmethod
    def get_asin_path():
        return asin_path

    @staticmethod
    def get_next_element_path():
        return next_element_path


if __name__ == "__main__":
    main = Controller()
