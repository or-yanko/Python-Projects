import socket
import threading

# Function to handle receiving messages from server
def receive_messages(server_socket):
    while True:
        try:
            message = server_socket.recv(1024).decode()
            print("Server: ", message)
        except ConnectionResetError:
            break

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 5050)

# Connect to the server
client_socket.connect(server_address)
print("Connected to the server")

# Create a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Send messages to the server
while True:
    message = input("")
    client_socket.sendall(message.encode())