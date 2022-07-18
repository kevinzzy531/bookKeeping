from utils import print_menu
from user_inputs import menu_user_input
from constants import TransactionType, UserInteraction, menu_options, type_options
if __name__ == "__main__":
    while True:
        print_menu(menu_options)
        menu_choice = input()
        menu_user_input(UserInteraction(int(menu_choice)))
        