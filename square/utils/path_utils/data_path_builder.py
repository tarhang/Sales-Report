from glob import glob

from square.utils.path_utils.abstract_path_builder import *


class DataPathBuilder(object):
    def __init__(self):
        self._DATA = os.path.join(os.path.dirname(os.getcwd()), 'data')

    @create_dir_if_necessary
    def get_data_dir_path(self):
        return self._DATA

    @create_dir_if_necessary
    def get_event_dir_path(self, year, event):
        return os.path.join(self.get_data_dir_path(), f"{year}_{event}")

    def get_transactions_file_path(self, year, event):
        root = self.get_event_dir_path(year, event)
        return glob(os.path.join(root, f"transactions-{year}*.csv"))[0]
