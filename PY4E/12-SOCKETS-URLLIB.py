import time
import urllib.request, urllib.parse, urllib.error

start = time.time()

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand :
    print(line.decode().strip())

end = time.time()
print(f'Socket Time: {end-start:.4f} seconds')
