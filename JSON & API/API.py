import json
import requests
from requests import session
from requests_oauthlib import OAuth2Session
import os
#pip install python_dotenv
from dotenv import load_dotenv


# headers = {"Content-Type": "application/json"}
# header = {"Authorization": "Bearer YOUR_API_KEY"}

# - Headers: This is a dictionary that holds HTTP headers sent with an API request.

# - Content-Type: This is an HTTP header that tells the server what type of data is being sent in the request body. It ensures that
#the server correctly interprets the request data.

# - Application/JSON: This indicates that the request body contains data formatted as JSON.

# - Authorisation: This is the HTTP header used to send authorisation credentials to the server.

# - Bearer: This is a token-based authentication scheme, it means that the request is authorized because it bears a token.

# - API KEY: This is the actual API KEY(token) used to authenticate request, the API Server checks if the token is valid before
#processing the request.

# - OAuth2 Authentication: It is a secure way for applications to authenticate and access protected resources without needing username
#and password for every request, instead of sending login details all the time. OAuth2 provides a token that the client can use to
#access resources.
#                               Reasons for using OAuth2
# * It is more secure. There is no need to send password or username repeatedly.
# * It is token-based: Access token expires after some time, reducing security risks.
# * It is widely used: APIs from Google, facebook, GitHub, etc. uses OAuth2.

#Working with RESTful APIs in Python
#GET Request (Fetch Data)
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
data = response.json() #converts a JSON response to a Python dictionary
print(data)

#POST Request (Send Data)
url = "https://jsonplaceholder.typicode.com/posts"
payload = {"title": "New Post", "body": "This is a new post", "userId": 1}
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=payload, headers=headers)
print(response.json()) #should return a new ID

#PUT Request (Update Data)
url = "https//jsonplaceholder.typicode.com/posts/1"
payload = {"title": "Updated Post", "body": "Updated content", "userId": 1}
response = requests.put(url, json=payload)
print(response.json()) #Should update post-ID 1

#DELETE Request (Remove Data)
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)
print(response.status_code) #Should return 200


#Handling API Authentication
#Some APIs require API keys for authentication
headers = {"Authorization": "Bearer 523ae9502n32nbv9235jgngf"}
response = requests.get(url, headers=headers)

#OAuth 2.0 Authentication
# client_id = "your_client_id" #Given by the API provider
client_secret= "your_client_secret" #Also given by the provider
# token_url = "https://example.com/oauth/token" #URL to get the access token

load_dotenv()

client_id = os.getenv("CLIENT_SECRET")
print(client_secret)
client_key = os.getenv("CLIENT_KEY")
print(client_key)

#Create an OAuth 2 Session
session2 = OAuth2Session(client_id)
#Get an access token
# = session.fetch_token(token_url, client_secret=client_secret)
#print(token)
#This contains the access token needed for authentication

#Error Handling in  API Calls
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    response.raise_for_status() # Raises an error for 4xx/5xx responses
    data = response.json()
    print(data)
except requests.exceptions.HTTPError as errh:
    # 🔴 Handles HTTP errors like:
    # 404 Not Found (Wrong URL)
    # 401 Unauthorized (Invalid API key)
    # 500 Internal Server Error (Server issue)
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    # 🔴 Handles network errors, such as
    # No Internet Connection
    # API server is down
    # Incorrect domain name
    print("Connection Error:", errc)
except requests.exceptions.Timeout as errt:
    # 🔴 Handles slow responses:
    # If the API takes too long to respond
    # If the request times out
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    # 🔴 Catches all other errors related to requests, including
    # Invalid URL format
    # SSL errors
    # Any unknown request failures
    print("Something went wrong:", err)
    