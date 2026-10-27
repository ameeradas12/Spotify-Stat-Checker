import spotipy
from spotipy.oauth2 import SpotifyPKCE

sp = None

def connect(client_id):
    global sp
    auth = SpotifyPKCE(client_id=client_id,
                    redirect_uri="http://127.0.0.1:8888/callback",
                    scope="user-top-read user-read-recently-played user-read-currently-playing")
    sp = spotipy.Spotify(auth_manager=auth)


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


def getNowPlaying():
    current = sp.current_user_playing_track()
    if current is None or current['item'] is None:
        return None
    trackName = current['item']['name']
    artistName = current['item']['artists'][0]['name']
    albumName = current['item']['album']['name']
    albumCover = current['item']['album']['images'][1]['url']
    return {
        "name": trackName,
        "artist": artistName,
        "albumName": albumName,
        "albumCover": albumCover,
    }



   