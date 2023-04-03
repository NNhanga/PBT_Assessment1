import time, socket, sys, os

""" def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='queue1')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='queue1', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

  """

#the ip address is retrived by ip_user, ipu_store stores the ip address and port_store stroes the port
user_server = socket.socket()
ip_user = socket.gethostname()
ipu_store = socket.gethostbyname(ip_user)
port_store = 5555
#User is asked to input ther IP Address and name 
ip_user = input('Enter IP address:')
name = input('Enter name: ')

#The server and port are connected to the socket 
user_server.connect((ip_user, port_store))

#Receiving messages from the server 
user_server.send(name.encode())
user_name = user_server.recv(1024)
user_name = user_name.decode()

print(user_name,' joined!...')
while True:
    message = (user_server .recv(1024)).decode()
    print(user_name, ":", message)
    message = input("Me : ")
    user_server .send(message.encode())

user_server.close()

#Reference: https://www.askpython.com/python/examples/create-chatroom-in-python