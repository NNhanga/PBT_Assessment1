import socket, pika,  time, sys

# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# channel = connection.channel()
# channel.exchange_declare('test', durable=True, exchange_type='topic')
# channel.queue_declare(queue='chat')
# channel.queue_bind(exchange='test', queue='chat', routing_key='chat')
# channel.basic_publish(exchange='test', routing_key='chat', body= '')
# channel.close()


#Finds the IP Address and stores it
server = socket.socket()
ip = socket.gethostname()
ip_store = socket.gethostbyname(ip)
 
port = 37775

#Binds the IP address and port 
server.bind((ip, port))

#When connected user will be welcomed and promted to enter name
print ("WELCOME!")
name = input('Enter name: ')

#Listens for connections for up to 100
server.listen(100) 

#Accepts new connections
connection = server.accept()

#Stores incoming connections and prints the name of who has connected
user = (connection.recv(1024)).decode()
print(user + ' has connected.')
connection.send(name.encode())

# This delivers messages to users.
while True:
    message = input('Me : ')
    connection.send(message.encode())
    message = connection.recv(1024)
    message = message.decode()
    print(user, ':', message)

    server.close


   
#Reference: https://www.askpython.com/python/examples/create-chatroom-in-python