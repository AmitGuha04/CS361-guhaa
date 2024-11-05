import os
import json
from input import main as input_main
from search import main as search_main


def display_menu():
    print()
    print("Welcome to the Trail Management System!")
    print("With our system you can search for trails based on specific details! You can also add your own trails to our database!")
    print("1. Add a new trail")
    print("2. Search for trails")
    print("3. Exit")

def main():
    option = 4
    while option != 3:
        display_menu()
        option = int(input("Please choose from these options: "))
        while option < 1 or option > 3:
            option = int(input("Invalid Input. Please try again: "))

        if option == 1:
            input_main()
        elif option == 2:
            search_main()
    print("Thanks for running!")


if __name__ == "__main__":
    main()