from enum import Enum

class TransactionType(Enum):
    MEAL = 1
    TRANSPORTATION = 2
    ENTERTAINMENT = 3
    GROCERY = 4

class UserInteraction(Enum):
    QUERY = 1
    ADD = 2
    EXIT = 3


menu_options = {
    1: "Query",
    2: "Add a Transaction",
    3: "Exit"
}

type_options = {
    1: "Meal",
    2: "Transportation",
    3: "Entertainment",
    4: "Grocery"
}

dataSource = "../data"

date_options = {
    1: "Today",
    2: "Pick another day in the past"
}

inputDateDialogue = "Please input a date (yyyy-mm-dd): "

inputValueDialogue = "Please input a transaction value: "