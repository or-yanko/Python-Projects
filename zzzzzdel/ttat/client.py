import socket

# Create a client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(('localhost', 8888))

# Send messages to the server
message=" "
while message!="q":
    message = input("Enter a message to send: ")
    if message=='':
        continue
    client.sendall(message.encode())

    # Receive the echoed message from the server
    data = client.recv(1024)
    print("Server sent:", data.decode())

# Close the client socket
client.close()