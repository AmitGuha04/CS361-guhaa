# Backend Code aka Server

import zmq
import bcrypt
import json
import os

DATA_FILE = 'accounts.json'

# Initialize ZeroMQ context and socket (REP - Reply)
context = zmq.Context()
socket = context.socket(zmq.REP)  # REP socket type for request-reply pattern
socket.bind("tcp://*:5555")  # Listen on TCP port 5555

# Load accounts from JSON file
def read_accounts():
    # Read accounts from the JSON file
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as g:
        try:
            return json.load(g)
        except json.JSONDecodeError:
            return {}

# Write back to JSON file
def write_accounts(accounts):
    # Write accounts to the JSON file
    with open(DATA_FILE, 'w') as f:
        json.dump(accounts, f, indent=4)

# Given username and password, create the account
def create_account(usern, passw):
    # Handle account creation
    accounts = read_accounts()

    # Hash the password using bcrypt
    hashed = bcrypt.hashpw(passw.encode(), bcrypt.gensalt())
    accounts[usern] = hashed.decode()  # Store the hash as a string
    
    # Write updated accounts back to JSON file
    write_accounts(accounts)
    return f"Account created for {usern}"

# Given username and password create the account
def handle_login(usern, passw):
    # Handle login
    accounts = read_accounts()
    if usern not in accounts:
        return "Account not found"

    stored_hash = accounts[usern].encode()
    if bcrypt.checkpw(passw.encode(), stored_hash):
        return f"Login successful! Welcome back, {usern}"
    else:
        return "Incorrect password"

while True:
    # Receive the request from the client
    message = socket.recv_json()
    action = message.get("action")
    usern = message.get("username")
    passw = message.get("password")

    # Depending on what has been recieved, create or login
    if action == "create":
        response = create_account(usern, passw)
    elif action == "login":
        response = handle_login(usern, passw)
    else:
        response = "Invalid action"

    # Send the response back to the client
    socket.send_json({"response": response})
