import socket
SERVER_IP = "0.0.0.0"
PORT = 8821
MAX_SMG_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, PORT))

while True:
    (msg, addres) = server_socket.recvfrom(MAX_SMG_SIZE)
    data = msg.decode()
    if data.lower() == 'exit':
        break
    print('client sent: ' + data)
    response = 'Super' + data
    server_socket.sendto(response.encode(), addres)

server_socket.close()