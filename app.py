import sys
import requests

from PyQt6.QtWidgets import (
    QApplication, QWidget, QInputDialog,
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap
from PyQt6 import uic
import os

def resource_path(name):
    # When running as an exe, PyInstaller unpacks files into sys._MEIPASS
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)

from main import get_top_artists, get_top_tracks, getNowPlaying, connect
from settings import load_client_id, save_client_id

class StatsWindow(QWidget):
    def load_data(self):
        time_range = self.range_box.currentIndex()
        ranges = ["short_term", "medium_term", "long_term"]
        selectedRange = ranges[time_range]
        topTracksList = self.trackList
        topArtistList = self.artistList
        
        topTracksList.clear()
        topArtistList.clear()

        for track in get_top_tracks(selectedRange):
            topTracksList.addItem(track)
        for artist in get_top_artists(selectedRange):
            topArtistList.addItem(artist)

    def update_now_playing(self):
        currentTrack = getNowPlaying()

        if currentTrack is None:
            self.trackName.setText("Nothing playing")
            self.albumCover.clear()
        else:
            self.trackName.setText(f"{currentTrack['name']} - {currentTrack['artist']}")

            data = requests.get(currentTrack["albumCover"]).content
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            pixmap = pixmap.scaled(120,120,
                       Qt.AspectRatioMode.KeepAspectRatio,
                       Qt.TransformationMode.SmoothTransformation)
            self.albumCover.setPixmap(pixmap)
    
    def __init__(self):
        super().__init__()
        uic.loadUi(resource_path("stats.ui"), self)      
        self.albumCover.setFixedSize(120,120)
        self.load_data()
        self.range_box.currentIndexChanged.connect(self.load_data)
        self.update_now_playing()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_now_playing)
        self.timer.start(5000)


app = QApplication(sys.argv)
client_id = load_client_id()
if client_id is None:
    text, ok = QInputDialog.getText(
        None, 
        "Spotify Stats Viewer Setup",
        "Paste your Spotify Client Id from 'developer.spotify.com/dashboard'"
    )
    if not ok or not text.strip():
        sys.exit()
    client_id = text.strip()
    save_client_id(client_id)

connect(client_id)
window = StatsWindow()
with open(resource_path("style.qss")) as f:
    app.setStyleSheet(f.read())

window.show()
sys.exit(app.exec())

