import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib.font_manager import FontProperties


class DataAnalysis:
    def __init__(self):
        # Load scraped data
        df = pd.read_csv('AmazonProducts.csv')
        print('• DataFrame Information: \n', df.info)

        # Load important attributes
        self.ratings = df['ratings']
        self.prices = df['prices']
        self.rating_lists = []
        self.price_lists = []

        print('-'*30, '\n', self.ratings.describe())
        print(self.prices.describe(), '\n')

    @staticmethod
    def graph_settings():
        # Customizable Set-ups
        plt.figure(figsize=(12, 16))
        font = FontProperties()
        font.set_family('serif bold')
        font.set_style('oblique')
        font.set_weight('bold')
        ax = plt.axes()
        ax.set_facecolor("#e6eef1")

    def data_structures(self):
        # Filter Data
        for row in range(0, len(self.ratings)):
            self.rating_lists.append(self.ratings[row].split()[0])

        for row in range(0, len(self.prices)):
            self.price_lists.append(self.prices[row].replace('$', ''))

        print('-'*30, '\nRatings: ', self.rating_lists)
        print('Prices: ', self.price_lists, '\n', '-'*30, '\n')
        pass

    def line_graph(self):
        # Axis Initialization
        self.data_structures()
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


if __name__ == "__main__":
    data = DataAnalysis()
    data.line_graph()
