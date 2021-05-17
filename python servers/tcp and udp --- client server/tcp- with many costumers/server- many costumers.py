import socket
import select

SERVER_IP = "0.0.0.0"
PORT = 5555
MAX_SMG_SIZE = 1024

def print_client_sockets(client_sockets):
    for c in client_sockets:
        print("\t", c.getpeername())

def main():
    print("setting up server...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #open socket
    server_socket.bind((SERVER_IP, PORT)) #listen to requests
    server_socket.listen()  #listening
    print("listening for clients...")
    client_sockets = []
    #get info from the clients
    while True:
        (ready_to_read, ready_to_write, in_error) = select.select([server_socket] + client_sockets, [], [])
        for current_socket in ready_to_read:
            if current_socket is server_socket:
                (client_socket, client_adress) = current_socket.accept()
                print("new client joined ", client_adress, "(;")
                client_sockets.append(client_socket)

            else:
                try:
                    data = current_socket.recv(MAX_SMG_SIZE).decode()
                except:
                    data = ""
                if data.lower() == "exit" or data == "":
                    print("connection closed with ", current_socket.getpeername(), " ):")
                    client_sockets.remove(current_socket)
                    current_socket.close()
                else:
                    print("new data from ", current_socket.getpeername(),":", data)
                    current_socket.send(data.encode())


main()