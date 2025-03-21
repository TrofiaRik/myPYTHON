import urllib.request, urllib.parse, urllib.error
import hidden_v2

def augment(url, parameters):
    ##1## import security
    secrets = hidden_v2.oauth() 
    bearer_token = secrets["bearer_token"]
    
    ##2## check if parameters are provided, if yes, append them
    if parameters:
        url += "?" + urllib.parse.urlencode(parameters)

    ##3## assemble the request with the authorization header included
    headers = {"Authorization": f"Bearer {bearer_token}"}
    req = urllib.request.Request(url, headers=headers)
    
    ##4## return the complete request
    return req

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
