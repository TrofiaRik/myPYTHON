import urllib.request, urllib.parse, urllib.error
import hidden-v2

# Load Bearer token (api v2) from hidden.py 
secrets = hidden-v2.oauth() 
BEARER_TOKEN = secrets['bearer_token']
HEADERS = {"Authorization": f"Bearer {BEARER_TOKEN}"}   

def augment(url, parameters):
    """Append parameters to URL and return the full request URL."""
    if parameters:
        url += "?" + urllib.parse.urlencode(parameters)

    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"  # Required for API v2
    }

    return url, headers

# def fetch_posts_test(userid, count):
#         """ Fetch tweets using Twitter API v2 with Bearer Token authentication. """
#     print('* Calling Twitter...')
#     url = f"https://api.twitter.com/2/users/{userid}/tweets"
#     details = {'screen_name': 'drchuck', 'count': '2'})
#     print(url)
#     connection = urllib.request.urlopen(url)
#     data = connection.read()
#     print(data)
#     headers = dict(connection.getheaders())
#     print(headers)
