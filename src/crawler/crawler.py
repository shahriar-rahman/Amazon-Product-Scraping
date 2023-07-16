import os
import sys
import time as t
import pandas as pd
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as WdW
sys.path.append(os.path.abspath('../controller'))
import controller


class SeleniumDriver:
    def __init__(self):
        # Driver Set-ups
        self.ctrl = controller.Controller()
        start_urls = self.ctrl.get_url_link()
        user_search = self.ctrl.get_user_search()

        self.product_search = user_search
        self.options = ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument("--headless=new")
        self.options.add_argument('window-size=1920x1080')

        self.driver = Chrome(options=self.options)
        self.temp_driver = ''
        self.driver.get(start_urls)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # Storage
        self.product_names = []
        self.prices = []
        self.product_desc = []
        self.ratings = []
        self.total_ratings = []
        self.links = []
        self.asin = []
        self.current = 1
        self.pages = 3
        self.df = pd.DataFrame(columns=['product_names', 'prices', 'product_desc', 'ratings', 'total_ratings',
                                        'links', 'asin'])

    def popup_handler(self, driver):
        # Supress popups
        popup_path = self.ctrl.get_popup_path()
        try:
            popup = WdW(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, popup_path))
            )

        except Exception as exc:
            print("!!! Popup did not appear. !!!\n", exc)

        else:
            popup.click()

    def load_page(self):
        text_box = ''
        # Initiate search page
        try:
            search_id = self.ctrl.get_search_id(1)
            self.popup_handler(self.driver)

            text_box = WdW(self.driver, 5).until(
                ec.presence_of_element_located((By.ID, search_id))
            )

        except Exception as exc:
            print("!!! Failed to locate the text box !!!\n", exc)
            search_id = self.ctrl.get_search_id(2)
            text_box = WdW(self.driver, 10).until(
                ec.presence_of_element_located((By.ID, search_id))
            )

        finally:
            text_box.clear()
            text_box.send_keys(self.product_search)
            text_box.send_keys(Keys.ENTER)
            self.driver.implicitly_wait(10)

    # Nested Pagination
    def access_links(self):
        print('-'*50, '\n' + "◘ Accessing Links...")
        access_products = self.ctrl.get_product_links()
        temp_container = []

        try:
            get_links = WdW(self.driver, 15).until(
                ec.presence_of_all_elements_located((By.XPATH, access_products))
            )

        except Exception as exc:
            print("!!! Links cannot be not found. !!!\n", exc)

        else:
            for link in get_links:
                href = link.get_attribute('href')
                temp_container.append(href)

            temp_container = list(set(temp_container))

            # Diagnosis
            for link in temp_container:
                print('* ', link)

        finally:
            print('-'*50, '\n\n')
            return temp_container

    def get_data(self):
        while self.current <= self.pages:
            # Cycle though all links from each page
            queue = self.access_links()

            for link in queue:
                # Temporary Driver Set-ups
                self.temp_driver = Chrome(options=self.options)
                self.temp_driver.get(link)
                self.temp_driver.implicitly_wait(15)

                self.temp_driver.maximize_window()
                self.popup_handler(self.temp_driver)
                self.temp_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.temp_driver.implicitly_wait(10)

                t.sleep(3)
                text_message = ""
                product_name = self.temp_driver.title.replace('Amazon.com: ', '')

                try:
                    text_message = "◘ Checking for price..."
                    print(text_message)

                    # Nested Try clause for adaptive scraping
                    price_path = self.ctrl.get_price_path(1)
                    try:
                        price = WdW(self.temp_driver, 10).until(
                            ec.presence_of_element_located((By.XPATH, price_path))
                        )

                    except Exception as exc:
                        print("!!! Exception encountered for first attempt during price search !!!\n", exc)

                        price_path = self.ctrl.get_price_path(2)
                        price = WdW(self.temp_driver, 10).until(
                            ec.presence_of_element_located((By.XPATH, price_path))
                        )

                    print("◘ Price Extraction successful")
                    text_message = "◘ Checking for product description..."
                    print(text_message)

                    description_id = self.ctrl.get_description()
                    product_desc = WdW(self.temp_driver, 10).until(
                        ec.presence_of_element_located((By.ID, description_id))
                    )

                    text_message = "◘ Checking for product ratings..."
                    print(text_message)

                    rating_path = self.ctrl.get_rating()
                    rating = WdW(self.temp_driver, 10).until(
                        ec.presence_of_element_located((By.XPATH, rating_path))
                    )

                    text_message = "◘ Checking for total reviews..."
                    print(text_message)

                    total_reviews_id = self.ctrl.get_total_reviews_id()
                    total_rating = WdW(self.temp_driver, 10).until(
                        ec.presence_of_element_located((By.ID, total_reviews_id))
                    )

                    text_message = "◘ Checking specs for ASIN number...\n"
                    print(text_message)

                    asin_path = self.ctrl.get_asin_path()
                    specs = WdW(self.temp_driver, 10).until(
                        ec.presence_of_all_elements_located((By.XPATH, asin_path))
                    )

                    text_message = "◘ Information scraping successful\n"
                    print(text_message)

                except Exception as exc:
                    # Skip row if one fails
                    print("!!! Failure encountered at this line: " + text_message + ' !!!\n', exc)

                else:
                    print(product_name)
                    print(price.text.replace('\n', '.'))
                    print(product_desc.text)
                    print(rating.text)
                    print(total_rating.text)
                    print(link)

                    # Append if all conditions met
                    self.product_names.append(product_name)
                    self.prices.append(price.text.replace('\n', '.'))
                    self.product_desc.append(product_desc.text)
                    self.ratings.append(rating.text)
                    self.total_ratings.append(total_rating.text)
                    self.links.append(link)

                    # ASIN extraction
                    temp_list = []
                    for items in specs:
                        temp_list.append(items.text)

                    print(temp_list[2])
                    self.asin.append(temp_list[2])
                    print('-' * 50, '\n\n')

                finally:
                    t.sleep(1)
                    self.temp_driver.quit()

            self.current += 1

            # Pagination
            try:
                next_element_path = self.ctrl.get_next_element_path()
                next_element = self.driver.find_element(By.XPATH, next_element_path)

            except Exception as exc:
                print(exc)

            else:
                next_element.click()

            finally:
                self.driver.implicitly_wait(10)

        self.driver.quit()

    def store_data(self):
        # Structural integrity evaluation
        list_properties = [len(self.product_names), len(self.prices), len(self.product_desc),
                           len(self.ratings), len(self.total_ratings), len(self.links), len(self.asin)]
        print("\n◘ Displaying list properties -\n", list_properties)

        # Store to DataFrame upon successful evaluation
        if len(set(list_properties)) == 1:
            for row in range(0, len(self.product_names)):
                try:
                    self.df.loc[len(self.df)] = {'product_names': self.product_names[row], 'prices': self.prices[row],
                                                 'product_desc': self.product_desc[row], 'ratings': self.ratings[row],
                                                 'total_ratings': self.total_ratings[row], 'links': self.links[row],
                                                 'asin': self.asin[row]}

                except Exception as exc:
                    print('!!! Failed to store data at index #', row, ' !!!\n', exc)

            print("DataFrame storage successful")

        # Data set Storage
        try:
            self.df.to_csv('../../scraped_data/csv/amazon_products.csv', sep=',')
            self.df.to_excel('../../scraped_data/excel/amazon_products..xlsx')
            self.df.to_json('../../scraped_data/json/amazon_products.json')

        except Exception as exc:
            print("! ", exc)

        else:
            print("Data Storage successful!")


if __name__ == "__main__":
    drv = SeleniumDriver()
    drv.load_page()
    drv.get_data()
    drv.store_data()
