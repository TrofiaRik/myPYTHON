import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mydest = 'data.pr4e.org'
myport = 80
try :
    mysock.connect( (mydest, myport) )
    print(f'Connection to {mydest}:{myport} has been successfull!')
except socket.error as e :
    print(f'Connection failed: {e}')

close = input('If and when you want to close the connection, just input \'x\': ')

def xsock() :
    mysock.close()
    print("Connection closed")

if close == 'x' :
    xsock()
