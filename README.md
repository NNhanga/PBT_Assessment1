# PBT_Assessment1
PBT205 group project with Nenci, David and Taygan
#Chatting Application
##Prerequisites  
1. Python 3.x
2. Docker
3. RabbitMQ Docker image
4. Python libraries: pika, sys, os, socket, time 
##Setup
Install Python 3.x 
Install Docker and pull the RabbitMQ Docker image: docker pull rabbitmq:3-management
Install the required Python libraries: pip install pika (the rest do not require installation
##Running the program 
1. Start the RabbitMQ container: docker run -d --hostname my-rabbit --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
2. Start server in a terminal: python server.py
3. Start user in another terminal: python user.py


