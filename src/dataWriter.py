import json
from constants import TransactionType, dataSource, type_options
from model import DataItem, Transaction
from utils import (create_folder_if_not_exist, 
                    check_file_exist, 
                    get_year_month_from_date)
import os.path

class dataWriter:
    @classmethod
    def store_transaction(cls, date: str, category: TransactionType, value: float) -> None:
        # date format: yyyy-mm-dd
        year_month = get_year_month_from_date(date)
        create_folder_if_not_exist(dataSource, year_month)
        json_file_name = f"{os.path.join(dataSource, year_month, date)}.json"
        if (not check_file_exist(json_file_name)):
            cls.init_json_file(json_file_name, date)
        

    @classmethod
    def init_json_file(cls, json_file_name: str, date: str) -> None:
        data = DataItem(date=date, transactions=[], total_cost=0.0, report=[0 for _ in range(len(type_options))])
        f = open(json_file_name, "w+")
        f.write(data.json())
        f.close()

if __name__ == "__main__":
    transactions = []
    transactions.append(Transaction(timestamp=14, category=TransactionType.MEAL, value=16.6))
    data_item = DataItem(date="2022-07-17", transactions=transactions)
