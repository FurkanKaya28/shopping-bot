import time
from locators import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class ShoppingBot(object):
    all_price = []
    prod_link = []
    key = 'test'

    @staticmethod
    def sorting(products: list):
        """
        Bulunan ürünleri fiyata göre küçükten büyüğe doğru sıralar. İstenmeyen ürünleri listeden siler.
        Örn: Telefon arıyoruz ama telefon kılıfları da geliyor. Kılıfları ürün listesinden silmek için tüm ürünlerin ortalama fiyatı kullanılmıştır.

        :param products: Ürünlerin bulunduğu liste
        :return: ürünlerin sıralandığı liste
        """
        for idx, number in enumerate(products):
            number, currency = number.split(" ")
            number = float(number.replace(".", "").replace(",", "."))
            products[idx] = number

        mean = sum(products) / len(products)
        numbers = [(idx, num) for idx, num in enumerate(products) if num > mean * 0.5]
        numbers = sorted(numbers, key=lambda num: num[1])
        return numbers

    def __setup(self, url):
        print("Searching on : ", url)
        options = Options()
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-extensions")

        # headless mod da bazı locatorleri bulamıyor ve hata veriyordu. bunu yapınca düzeldi.
        # kaynak: https://stackoverflow.com/questions/50050622/python-selenium-cant-find-element-by-xpath-when-browser-is-headless
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
        options.add_argument('user-agent={0}'.format(user_agent))
        options.add_argument("--window-size=1920x1080")

        self.__driver = webdriver.Chrome(options=options)
        self.__driver.implicitly_wait(10)
        self.__driver.get(url)

    def __quit(self):
        self.__driver.close()
        self.__driver.quit()

    def search_on_n11(self):
        self.__setup("https://www.n11.com/")
        inp = self.__driver.find_element(*N11Locators.SEARCH_INPUT)
        inp.send_keys(self.key + Keys.ENTER)
        products = self.__driver.find_elements(*N11Locators.PRODUCTS)
        for product in products:
            link = product.find_element(By.TAG_NAME, 'a')
            self.prod_link.append(link.get_attribute('href'))
            price = product.find_element(*N11Locators.PRICE)
            self.all_price.append(price.text)
        self.__quit()

    def search_on_trendyol(self):
        self.__setup("https://www.trendyol.com/")
        inp = self.__driver.find_element(*TrendyolLocators.SEARCH_INPUT)
        inp.send_keys(self.key + Keys.ENTER)
        products = self.__driver.find_elements(*TrendyolLocators.PRODUCTS)
        for product in products:
            link = product.find_element(By.TAG_NAME, 'a')
            self.prod_link.append(link.get_attribute('href'))
            price = product.find_element(*TrendyolLocators.PRICE)
            self.all_price.append(price.text)
        self.__quit()

    def search_on_hepsiburada(self):
        self.__setup("https://www.hepsiburada.com/")
        inp = self.__driver.find_element(*HepsiBuradaLocators.SEARCH_INPUT)
        inp.send_keys(self.key + Keys.ENTER)
        products = self.__driver.find_elements(*HepsiBuradaLocators.PRODUCTS)
        for product in products:
            link = product.find_element(By.TAG_NAME, 'a')
            self.prod_link.append(link.get_attribute('href'))
            price = product.find_element(*HepsiBuradaLocators.PRICE)
            self.all_price.append(price.text)
        self.__quit()

    def search_on_gittigidiyor(self):
        self.__setup("https://www.gittigidiyor.com/")
        inp = self.__driver.find_element(*GittiGidiyorLocators.SEARCH_INPUT)
        inp.send_keys(self.key + Keys.ENTER)
        products = self.__driver.find_elements(*GittiGidiyorLocators.PRODUCTS)
        for product in products:
            self.prod_link.append(product.get_attribute('href'))
            price = product.find_element(*GittiGidiyorLocators.PRICE)
            self.all_price.append(price.text)
        self.__quit()

    def run(self):
        stime = time.time()
        self.search_on_n11()
        self.search_on_trendyol()
        self.search_on_hepsiburada()
        self.search_on_gittigidiyor()
        print("Total time: ", round(time.time() - stime, 2), " sn")
        print("Number of products found: ", len(self.prod_link))

    def get_result(self):
        prices = self.sorting(self.all_price)
        for idx, pr in prices:
            print("************\nPrice: ", pr, "TL\nLink: ", self.prod_link[idx], "\n************\n")


bot = ShoppingBot()
bot.key = "xiaomi robot süpürge"
bot.run()
bot.get_result()
