import socket
import chatlib
import select

# GLOBALS
clients_sockets = []
users = {}
questions = {}
logged_users = {} # a dictionary of client hostnames to usernames - will be used later

ERROR_MSG = "Error! "
SERVER_PORT = 5678
SERVER_IP = "127.0.0.1"


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
	print("send:", data, "to", conn.getpeername())

def recv_message_and_parse(conn):
	"""Recieves a new message from given socket,
	then parses the message using chatlib.
	Paramaters: conn (socket object)
	Returns: cmd (str) and data (str) of the received message.
	If error occured, will return None, None"""
	full_msg = str(conn.recv(1024).decode())  # get data from the server
	(cmd, data) = chatlib.parse_message(full_msg)
	print((conn.getpeername(), " sent:", data))
	return cmd, data

# Data Loaders #

def load_questions():
	"""
	Loads questions bank from file	## FILE SUPPORT TO BE ADDED LATER
	Recieves: -
	Returns: questions dictionary
	"""
	questions = {
				2313 : {"question":"How much is 2+2","answers":["3","4","2","1"],"correct":2},
				4122 : {"question":"What is the capital of France?","answers":["Lion","Marseille","Paris","Montpellier"],"correct":3}
				}

	return questions

def load_user_database():
	"""
	Loads users list from file	## FILE SUPPORT TO BE ADDED LATER
	Recieves: -
	Returns: user dictionary
	"""
	users = {
			"test"		:	{"password":"test","score":0,"questions_asked":[]},
			"yossi"		:	{"password":"123","score":50,"questions_asked":[]},
			"master"	:	{"password":"master","score":200,"questions_asked":[]}
			}
	return users

# SOCKET CREATOR

def setup_socket():
	"""
	Creates new listening socket and returns it
	Recieves: -
	Returns: the socket object
	"""
	print("setting up server...")
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # open socket
	server_socket.bind((SERVER_IP, SERVER_PORT))  # listen to requests
	server_socket.listen()  # listening
	print("listening for clients...")
	return server_socket

def send_error(conn, error_msg):
	"""
	Send error message with given message
	Recieves: socket, message error string from called function
	Returns: None
	"""
	build_and_send_message(conn, 'ERROR', "")
	print(error_msg)

##### MESSAGE HANDLING

def handle_logout_message(conn):
	"""
	Closes the given socket (in laster chapters, also remove user from logged_users dictioary)
	Recieves: socket
	Returns: None
	"""
	global logged_users
	global clients_sockets
	try:
		print("connection closed with ", logged_users[conn.getpeername()], " ):")
	except:
		print("connection closed with user... :(")
	logged_users.pop(conn.getpeername())
	clients_sockets.remove(conn)
	conn.close()

def handle_login_message(conn, data):
	"""
	Gets socket and message data of login message. Checks  user and pass exists and match.
	If not - sends error and finished. If all ok, sends OK message and adds user and address to logged_users
	Recieves: socket, message code and data
	Returns: None (sends answer to client)
	"""
	global users  # This is needed to access the same users dictionary from all functions
	global logged_users	 # To be used later
	userarr = data.split('#')
	if userarr[0] in users and userarr[1] == users.get(userarr[0]).get('password'):
		build_and_send_message(conn, 'LOGIN_OK', '')
		print('successfuly login')
		logged_users[conn.getpeername()] = userarr[0] #conection : username
	else:
		send_error(conn, "connection error with client (wrong password)")


def handle_getscore_massage(conn, username):
	global users
	score = users[username].get('score')
	build_and_send_message(conn, 'YOUR_SCORE', str(score))

#def handle_highscore_massage(conn):
#	global users
#	highscore = 1
#
#	build_and_send_message(conn, 'YOUR_SCORE', str(highscore))

def handle_logged_massage(conn):
	global logged_users
	lst = []
	for key, val in logged_users.items():
		lst.append(val)
	build_and_send_message(conn, 'YOUR_SCORE', str(lst))

#questions funcs
def handle_question_massage(conn):
	global questions
	global logged_users
	flag = False
	username = logged_users[conn.getpeername()]
	qarr = users[username].get("questions_asked")
	qnum = 0
	for question in questions:
		#print(question, '<->', qarr)
		if question not in qarr:
			flag =True
			qnum = question
			break
	if flag == False:
		send_error(conn, str(username + " you answered all questions"))
	else:
		ans = questions[qnum].get("answers")
		strans = chatlib.join_data(ans)
		arr = [str(qnum), questions[qnum].get("question"), strans]
		msg = chatlib.join_data(arr)
		build_and_send_message(conn, 'YOUR_QUESTION', msg)

def handle_answer_massage(conn, username, data):
	global questions
	global users
	arr = data.split('#')
	idq = int(arr[0])
	ans = int(arr[1])
	#print(idq, ans)
	#print(questions[idq].get('correct'))
	if ans == questions[idq].get('correct'):
		qs = users[username].get('questions_asked')
		qs.append(idq)
		users[username] = {"password": users[username].get('password'),
						"score" : (users[username].get('score')+5),
						"questions_asked": qs}
		build_and_send_message(conn, 'CORRECT_ANSWER', '')
	else:
		build_and_send_message(conn, 'WRONG_ANSWER', str(questions[idq].get('correct')))



def handle_client_message(conn, cmd, data):
	"""
	Gets message code and data and calls the right function to handle command
	Recieves: socket, message code and data
	Returns: None
	"""
	global logged_users  # To be used later

	if cmd == 'LOGIN':
		handle_login_message(conn, data)
	elif cmd == 'LOGOUT':
		handle_logout_message(conn)
	elif cmd == "LOGGED":
		handle_logged_massage(conn)
	elif cmd == "MY_SCORE":
		handle_getscore_massage(conn, logged_users[conn.getpeername()])
	elif cmd == "GET_QUESTION":
		handle_question_massage(conn)
	elif cmd == "SEND_ANSWER":
		handle_answer_massage(conn, logged_users[conn.getpeername()], data)
	else:
		build_and_send_message(conn, 'NO_ANSWERS', '')


def main():
	# Initializes global users and questions dicionaries using load functions, will be used later
	global users
	global questions

	print("loading...")
	questions = load_questions()
	users = load_user_database()
	server_socket = setup_socket()
	print("Welcome to Trivia Server!")
	global clients_sockets
	while True:

		(ready_to_read, ready_to_write, in_error) = select.select([server_socket] + clients_sockets, [], [])
		for current_socket in ready_to_read:
			if current_socket is server_socket:
				(client_socket, client_adress) = current_socket.accept()
				print("new client joined ", client_adress, "(;")
				clients_sockets.append(client_socket)
			else:
				try:
					data = current_socket.recv(1024).decode()
				except:
					handle_logout_message(current_socket)
					break
				cmd, data1 = chatlib.parse_message(data)
				handle_client_message(current_socket, cmd, data1)


if __name__ == '__main__':
	main()

