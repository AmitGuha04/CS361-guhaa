#input.py (Inputs)

import json
import os
from bend import Road  # Import the Road class
from bend import load_roads


DATA_FILE = 'road_data.json'

def get_user_input():
    name = input("What is the name of the bike Trail: ")

    v_diff = ['easy', 'medium', 'hard']
    difficulty = input("Please enter a valid difficulty (Easy, Medium, Hard): ").lower()
    while difficulty.lower() not in v_diff:
        print("Invalid entry. Please try again...")
        difficulty = input("Please enter a valid difficulty (Easy, Medium, Hard): ").lower()

    location = input("Please enter a location: ")

    length_inp = input("Please enter length in miles: ")
    while True:  # Use a loop to keep asking until a valid input is received
        try:
            length = float(length_inp)
            break  # Valid input, exit the loop
        except ValueError:
            print("Invalid number. Please enter a valid FLOAT...")
            length_inp = input("Please enter length in miles: ")

    description = input("If you would like to, please type a description. Otherwise press enter: ")

    photos = input("Enter photos (comma-separated URLs or file paths). Otherwise press enter: ").split(',')

    new_road = Road(name, difficulty, location, length, description, photos)
    
    add_road_json(new_road)



def add_road_json(road):
    road_dict = road.to_dict()

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as json_file:
            try:
                roads = json.load(json_file)
            except json.JSONDecodeError:
                roads = []
    else:
        roads = []
    
    roads.append(road_dict)

    with open(DATA_FILE, 'w') as json_file:
        json.dump(roads, json_file, indent = 4)


#Look into tkinter library for photo by file choosen

def main():
    get_user_input()

if __name__ == "__main__":
    main()
    