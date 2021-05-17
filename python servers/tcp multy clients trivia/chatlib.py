# Protocol Constants

CMD_FIELD_LENGTH = 16	# Exact length of cmd field (in bytes)
LENGTH_FIELD_LENGTH = 4   # Exact length of length field (in bytes)
MAX_DATA_LENGTH = 10**LENGTH_FIELD_LENGTH-1  # Max size of data field according to protocol
MSG_HEADER_LENGTH = CMD_FIELD_LENGTH + 1 + LENGTH_FIELD_LENGTH + 1  # Exact size of header (CMD+LENGTH fields)
MAX_MSG_LENGTH = MSG_HEADER_LENGTH + MAX_DATA_LENGTH  # Max size of total message
DELIMITER = "|"  # Delimiter character in protocol
DATA_DELIMITER = "#"  # Delimiter in the data part of the message

# Protocol Messages 
# In this dictionary we will have all the client and server command names

PROTOCOL_CLIENT = {
"login_msg" : "LOGIN",
"logout_msg" : "LOGOUT"
} # .. Add more commands if needed

PROTOCOL_SERVER = {
"login_ok_msg" : "LOGIN_OK",
"login_failed_msg" : "ERROR"
} # ..  Add more commands if needed

# Other constants

ERROR_RETURN = None  # What is returned in case of an error

def build_message(cmd, data):
	"""Gets command name (str) and data field (str) and creates a valid protocol message
	Returns: str, or None if error occured
	"""
	if len(cmd) > 16:
		return None
	finalCommand = cmd+' '*(16-len(cmd))
	lenStrShort = str(len(data))
	length = '0'*(4-len(lenStrShort))+lenStrShort
	full_msg = finalCommand + '|' + length + '|' + data
	return full_msg

def parse_message(data):
	"""Parses protocol message and returns command name and data field
	Returns: cmd (str), data (str). If some error occured, returns None, None
	"""
	if data.count('|') != 2:
		return None, None
	arr = data.split('|')
	cmd = arr[0]
	cmd = cmd.replace(' ', '')
	if int(arr[1]) != len(arr[2]):
		return None, None
	return cmd, arr[2]

def split_data(msg, expected_fields):
	"""Helper method. gets a string and number of expected fields in it. Splits the string
	using protocol's data field delimiter (|#) and validates that there are correct number of fields.
	Returns: list of fields if all ok. If some error occured, returns None
	"""
	count=0
	data_list = list(msg)
	for ch in data_list:
		if ch == '#':
			count+=1
	if count == expected_fields:
		return msg.split('#')
	return [None]

def join_data(msg_fields):
	"""
	Helper method. Gets a list, joins all of it's fields to one string divided by the data delimiter. 
	Returns: string that looks like cell1#cell2#cell3
	"""
	return '#'.join(msg_fields)