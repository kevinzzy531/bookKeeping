import json
from constants import TransactionType
from model import DataItem, Transaction




if __name__ == "__main__":
    transactions = []
    transactions.append(Transaction(timestamp=14, category=TransactionType.MEAL, value=16.6))
    data_item = DataItem(date="2022-07-17", transactions=transactions)
    print("everything is fine")