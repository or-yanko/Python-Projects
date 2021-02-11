import socket
SERVER_IP = "127.0.0.1"
PORT = 8821
MAX_SMG_SIZE = 1024

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    inpt = input("enter msg: ")
    my_socket.sendto(inpt.encode(), (SERVER_IP, PORT))
    if inpt.lower() == 'exit':
        break
    (response, address) = my_socket.recvfrom(MAX_SMG_SIZE)
    data = response.decode()
    print('the server sent: ' + data)

my_socket.close()