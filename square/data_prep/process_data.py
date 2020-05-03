from datetime import date, time, datetime

import numpy as np
import pandas as pd

from square.utils.path_utils.data_path_builder import DataPathBuilder


class DataLoader(object):
    def __init__(self, year, event):
        self._path_builder = DataPathBuilder()
        self._transactions_file_path = self._path_builder.get_transactions_file_path(year, event)
        self._transactions = pd.read_csv(self._transactions_file_path)
        self.data = pd.DataFrame()
        self.__format_data()

    def __format_data(self):
        def date_formatter(d):
            d = d.split("/")
            return date(int('20' + d[2]), int(d[0]), int(d[1]))

        def time_formatter(t):
            t = t.split(":")
            return time(int(t[0]), int(t[1]), int(t[2]))

        money_formatter = lambda s: float(s.lstrip("$"))
        event_type_formatter = lambda x: 1 if 'Payment' in x else -1
        identity_formatter = lambda x: x

        columns_to_format = {"Date": ("date", date_formatter),
                             "Time": ("time", time_formatter),
                             "Gross Sales": ("gross_sale", money_formatter),
                             "Tax": ("tax", money_formatter),
                             "Discounts": ("discounts", money_formatter),
                             "Total Collected": ("total_sale", money_formatter),
                             "Cash": ("cash_collected", money_formatter),
                             "Other Tender": ("card_collected", money_formatter),
                             "Transaction ID": ("transaction_id", identity_formatter),
                             "Payment ID": ("payment_id", identity_formatter),
                             "Event Type": ("event_type", event_type_formatter),
                             "Details": ("url", identity_formatter),
                             "Description": ("description", identity_formatter),
                             "Device Name": ("device_name", identity_formatter)
                             }

        for old_c, new_c in columns_to_format.items():
            self.data[new_c[0]] = self._transactions[old_c].apply(new_c[1])
        self.data["date_time"] = np.vectorize(datetime.combine)(self.data["date"], self.data["time"])
        cols = self.data.columns.tolist()
        cols = [cols[-1]] + cols[2:-1]
        self.data = self.data[cols]


if __name__ == "__main__":
    r1 = DataLoader(2019, 'tirgan')
