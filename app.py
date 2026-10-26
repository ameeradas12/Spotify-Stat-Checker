import sys
import requests

from PyQt6.QtWidgets import (
    QApplication, QWidget,
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap
from PyQt6 import uic


from main import get_top_artists, get_top_tracks, getNowPlaying

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
        uic.loadUi("stats.ui", self)
        self.albumCover.setFixedSize(120,120)
        self.load_data()
        self.range_box.currentIndexChanged.connect(self.load_data)
        self.update_now_playing()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_now_playing)
        self.timer.start(5000)


app = QApplication(sys.argv)
window = StatsWindow()
window.show()
sys.exit(app.exec())

