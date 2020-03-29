import pandas as pd

from square.utils.path_utils.data_path_builder import DataPathBuilder


class SalesReport(object):
    def __init__(self, year, event):
        self.path_builder = DataPathBuilder()
        self.transactions_file = self.path_builder.get_transactions_file_path(year, event)
        self.data = pd.read_csv(self.transactions_file)


if __name__ == "__mcleaain__":
    r1 = SalesReport(2019, 'tirgan')
