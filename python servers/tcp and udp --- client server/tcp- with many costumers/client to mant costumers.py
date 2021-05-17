import socket
#
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #open socket
my_socket.connect(("127.0.0.1", 5555))  #connecting to the socket

data = ""
while True:
    msg = input("please enter your massage:  ")
    my_socket.send(msg.encode())    #send data to server
    if msg.lower() == "exit":
        break
    data = my_socket.recv(1024).decode()    #get data from the server
    print("the server sent: " + data)

my_socket.close()   #close socket