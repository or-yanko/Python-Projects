import socket

# Client socket setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5050)
client_socket.connect(server_address)

# Read the image file
image_path = "C:\\Users\gilya\Desktop\image.png"
with open(image_path, 'rb') as img_file:
    image_data = img_file.read()

# Send image data to server
client_socket.sendall(image_data)

print("Image sent.")

client_socket.close()