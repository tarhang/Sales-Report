import pandas as pd
import matplotlib.pyplot as plt

from square.utils.path_utils.data_path_builder import DataPathBuilder
from square.data_prep.process_data import DataLoader


class SalesReport(object):
    def __init__(self, year, event):
        self.year = year
        self.event = event
        self.path_builder = DataPathBuilder()
        self.data_loader = DataLoader(year, event)
        self.sales = self.data_loader.data.iloc[self.data_loader.data["event_type"].to_numpy() == 1]

    def get_mean_total_sale(self):
        return self.sales["total_sale"].mean()

    def get_mean_gross_sale(self):
        return self.sales["gross_sale"].mean()

    def get_median_total_sale(self):
        return self.sales["total_sale"].median()

    def get_median_gross_sale(self):
        return self.sales["gross_sale"].median()

    def plot_sales_distribution(self):
        fig = plt.hist(self.sales["total_sale"], bins=50, label=f"{self.event} {self.year}")
        plt.xlabel("sales amount ($)", fontsize=12)
        plt.ylabel("number of sales", fontsize=12)
        # plt.legend()
        plt.title(f"{self.event} {self.year} sales distribution", fontsize=14)
        plt.show()
        return fig

    def compute_sales_per_day(self):
        dates = self.data_loader.get_festival_dates()
        total_sales = []
        for day in dates:
            sales = self.data_loader.get_sales_on_date(day)
            total_sales.append(sales["total_sale"].sum())
        df = pd.DataFrame()
        df["dates"] = dates
        df["sales"] = total_sales
        return df

    def plot_daily_sales(self):
        sales = self.compute_sales_per_day()
        fig = plt.bar(sales["dates"], sales["sales"], label=f"{self.event} {self.year}")
        plt.xlabel("festival days", fontsize=12)
        plt.ylabel("total sales ($)", fontsize=12)
        plt.title(f"{self.event} {self.year} daily sales", fontsize=14)
        # plt.legend()
        plt.show()
        return fig


if __name__ == "__main__":
    f = SalesReport(2019, 'tirgan')
    fig = f.plot_sales_distribution()
