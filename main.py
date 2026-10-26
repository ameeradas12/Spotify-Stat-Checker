from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

auth = SpotifyOAuth(scope="user-top-read user-read-recently-played")
sp = spotipy.Spotify(auth_manager=auth)

user = sp.current_user()




topArtists = sp.current_user_top_artists(limit=10,time_range="long_term")
listofArtists = topArtists['items']


def get_top_tracks(time_range):
    top_tracks = sp.current_user_top_tracks(limit=10, time_range=time_range)
    results = []
    for i, track in enumerate(top_tracks['items'], start=1):  
        results.append(f"{i}. {track['name']} | {track['artists'][0]['name']}")  
    return results

def get_top_artists(time_range):
    top_artists = sp.current_user_top_artists(limit=10, time_range=time_range)  
    results = []
    for i, artist in enumerate(top_artists['items'], start=1):
        results.append(f"{i}. Artist: {artist['name']}")
    return results   

if __name__== "__main__":
    print("\n".join(get_top_tracks("long_term")))
    print("\n".join(get_top_artists("long_term")))
    print(f"Logged in as: {user['display_name']}")
    print(f"Followers:  {user['followers']['total']}")

