import socket
from PIL import Image

# Server socket setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5050)
server_socket.bind(server_address)
server_socket.listen(1)

print("Waiting for a client to connect...")

# Accept connection from client
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} established.")

# Receive image data
image_data = client_socket.recv(4096)
received_data = bytearray()

while image_data:
    received_data += image_data
    image_data = client_socket.recv(4096)

# Write received image data to a file
with open('received_image.jpg', 'wb') as img_file:
    img_file.write(received_data)
im = Image.open('received_image.jpg')
im.show()

print("Image received and saved.")

client_socket.close()
server_socket.close()