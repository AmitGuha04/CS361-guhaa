#search.py (Search for Trail)

import os
import json
from bend import Road
from bend import load_roads

DATA_FILE = 'road_data.json'


def filter_road_ss(substring):
    ss_roads = []
    roads = load_roads()
    ss_roads = [road for road in roads if substring.lower() in road['Name: '].lower()]
    return ss_roads

def filter_difficulty(i_diff, ss_roads):
    diff_roads = []
    diff_roads = [road for road in ss_roads if road['Difficulty: '] == i_diff]
    return diff_roads


def filter_length(u_lim, l_lim, diff_roads):
    length_roads = []
    length_roads = [road for road in diff_roads if l_lim < road['Length: '] < u_lim]
    return length_roads[:10]

def main():
    filtered_roads = []
    print("Welcome to Trail Search")
    print("You can filter by name, difficulty, and length.")

    ss = input("Which name would you like to filter by: ")
    filtered_roads = filter_road_ss(ss)

    diff = input("What difficulty would you like to filter by (Easy, Medium, Hard): ").lower()
    list_diff = ['easy', 'medium', 'hard']
    while diff.lower() not in list_diff:
        print("Invalid entry. Please try again...")
        diff = input("Please enter a valid difficulty (Easy, Medium, Hard): ").lower()
    filtered_roads = filter_difficulty(diff, filtered_roads)

    upper_lim = float(input("What is the max length you are looking for: "))
    lower_lim = float(input("What is the min length you are looking for: "))
    while lower_lim >= upper_lim:
        lower_lim = float(input("That is an invalid min length. Please re-enter: "))

    filtered_roads = filter_length(upper_lim, lower_lim, filtered_roads)

    if not filtered_roads:
        print("No filtered roads found...")
    else:
        print("Filtered Roads: ")
        for index, road in enumerate(filtered_roads, start=1):
            print(f"{index}. {road['Name: ']}, {road['Difficulty: ']}, {road['Length: ']} miles")
        choice = int(input("Enter the corresponding number to get more info on a trail (0 to exit)"))

        if 1 <= choice <= len(filtered_roads):
            selected_road = filtered_roads[choice - 1]
            print()
            print(f"Extended info on {selected_road['Name: ']}: ")
            print(f"Difficulty: {selected_road['Difficulty: ']}")
            print(f"Location: {selected_road['Location: ']}")
            print(f"Length: {selected_road['Length: ']} miles")
            print(f"Description: {selected_road['Description: ']}")
            #Use code from assignment 1 to display photos here
        elif choice == 0:
            print("Thanks for using the Trail Search!")
            return
        else:
            print("No valid number entered...")

if __name__ == "__main__":
    main()

