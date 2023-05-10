# Objective: Scrape product specs based on a search on Amazon
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as WdW
import time as t
import pandas as pd


class SeleniumDriver:
    def __init__(self):
        # Driver Set-ups
        start_urls = 'https://www.amazon.com/'
        self.product_search = "iphone"
        self.options = ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument('--headless')

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

    @staticmethod
    def popup_handler(driver):
        # Supress popups
        try:
            popup = WdW(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="nav-main"]/div[1]/div/div/div[3]/span[1]/'
                                                          'span/input'))
            )

        except Exception as exc:
            print("!!! Popup did not appear. !!!\n", exc)

        else:
            popup.click()

    def load_page(self):
        # Initiate search page
        try:
            self.popup_handler(self.driver)

            text_box = WdW(self.driver, 5).until(
                ec.presence_of_element_located((By.ID, "twotabsearchtextbox"))
            )

        except Exception as exc:
            print("!!! Failed to locate the text box !!!\n", exc)

        else:
            text_box.clear()
            text_box.send_keys(self.product_search)
            text_box.send_keys(Keys.ENTER)

        finally:
            self.driver.implicitly_wait(10)

    def access_links(self):
        # Nested Pagination
        print('-'*50, '\n' + "◘ Accessing Links...")
        temp_container = []

        try:
            get_links = WdW(self.driver, 15).until(
                ec.presence_of_all_elements_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), '
                                                               'concat( " ", "a-link-normal", " " )) and '
                                                               'contains(concat( " ", @class, " " ), '
                                                               'concat( " ", "s-link-style a-text-normal", " " ))]'))
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
                    try:
                        price = WdW(self.temp_driver, 10).until(
                            ec.presence_of_element_located((By.XPATH, '//span[contains(@class, "apexPriceToPay")]'))
                        )

                    except Exception as exc:
                        print("!!! Exception encountered for first attempt during price search !!!\n", exc)
                        price = WdW(self.temp_driver, 10).until(
                            ec.presence_of_element_located((By.XPATH,'//div[contains(@id, "corePrice_feature_div")]'))
                        )

                    text_message = "◘ Checking for product description..."
                    print(text_message)
                    product_desc = WdW(self.temp_driver, 10).until(
                        ec.presence_of_element_located((By.ID, 'feature-bullets'))
                    )

                    text_message = "◘ Checking for product ratings..."
                    print(text_message)
                    rating = WdW(self.temp_driver, 10).until(
                        ec.presence_of_element_located((By.XPATH, '//span[@data-hook = "rating-out-of-text"]'))
                    )

                    text_message = "◘ Checking for total reviews..."
                    print(text_message)
                    total_rating = WdW(self.temp_driver, 10).until(
                        ec.presence_of_element_located((By.ID, 'acrCustomerReviewText'))
                    )

                    text_message = "◘ Checking specs for ASIN number...\n"
                    print(text_message)
                    specs = WdW(self.temp_driver, 10).until(
                        ec.presence_of_all_elements_located((By.XPATH, '//td[@class = "a-size-base prodDetAttrValue"]'))
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
                next_element = self.driver.find_element(By.XPATH, '//a[contains(@class, "s-pagination-next")]')

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
        self.df.to_csv('AmazonProducts.csv', sep=',')
        self.df.to_xml('AmazonProducts.xml')
        self.df.to_json('AmazonProducts.json')


if __name__ == "__main__":
    drv = SeleniumDriver()
    drv.load_page()
    drv.get_data()
    drv.store_data()
