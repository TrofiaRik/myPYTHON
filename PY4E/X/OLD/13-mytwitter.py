import urllib.request, urllib.parse, urllib.error
import twurl_v2
import json
############################################################################
# Insert the below code in case of ssl problems and need to disable ssl
############################################################################
#import ssl

#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE  # Disables SSL verification (not recommended)

#connection = urllib.request.urlopen(url, context=ctx)
############################################################################

# Base URLs for Twitter API v2
USER_BY_USERNAME_URL = "https://api.twitter.com/2/users/by/username/"
FOLLOWERS_URL = "https://api.twitter.com/2/users/"

def get_user_id(username):
    # Prepare parameters for the user lookup (optional)
    params = {}  # Could include "user.fields": "id,name" if needed
    req_url_name = twurl_v2.augment(USER_BY_USERNAME_URL + username, params)
    print('Retrieving URL:', req_url_name.full_url)
    try:
        with urllib.request.urlopen(req_url_name) as response:
            data = response.read().decode()
            json_data = json.loads(data)
    user_id = json_data["data"]["id"]
            print(f"User ID for {username}: {user_id}")
            return user_id
    except urllib.error.URLError as e:
        print(f"Error fetching user ID: {e}")
        return None

def get_tweets(user_id, qty):
    # Prepare parameters for the followers lookup
    params = {"max_results": f'{qty}'} # Limit to qty followers
    req_url_id = twurl_v2.augment(FOLLOWERS_URL + user_id + "/tweets", params)
    print(f"Retrieving URL: {req_url_id.full_url}")  # Print the exact URL
    try:
        with urllib.request.urlopen(req_url_id) as response:
            data = response.read().decode()
            json_data = json.loads(data)
            tweets = json_data["data"]
            print(f"\nFirst {qty} tweets for USER ID {user_id}:")
            for tweet in tweets:
                print(f"- {tweet['text']} (ID: {tweet['id']})")
    except urllib.error.URLError as e:
        print(f"Error fetching followers: {e}")

while True:
    print('')
    acct = input('Enter Twitter Account: ')
    if (len(acct) < 1): break
    qty = input('Enter how many tweets: ')
    if (len(qty) < 1): qty = 1

    # Step 1: Fetch user ID
    user_id = get_user_id(acct)

    # Step 2: Fetch first 'qty' followers if user ID was retrieved
    if user_id:
        get_tweets(user_id, qty)

#     ### 1 ### RETREIVING USID FROM USERNAME
#     usr_url = f'https://api.twitter.com/2/users/by/username/{acct}'
#     usr_url_augm = twurl-v2.augment(usr_url,
#                                     {'user': acct})   
#     print('Retrieving', usr_url_augm) 
#     connection = urllib.request.urlopen(usr_url_augm)
#     data = connection.read().decode()
#
#     js = json.loads(data)
#     user_id = js.get('data', {}).get('id')
#     if not user_id:
#         print("User not found.")
#     else:
#         print(f"User ID: {user_id}")
#
#     ### 2 ### RETREIVING FOLLOWERS INFO USING THE USID
#     following_url = f'https://api.twitter.com/2/users/{usr_id}/following'
#
#     url = twurl-v2.augment(following_url,{'max_results': '2'})
#
#     print('Retrieving', url)
#     connection = urllib.request.urlopen(url)
#     data = connection.read().decode()
#
#     js = json.loads(data)
#     print(json.dumps(js, indent=2))
#
#     headers = dict(connection.getheaders())
#     print('Remaining', headers['x-rate-limit-remaining'])
# 
#     for user in js['data']:
#         print(u['username'])
#         if 'status' not in user:
#             print('   * No status found')
#             continue
#         s = user['status']['text']
#         print('  ', s[:50])
