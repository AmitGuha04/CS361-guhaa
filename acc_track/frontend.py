# Frontend Code aka Client

import zmq
import os
import json

DATA_FILE = 'accounts.json'

# Initialize ZeroMQ context and socket (REQ - Request)
context = zmq.Context()
socket = context.socket(zmq.REQ)  # REQ socket type for request-reply pattern
socket.connect("tcp://localhost:5555")  # Connect to the server

# Read all accounts from JSON file
def read_accounts():
    """Read accounts from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as g:
        try:
            return json.load(g)
        except json.JSONDecodeError:
            return {}


def create_account():
    # Read all accounts    
    accounts = read_accounts()
    
    # Error checking for username (can also be done on server side)
    while True:
        usern = input("Enter your username: ")
        if usern in accounts:
            print("Account exists. Please try again...")
        else:
            break

    # Error checking for password (can also be done server side)
    while True:
        passw = input("Enter a new password: ")
        passcon = input("Confirm your new password: ")
        if passw != passcon:
            print("Passwords do not match...")
        else:
            break
    
    # Send request to server
    socket.send_json({"action": "create", "username": usern, "password": passw})

    # Receive response from server
    response = socket.recv_json()
    print(response["response"])

def login():
    # Log in to an existing account
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Send request to server
    socket.send_json({"action": "login", "username": username, "password": password})

    # Receive response from server
    response = socket.recv_json()
    print(response["response"])

def main():
    # Initial Print
    print("Welcome to the account system.")
    action = input("Would you like to create an account or log in? (create/login): ").lower()

    # Ask if user wants to create or login
    if action == "create":
        create_account()
    elif action == "login":
        login()
    else:
        print("Invalid option. Please choose 'create' or 'login'.")

if __name__ == "__main__":
    main()
