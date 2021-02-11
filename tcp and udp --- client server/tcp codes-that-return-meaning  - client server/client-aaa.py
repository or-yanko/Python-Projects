import socket
#tcp!!!!!!!!!!!!!!
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #open socket
my_socket.connect(("127.0.0.1", 8821))  #connecting to the socket

data = ""
while data != "Bye":
    msg = input("please enter your massage:  ")
    my_socket.send(msg.encode())    #send data to server
    data = my_socket.recv(1024).decode()    #get data from the server
    print("the server sent: " + data)

my_socket.close()   #close socket
