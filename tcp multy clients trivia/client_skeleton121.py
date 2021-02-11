import socket
import time
import chatlib  # To use chatlib functions or consts, use chatlib.****

SERVER_IP = "127.0.0.1"  # Our server will run on same computer as client
SERVER_PORT = 5678

# HELPER SOCKET METHODS

def build_and_send_message(conn, code, data):
    """
    Builds a new message using chatlib, wanted code and message.
    Prints debug info, then sends it to the given socket.
    Paramaters: conn (socket object), code (str), data (str)
    Returns: Nothing
    """
    # Implement Code
    msg = chatlib.build_message(code, data)
    conn.send(msg.encode())    #send data to server
    print('data sent -> command: '+code+'   data: '+data)

def recv_message_and_parse(conn):
    """Recieves a new message from given socket,
    then parses the message using chatlib.
    Paramaters: conn (socket object)
    Returns: cmd (str) and data (str) of the received message.
    If error occured, will return None, None"""
    full_msg = conn.recv(1024).decode()    #get data from the server
    cmd, data = chatlib.parse_message(full_msg)
    print('data recieved -> command: ', cmd, '   data: ', data)
    return cmd, data

def connect():
    # Implement Code
    my_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # open socket
    my_socket.connect((SERVER_IP, SERVER_PORT))  # connecting to the socket
    return my_socket

def error_and_exit(error_msg):
    print(error_msg)
    exit(1)

def login(conn):
    while True:
        username = input("Please enter username: \t")
        password = input("Please enter password: \t")
        # Implement code
        txt = chatlib.join_data([username, password])

        build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["login_msg"], txt)

        # Implement code
        retcmd, retdata = recv_message_and_parse(conn)
        print(retcmd)
        if retcmd == "LOGIN_OK":
            print("logined sucesfully")
            break
        print("login failed, try again")

def logout(conn):
    build_and_send_message(conn, "LOGOUT", "")

def build_send_recv_parse(conn, cmd, data):
    build_and_send_message(conn, cmd, data)
    cmd1, data1 = recv_message_and_parse(conn)
    if cmd1.upper() == 'ERROR':
        error_and_exit(data1)
    return cmd1, data1

def get_score(conn):
    cmd, data = build_send_recv_parse(conn, "MY_SCORE", "")
    if cmd == 'ERROR':
        error_and_exit("error geting the score")
    print("your score is: "+data)

def get_highscore(conn):
    cmd, data = build_send_recv_parse(conn, "HIGHSCORE", "")
    if cmd == 'ERROR':
        error_and_exit("error geting the score")
    print("your high score is: " + data)

def play_question(conn):
    cmd, question = build_send_recv_parse(conn, "GET_QUESTION", "")
    lst = question.split('#')
    if cmd == 'NO_ANSWERS':
        error_and_exit("game over! no more questions!!!")
    id1 = lst[0]
    print(lst[1])
    print('1) ' + lst[2] + '\t2) ' + lst[3])
    print('3) ' + lst[4] + '\t4) ' + lst[4])
    ansnum = -1
    while not (0 < int(ansnum) < 5):
        ansnum = input("---------your answer: ")
    cmd, answer = build_send_recv_parse(conn, "SEND_ANSWER", str(str(id1)+'#'+str(ansnum)))
    if cmd == 'WRONG_ANSWER':
        print('wrong!  correct answer is: ' + answer)
    elif cmd == 'CORRECT_ANSWER':
        print('correct!!!')

def get_logged_user(conn):
    cmd, data = build_send_recv_parse(conn, "LOGGED", "")
    if cmd == 'ERROR':
        error_and_exit("error in get_logged_user")
    print('all scores:\n', data)


def main():
    my_socket = connect()
    login(my_socket)

    while True:
        ch = input("""------------------------------------------------------
press play or p to get a question
press logged users or l to get all loged users
press score or s to see your score
press quit or q to log out
please enter your choice: """)
#print("press play highscore or h to see the highest scores")
        if ch.upper() == 'LOGGED USERS'or ch.upper() == 'L':
            get_logged_user(my_socket)
        elif ch.upper() == 'PLAY' or ch.upper() == 'P':
            play_question(my_socket)
        #elif ch.upper() == 'HIGHSCORE' or ch.upper() == 'H':
        #   get_highscore(my_socket)
        elif ch.upper() == 'SCORE' or ch.upper() == 'S':
            get_score(my_socket)
        elif ch.upper() == 'QUIT' or ch.upper() == 'Q':
            break

    # Implement code
    logout(my_socket)
    time.sleep(3)
    my_socket.close()  # close socket

if __name__ == '__main__':
    main()
