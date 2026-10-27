# Spotify Stats Viewer

A desktop app that shows your Spotify listening stats: your top tracks and artists over different time ranges, and a live "now playing" card with album art.

Built with Python, PyQt6 and the Spotify Web API.

![alt text](image.png)

## Features

- **Log in with Spotify:** secure OAuth login (PKCE), so the app never sees your password and needs no client secret
- **Top tracks and artists:** your top 10 over the last 4 weeks, 6 months or year
- **Now playing:** shows the song you're listening to with its album cover, updated every 5 seconds
- **First-launch setup:** asks for your Spotify Client ID once and remembers it
- **Custom dark theme:** styled with Qt Style Sheets in `style.qss`
- **Designed in Qt Designer:** the layout lives in `stats.ui`, separate from the logic. Change it how you like. I used `pyside6-designer`.

## Download

Grab the latest `.exe` from the [Releases](https://github.com/ameeradas12/Spotify-Stat-Checker/releases) page. 

### First launch
The app asks for a Spotify **Client ID**. Spotify only lets approved accounts use each developer app, so you need your own (free, about 5 minutes):

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and log in.
2. Click **Create app**.
3. Set the **Redirect URI** to `http://127.0.0.1:8888/callback`.
4. Select **Web API**, then save.
5. Open the app's **Settings**, copy the **Client ID**, and paste it into Stats Viewer. You don't need the Client Secret.

A browser window then opens so you can log in to Spotify and approve access.

**Entered the wrong ID?** Delete `%APPDATA%\SpotifyStatsViewer\settings.json` and restart the app.

## Tech Stack

- **Python 3.12+**
- **PyQt6:** desktop UI
- **Spotipy:** Spotify Web API client (handles OAuth and token refresh)
- **Requests:** downloads album art
- **PyInstaller:** builds the `.exe`

## Run from Source

You'll still need a Client ID; see [First launch](#first-launch) above.

```bash
git clone https://github.com/ameeradas12/Spotify-Stat-Checker.git
cd Spotify-Stat-Checker
python -m venv .venv
.venv\Scripts\activate
pip install spotipy PyQt6 requests
python app.py
```
The app asks for your Client ID on first launch, the same as the exe.

## Building the .exe

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "SpotifyStatsViewer" --add-data "stats.ui;." --add-data "style.qss;." --exclude-module PySide6 app.py
```
The exe is created in the `dist` folder.

## Planned Features

- [ ] "Change Client ID" button in the app
- [ ] Album art icons in the top tracks list
- [ ] Paused indicator on the now playing card
- [ ] Recently played tab
- [ ] Lifetime stats from Spotify's extended streaming history export
- [ ] Progress bar on the currently playing song