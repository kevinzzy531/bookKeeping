from constants import (TransactionType,
                        UserInteraction, 
                        date_options, 
                        inputDateDialogue,
                        inputValueDialogue, 
                        type_options)
from dataWriter import dataWriter
from utils import print_menu
from datetime import date

def menu_user_input(option: UserInteraction) -> bool:
    if option == UserInteraction.QUERY:
        # TODO: implement query
        pass
    elif option == UserInteraction.ADD:
        # TODO: implement add
        print("add a transaction")
        date_str = date_user_input()
        category = category_user_input()
        value = value_user_input()
        print(f"{date_str}: {category} {value}")
        dataWriter.store_transaction(date_str, category, value)
    else:
        return False

def date_user_input() -> str:
    # return a yyyy-mm-dd date
    print_menu(date_options)
    date_option = input()
    if date_option == "1":
        return str(date.today())
    else:
        return input(inputDateDialogue)

def category_user_input() -> TransactionType:
    print_menu(type_options)
    return TransactionType(int(input()))

def value_user_input() -> float:
    return float(input(inputValueDialogue))

def add_transaction_user_input(date: str, category: str,  value: float):
    date = input()