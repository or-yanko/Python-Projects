import socket
import threading


# function that handle the msg
def handle_msg(msg):
    msg = msg.decode("utf-8")
    return msg.encode("utf-8")


# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"[+] Accepted connection from {client_address[0]}:{client_address[1]}")

    while running:
        # Receive data from the client
        data = client_socket.recv(1024)
        print(f'[#] {client_address[0]}:{client_address[1]} says:"{data.decode("utf-8")}"')

        # handling the massage
        data = handle_msg(data)

        # see if to close connection
        if not data or data == 'q':
            break

        # Echo the received data back to the client
        print(f'[#] replaying to {client_address[0]}:{client_address[1]} :"{data.decode("utf-8")}"')
        client_socket.sendall(data)

    # Close the connection when done
    print(f"[-] closed connection with {client_address[0]}:{client_address[1]}")
    client_socket.close()
    client_threads.remove(threading.current_thread())


# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8888))
server.listen(5)

print("Server listening on port 8888...")

# List to hold active client threads
client_threads = []

# Flag to control the server loop
running = True


# Function to close the server
def close_server():
    global running
    print("Closing server...")
    running = False
    for thread in client_threads:
        try:
            thread.join()  # Wait for all client threads to finish
        except RuntimeError:
            pass

    server.close()  # Close the listening socket
    print("Server closed.")


# Function to continuously listen for the "q" command
def listen_for_command():
    while True:
        command = input("Enter 'q' to close , 'l' to list: ")
        if command.lower() == 'q':
            close_server()
            exit()
        if command.lower() == 'l':
            print(client_threads)


# Start a thread to listen for the "q" command
command_thread = threading.Thread(target=listen_for_command)
command_thread.start()

# Set a timeout for the server socket
server.settimeout(1)  # Adjust the timeout value as needed

# Accept incoming connections and handle them using threads
while running:
    try:
        if running:
            try:
                client, addr = server.accept()

                # Create a new thread to handle the client
                client_handler = threading.Thread(target=handle_client, args=(client, addr))
                client_handler.start()
                client_threads.append(client_handler)
            except socket.timeout:
                pass
    except KeyboardInterrupt:
        close_server()
        exit()
    except OSError as e:
        if e.errno == 10038:
            exit()