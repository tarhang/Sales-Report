from square.utils.path_utils.abstract_path_builder import *


class DataPathBuilder(object):
    def __init__(self):
        self._DATA = os.path.join(os.path.dirname(os.getcwd()), 'data')

    @check_if_dir_exists
    def get_data_dir_path(self):
        return self._DATA

    @check_if_dir_exists
    def get_event_dir_path(self, year, event):
        return os.path.join(self.get_data_dir_path(), f"{year}_{event}")

    @check_if_file_exists
    def get_transactions_file_path(self, year, event):
        root = self.get_event_dir_path(year, event)
        for file in os.listdir(root):
            if f"transactions-{year}" in file:
                return os.path.join(root, file)


d = DataPathBuilder()
print(d.get_transactions_file_path(2019, 'tirgan'))