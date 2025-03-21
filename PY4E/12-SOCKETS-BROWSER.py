import time
import socket

###############################################
## CREATE A BROWSER GOING TROUGH THE KEY STEPS
# 1 socket.socket() -> CREATE
# 2 socket.connect() -> CONNECT
# 3 socket.send() -> SEND
# 4 socket.recv() -> RECEIVE
# 5 socket.close() -> CLOSE
################################################

start = time.time()

## ** 1 ** CREATE SOCKET .socket()
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ** 2 ** CONNECT SOCKET .connect()
mysock.connect(('data.pr4e.org', 80))

# ** 3 °° SEND COMMAND .send()
#cmd = 'GET /romeo.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()
cmd2 = 'GET / HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()
mysock.send(cmd2)

# ** 4 ** RECEIVE COMMAND .recv()
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

end = time.time()
print(f'Socket Time: {end - start:.4f} seconds')

# ** 5 ** CLOSE COMMAND .close()
mysock.close()
