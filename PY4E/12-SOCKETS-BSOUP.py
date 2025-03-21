import time
import urllib.request, urllib.parse, urllib.error
##############
# import socket
# import re
# import ssl
##############
from bs4 import BeautifulSoup
############################################################################
## URLLIB + BS4
############################################################################
url = input('Enter - ')
start = time.time()
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
print(soup)
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
end = time.time()
print(f'Exec Time = {end-start:.4f} secs')

#############################################################################
# SOCKET + BS4
#############################################################################
# url = input('Enter - ')
# start = time.time()
# host = re.findall(r'[^/]+', url)
# if len(host) > 1 :
#     dom = host[0]
#     #print(dom)
#     doc = '/'.join(host[1:])
#     #print(doc)
# else :
#     dom = host[0]
#     #print(dom)
#     doc = ''
#     #print(doc)
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # Wrap the socket with SSL
# context = ssl.create_default_context()
# s_sock = context.wrap_socket(sock, server_hostname=dom)
# try:
#     s_sock.connect((dom, 443))
#     print(f'Connection to {dom} succesfull!')
# except socket.error as e :
#     print(f'Connection to {dom} failed: {e}')
# rqst = f'GET /{doc} HTTP/1.0\r\nHost: {dom}\r\n\r\n'.encode()
# s_sock.send(rqst)
# while True:
#     data = s_sock.recv(512)
#     if len(data) < 1:break
#     #print(data.decode())
#     dc_data = data.decode()
# soup = BeautifulSoup(dc_data, 'html.parser')
# print(soup)
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))
# end = time.time()
# print(f'Socket Time: {end - start:.4f} seconds')
# s_sock.close()

######################## CHECK  **********************
import socket
import ssl

def fetch_http(url, port=80):
    hostname = url.split('/')[0]  # Extract the hostname
    path = '/' + '/'.join(url.split('/')[1:]) if '/' in url else '/'

    # Create a plain socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hostname, port))

    # Send an HTTP GET request
    request = f"GET {path} HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n"
    sock.sendall(request.encode())

    # Read the response
    response = b""
    while True:
        data = sock.recv(4096)
        if not data:
            break
        response += data

    sock.close()
    return response.decode()

# Parse and handle redirection
url = "www.example.com"
response = fetch_http(url)

if "HTTP/1.1 301" in response or "HTTP/1.1 302" in response:
    print("Redirect detected!")
    # Extract the 'Location' header
    for line in response.split("\r\n"):
        if line.lower().startswith("location:"):
            redirect_url = line.split(": ", 1)[1].strip()
            print(f"Redirecting to: {redirect_url}")

            # Handle HTTPS (port 443)
            if redirect_url.startswith("https://"):
                redirect_url = redirect_url.replace("https://", "")
                print(f"Fetching {redirect_url} over HTTPS")
                hostname = redirect_url.split('/')[0]
                path = '/' + '/'.join(redirect_url.split('/')[1:]) if '/' in redirect_url else '/'

                # Secure connection
                context = ssl.create_default_context()
                secure_sock = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=hostname)
                secure_sock.connect((hostname, 443))
                request = f"GET {path} HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n"
                secure_sock.sendall(request.encode())

                https_response = b""
                while True:
                    data = secure_sock.recv(4096)
                    if not data:
                        break
                    https_response += data

                secure_sock.close()
                print(https_response.decode())
else:
    print("No redirect detected, printing response:")
    print(response)
