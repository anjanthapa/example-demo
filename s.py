import socket  # Import socket module
 
HOST =socket.gethostname()         # Get local machine name
PORT = 42050              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating a socket
s.bind((HOST, PORT))  # Bind to the port
print "Server running", HOST, PORT
s.listen(5)  #Now wait for client connection.
conn, addr = s.accept()   # Establish connection with client.
print'Connected by', addr
 
while True:
    data = "".join(iter(lambda:conn.recv(1),"\n"))       
    print data   
    if not data: break                
      
print "Done Receiving"
conn.close()
