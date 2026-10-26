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

topTracks = sp.current_user_top_tracks(limit=10, time_range="long_term")
listofTracks = topTracks['items']
for i, track in enumerate(listofTracks, start=1):
    print(f"{i}. Name: {track['name']}  | {track['artists'][0]['name']}")

topArtists = sp.current_user_top_artists(limit=10,time_range="long_term")
listofArtists = topArtists['items']
for i, artist in enumerate(listofArtists, start=1):
    print(f"{i}. Artist: {artist['name']}")
