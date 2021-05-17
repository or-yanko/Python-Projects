import socket
SERVER_IP = "127.0.0.1"  # Our server will run on same computer as client
SERVER_PORT = 5678
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #open socket
my_socket.connect(("127.0.0.1", SERVER_PORT))  #connecting to the socket

data = ""
while True:
    msg = input("please enter your massage:  ")
    my_socket.send(msg.encode())    #send data to server
    if msg.lower() == "exit":
        break
    data = my_socket.recv(1024).decode()    #get data from the server
    print("the server sent: " + data)

my_socket.close()   #close socket