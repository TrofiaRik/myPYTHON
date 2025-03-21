import requests
import hidden_v2
#import json

##1## import security
secrets = hidden_v2.oauth() 
bearer_token = secrets["bearer_token"]

##2## FUNCTIONS
def get_user_id(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_id = response.json()["data"]["id"]
        print(f"User ID for {username}: {user_id}")
        return user_id
    else:
        print(f"Error fetching User ID for {username}: {response.status_code}")
        return None

def get_posts(user_id, username, qty):
    url = f"https://api.twitter.com/2/users/{user_id}/tweets"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    params = {"max_results": qty}

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        posts = response.json()["data"]
        print(f"\nThe first {qty} tweets for {username}-{user_id} are the below:")
        for post in posts:
            print(f"\n**\nPost con ID:{post['id']}\nTesto:{post['text']}")
        # Print rate limit headers if available
        print(f"Rate Limit: {response.headers.get('x-rate-limit-limit', 'N/A')}")
        print(f"Remaining: {response.headers.get('x-rate-limit-remaining', 'N/A')}")
        print(f"Reset Time (Unix): {response.headers.get('x-rate-limit-reset', 'N/A')}")
    else:
        print(f"Error fetching posts: {response.status_code}")
        print(f"Response: {response.text}")
        # Print rate limit headers if available
        print(f"Rate Limit: {response.headers.get('x-rate-limit-limit', 'N/A')}")
        print(f"Remaining: {response.headers.get('x-rate-limit-remaining', 'N/A')}")
        print(f"Reset Time (Unix): {response.headers.get('x-rate-limit-reset', 'N/A')}")

##3## ASK FOR DATA            
while True:
    print('')
    acct = input('Enter X username (without@): ')
    if (len(acct) < 1): break
    qty = input('Enter how many posts: ')
    if (len(qty) < 1): qty = 1

    # Step 1: Fetch user ID
    user_id = get_user_id(acct)

    # Step 2: Fetch first 'qty' followers if user ID was retrieved
    if user_id:
        get_posts(user_id, acct, qty)

