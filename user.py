import socket, sys, random
from datetime import datetime
from colorama import Fore, init, Back

# This intialises Colorama
init()

#List of colours, code obtained from Rockikz (https://www.thepythoncode.com/article/make-a-chat-room-application-in-python#:~:text=A%20chat%20room%20is%20an,it%20using%20sockets%20in%20Python.)
colours = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]

# choose a random color for the client
user_colour = random.choice(colours)
#obatined code stops here 

#TCP socket
user_socket = socket.socket()
#Retreives IP address
user_server = socket.gethostname()
user_ip = socket.gethostbyname(user_server )
port = 5000

# This connects user to the server, infroms them of their IP address and asks for name 
user_socket.connect((user_server, port))
print('This is your IP address: ', user_ip)
user_server = input('Enter IP address:')
name = input('Enter name: ')


#Recieves messages from the server 
user_socket.send(name.encode())
username= user_socket.recv(1024)
username= username.decode()
 
print(username,' has joined...')
while True:
    message = (user_socket.recv(1024)).decode()
    print(username, ":", message)
    message = input("Me : ")
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    message = f"{user_colour}[{date}] {name}{message}{Fore.RESET}"
    user_socket.send(message.encode())  

user_socket.close()

#References 
#Anu(https://www.askpython.com/python/examples/create-chatroom-in-python)
#Rockikz (https://www.thepythoncode.com/article/make-a-chat-room-application-in-python#:~:text=A%20chat%20room%20is%20an,it%20using%20sockets%20in%20Python.)