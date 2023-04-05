import socket, sys


#TCP socket
server = socket.socket()
#Retreives IP address
ip = socket.gethostname()
server_ip = socket.gethostbyname(ip)
port = 5000

# bind the socket to the IP and port we specified
server.bind((ip, port))
print("This is your IP: ", server_ip)
name = input('Enter name:')

# listens for connections, currently can hold 10 connections
server.listen(10)

#Accepts incoming connections
socket_s, user_ip = server.accept()

#Stores all the availabe users
user_sockets = set()

#stores the connection data sends the messages
user = (socket_s.recv(1024)).decode()
print(user + ' has connected.')
socket_s.send(name.encode())


while True:
    message = input('Me : ')
    socket_s.send(message.encode())
    message = socket_s.recv(1024)
    message = message.decode()
    print(user, ':', message)


# close server socket
server.close()


#References
#Anu(https://www.askpython.com/python/examples/create-chatroom-in-python)