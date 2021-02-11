import socket
import datetime
import random
#tcp!!!!!!!!!!!!!!
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #open socket
server_socket.bind(("0.0.0.0", 8821)) #listen to requests
server_socket.listen()  #listening
print("server is up and running")

for i in range(5):

    (client_socket, client_adress) = server_socket.accept() #קבלת קישור
    print("client connected")

    while True:
        data = client_socket.recv(1024).decode()    #קבלת ושליחית ההודעות
        print("Client sent: " + data)
        if data == "q" or data == "Q":
            print("closing client socket")
            client_socket.send("Bye".encode())
            break
        elif data.upper() == "NAME":
            client_socket.send("my name is forest gump".encode())
        elif data.upper() == "TIME":
            client_socket.send((datetime.datetime.now().strftime("%H:%M:%S")).encode())
        elif data.upper() == "RAND":
            client_socket.send(str(random.randrange(1, 10)).encode())
        else:
            client_socket.send(data.encode())
    client_socket.close()   #close the connection
server_socket.close()   #close the socket