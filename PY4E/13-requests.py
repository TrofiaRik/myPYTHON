#Basic example of 'request' library usage
import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)
