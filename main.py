import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import base64

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode()).decode()

headers = {
    "Authorization": f"Basic {client_creds_b64}",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials"
}

response = requests.post(
    "https://accounts.spotify.com/api/token",
    headers=headers,
    data=data
)

print("Status code:", response.status_code)
print("Response body:", response.text)

token_info = response.json()
access_token = token_info.get("access_token")

headers = {
    "Authorization": f"Bearer {access_token}"
}

params = {
    "q" : "NeYo",
    "type": "artist",
    "limit": 1
}

url = "https://api.spotify.com/v1/search"
response = requests.get(url, headers=headers, params=params)

data = response.json()
print(data)