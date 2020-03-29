import os
from functools import wraps


def check_if_dir_exists(get_dir_path_func):
    @wraps(get_dir_path_func)
    def wrapper(*args, **kwargs):
        path = get_dir_path_func(*args, **kwargs)
        if not os.path.isdir(path):
            os.makedirs(path)
        return path
    return wrapper


def check_if_file_exists(get_file_path_func):
    @wraps(get_file_path_func)
    def wrapper(*args, **kwargs):
        path = get_file_path_func(*args, **kwargs)
        if not os.path.isfile(path):
            return False
        return path
    return wrapper
