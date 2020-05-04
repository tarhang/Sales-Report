from datetime import time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from square.utils.path_utils.data_path_builder import DataPathBuilder
from square.data_prep.process_data import DataLoader


class SalesReport(object):
    def __init__(self, year: int, event: str):
        self.year = year
        self.event = event
        self.path_builder = DataPathBuilder()
        self.data_loader = DataLoader(year, event)
        self.data = self.data_loader.data.iloc[self.data_loader.data["event_type"].to_numpy() == 1]

    def compute_mean_total_sale(self):
        return self.data["total_sale"].mean()

    def compute_mean_gross_sale(self):
        return self.data["gross_sale"].mean()

    def compute_median_total_sale(self):
        return self.data["total_sale"].median()

    def compute_median_gross_sale(self):
        return self.data["gross_sale"].median()

    def compute_total_sales_per_day(self):
        dates = self.data_loader.get_festival_dates()
        total_sales = []
        for day in dates:
            sales = self.data_loader.get_sales_on_date(day)
            total_sales.append(sales["total_sale"].sum())
        df = pd.DataFrame()
        df["dates"] = dates
        df["sales"] = total_sales
        return df

    def compute_total_sales_in_hour(self, hour: int):
        data = self.data_loader.get_sales_in_hour(hour)
        return data["total_sale"].sum()

    def compute_per_hour_sales_amount(self):
        earliest = self.data.loc[self.data["time"] == self.data["time"].min()]
        latest = self.data.loc[self.data["time"] == self.data["time"].max()]
        h_start = earliest.at[earliest.index[0], "time"].hour
        h_end = latest.at[latest.index[0], "time"].hour
        sales, hours = [], [time(i) for i in range(h_start, h_end + 1)]

        for hour in range(h_start, h_end + 1):
            df = self.data_loader.get_sales_in_hour(hour)
            sales.append(df["total_sale"].sum())

        df = pd.DataFrame()
        df["hour"] = hours
        df["sales"] = sales
        return df

    def plot_daily_sales_amount(self):
        sales = self.compute_total_sales_per_day()
        plt.bar(sales["dates"], sales["sales"], label=f"{self.event} {self.year}", linewidth=1, edgecolor='k')
        plt.ylabel("total sales ($)", fontsize=12)
        plt.title(f"[{self.event} {self.year}] daily sales", fontsize=14)
        plt.legend(fontsize=12)
        plt.show()

    def plot_sales_amount_distribution(self):
        plt.hist(self.data["total_sale"], bins=50, label=f"{self.event} {self.year}", linewidth=1, edgecolor='k')
        plt.xlabel("sales amount ($)", fontsize=12)
        plt.ylabel("number of sales", fontsize=12)
        plt.legend(fontsize=12)
        plt.title(f"[{self.event} {self.year}] sales distribution", fontsize=14)
        plt.show()

    def plot_per_hour_sales_amount(self):
        df = self.compute_per_hour_sales_amount()
        hours = df["hour"].apply(lambda x: x.hour)
        plt.bar(df["hour"].apply(lambda x: x.hour), df["sales"], align='edge', label=f"{self.event} {self.year}", linewidth=1, edgecolor='k')
        plt.xticks(np.arange(hours.min(), hours.max() + 1))
        plt.xlabel("Hour of the day", fontsize=12)
        plt.ylabel("Sales amount ($)", fontsize=12)
        plt.legend(fontsize=12)
        plt.title(f"[{self.event} {self.year}] per hour sales", fontsize=14)
        plt.show()


if __name__ == "__main__":
    f = SalesReport(2019, 'tirgan')
    df = f.compute_per_hour_sales_amount()
    print(df)
    f.plot_per_hour_sales_amount()
