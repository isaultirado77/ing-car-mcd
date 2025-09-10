"""Colection of utilitary functions"""

import pathlib
from datetime import datetime

def get_all_file_names(path): 
    path_ = pathlib.Path(path)
    files_in_basepath = [item.name for item in path_.iterdir() if item.is_file()]
    return files_in_basepath

def get_all_subdirs_names(path): 
    path_ = pathlib.Path(path)
    subdirs_in_basepath = [item.name for item in path_.iterdir() if item.is_dir()]
    return subdirs_in_basepath

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y') 
    return formated_date

if __name__ == '__main__':
    path = "../"
    print(get_all_file_names(path))
    print(get_all_subdirs_names(path))