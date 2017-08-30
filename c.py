import socket
 
HOST =socket.gethostname()        # The remote host
PORT = 42050              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
s.connect((HOST, PORT))
f = open('mytext.txt', 'rb')
print "Sending Data ...."  
l = f.read()
while True:      
    for line in l:
        s.send(line)    
    break
f.close()
print "Sending Complete"
s.close()
