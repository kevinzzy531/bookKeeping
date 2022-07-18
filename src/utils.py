from fileinput import filename
from os import path, mkdir
def print_menu(options: dict):
    print("-----------------------")
    for key in options.keys():
        print(f"{key} --- {options[key]}")
    print("-----------------------")


def create_folder_if_not_exist(source_path: str,  folder_name: str) -> bool:
    folder_path = path.join(source_path, folder_name)
    if (check_file_exist(folder_path)):
        return False
    mkdir(folder_path)
    return True


def check_file_exist(file_name: str):
    return path.exists(file_name)

def get_year_month_from_date(date: str):
    return date[:7]