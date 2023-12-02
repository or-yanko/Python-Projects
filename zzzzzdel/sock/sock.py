import socket 
import sys 

ip = socket.gethostbyname('www.google.com')#get ip of website

print(ip)

def s1():#create socket to googleusing socket 
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        print ("Socket successfully created")
    except socket.error as err: 
        print ("socket creation failed with error %s" %(err))

    # default port for socket 
    port = 80

    try: 
        host_ip = socket.gethostbyname('www.google.com') 
    except socket.gaierror: 

        # this means could not resolve the host 
        print ("there was an error resolving the host")
        sys.exit() 

    # connecting to the server 
    s.connect((host_ip, port)) 

    print ("the socket has successfully connected to google") 

s1()