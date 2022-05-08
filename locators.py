from selenium.webdriver.common.by import By


class N11Locators:
    SEARCH_INPUT = (By.ID, "searchData")
    PRODUCTS = (By.CSS_SELECTOR, "#view ul li.column")
    PRICE = (By.CLASS_NAME, "newPrice")


class TrendyolLocators:
    SEARCH_INPUT = (By.CLASS_NAME, "search-box")
    PRODUCTS = (By.CLASS_NAME, "p-card-chldrn-cntnr")
    PRICE = (By.CLASS_NAME, "prc-box-dscntd")


class HepsiBuradaLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "#SearchBoxOld input")
    PRODUCTS = (By.CLASS_NAME, "productListContent-item")
    PRICE = (By.CSS_SELECTOR, '[data-test-id="price-current-price"]')


class GittiGidiyorLocators:
    SEARCH_INPUT = (By.NAME, "k")
    PRODUCTS = (By.CSS_SELECTOR, '[data-cy="product-card-item"] div a')
    PRICE = (By.CSS_SELECTOR, '[data-cy="buy-price"]')
