Amit Guha
OSU ID: 934-427-040

A bit of info before I show you how to call the code, ZeroMQ isn't able to call ohter programs meaning that any inputs I put in the backend wouldn't work correctly. Thus a lot of the user input is set up in the frontend.
Going more into depth, the first thing you need to do to run this program is make sure that your environment is set up correctly. To run code that includes the ZeroMQ and bcrypt libraries, you need to install the respective
packages which are:

pip install pyzmq
pip install bcrypt

Once your environment setup is complete, you will need to do a few things. First make sure to import the correct 'accounts.json' along with the zmq and bcrypt libraries like so:

import zmq
import bcrypt
DATA_FILE = "accounts.json"

After making sure you are reading and writting from the correct file and that the correct libraries are imported, you can set up the ZeroMQ context and socket. 
It is already set up in the backend so to set it up in the frontend correctly you will need to type:

# Initialize ZeroMQ context and socket (REQ - Request)
context = zmq.Context()
socket = context.socket(zmq.REQ)  # REQ socket type for request-reply pattern
socket.connect("tcp://localhost:5555")  # Connect to the server

Make sure that the socket you are connecting to is the same as the one the backend is binding to. This will allow the frontend to send and recieve messages from the backend if set up correctly.

From here, your main set up is complete and you can start coding the rest of the frontend. The main things to keep in mind is that you have to set up your own inputs and store them respectivly.
You also have to send info properly to the backend.
For example, on line 48-52 in frontend.py create_account function, this is how I send/recieve code to the backend:

# Send request to server
    socket.send_json({"action": "create", "username": usern, "password": passw})

    # Receive response from server
    response = socket.recv_json()
    print(response["response"])

The first line sends over three strings to the backend. You will need to use the same line of code, but replace the variable names accordingly (make sure to set the action to either "create" or "login" 
                                                                                                                                                based on which section you are implementing).
The second line is how you will recieve the correct response back from the backend. By printing the response on the third line, we will see exactly what the code was doing and what it achieved.



