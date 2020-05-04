import os
import shutil
from functools import wraps


def create_dir_if_necessary(get_dir_path_func):
    @wraps(get_dir_path_func)
    def wrapper(*args, **kwargs):
        dir_path = get_dir_path_func(*args, **kwargs)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
        return dir_path
    return wrapper


def merge_directories(root_src_dir, root_dst_dir):
    """
    This function copy-merges two directories.

    Args:
        root_src_dir (str): path to the source directory
        root_dst_dir (str): path to the destination directory
    """
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            shutil.copy(src_file, dst_dir)
