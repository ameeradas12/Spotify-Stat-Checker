from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

auth = SpotifyOAuth(scope="user-top-read user-read-recently-played")
sp = spotipy.Spotify(auth_manager=auth)

user = sp.current_user()
print(user)
print(f"Logged in as: {user['display_name']}")
print(f"Followers:  {user['followers']['total']}")