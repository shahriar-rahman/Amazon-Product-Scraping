import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib.font_manager import FontProperties
data_path = "../../scraped_data/csv/amazon_products.csv"


class DataAnalysis:
    def __init__(self):
        # Load scraped data
        df = pd.read_csv(data_path)
        print('• DataFrame Information: \n', df.info)

        # Load attributes
        self.ratings = df['ratings']
        self.prices = df['prices']
        self.t_ratings = df['total_ratings']

        # Storage
        self.rating_lists = []
        self.price_lists = []
        self.t_rating_lists = []

        # Characteristics
        print('-'*30, '\n', self.ratings.describe())
        print(self.prices.describe(), '\n')
        print(self.t_ratings.describe(), '\n')

    @staticmethod
    def graph_settings():
        # Customization
        plt.figure(figsize=(12, 16))

        font = FontProperties()
        font.set_family('serif bold')
        font.set_style('oblique')
        font.set_weight('bold')

        ax = plt.axes()
        ax.set_facecolor("#e6eef1")

    def data_structures(self, sort):
        # Data filter
        for row in range(0, len(self.ratings)):
            self.rating_lists.append(self.ratings[row].split()[0])

        for row in range(0, len(self.prices)):
            self.price_lists.append(self.prices[row].replace('$', ''))

        for row in range(0, len(self.t_ratings)):
            self.t_rating_lists.append(self.t_ratings[row].split()[0])

        if sort == 'sort':
            self.rating_lists.sort(reverse=True)
            self.price_lists.sort(reverse=True)

        print('-'*30, '\nRatings: ', self.rating_lists)
        print('Prices: ', self.price_lists, '\n', '-'*30, '\n')
        print('Total Ratings: ', self.t_rating_lists, '\n', '-'*30, '\n')

    def line_graph(self):
        # Axis Initialization
        self.data_structures('sort')
        x = self.price_lists
        y = self.rating_lists
        self.graph_settings()

        # Line Plot
        sb.lineplot(x=x, y=y, color='#01636e')
        plt.title("Price vs Rating Graph")
        plt.xlabel('Item Price ($)', fontsize=15)
        plt.ylabel('Item Rating (out of 5★)', fontsize=15)
        plt.grid(axis='y')
        plt.show()

    def bar_graph(self):
        # Axis Initialization
        self.data_structures('non-sort')
        x = self.rating_lists
        y = self.t_rating_lists
        self.graph_settings()

        # Bar Plot
        plt.bar(x, y, color='#01636e', width=0.4)
        plt.title("Rating vs Number of Reviews Graph")
        plt.xlabel('Item Rating (out of 5★)', fontsize=15)
        plt.ylabel('Total Reviews', fontsize=15)
        plt.grid(axis='y')
        plt.show()


if __name__ == "__main__":
    data = DataAnalysis()
    data.line_graph()
    data.bar_graph()
