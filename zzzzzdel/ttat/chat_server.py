import socket
import threading

# Function to handle receiving messages from client
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print("Client: ", message)
        except ConnectionResetError:
            break

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 5050)

# Bind the server to the address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)
print("Waiting for incoming connections...")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

# Create a thread to receive messages from the client
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Send messages to the client
while True:
    message = input("")
    client_socket.sendall(message.encode())