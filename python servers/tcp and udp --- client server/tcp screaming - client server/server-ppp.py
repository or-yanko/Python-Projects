import socket
#tcp!!!!!!!!!!!!!!
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #open socket
server_socket.bind(("0.0.0.0", 8822)) #listen to requests
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
        data = data.upper() + '!!!'
        client_socket.send(data.encode())
    client_socket.close()   #close the connection
server_socket.close()   #close the socket