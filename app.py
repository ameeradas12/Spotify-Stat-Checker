import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget
)
from PyQt6 import uic

from main import get_top_artists, get_top_tracks

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


    def __init__(self):
        super().__init__()
        uic.loadUi("stats.ui", self)
        self.load_data()
        self.range_box.currentIndexChanged.connect(self.load_data)


app = QApplication(sys.argv)
window = StatsWindow()
window.show()
sys.exit(app.exec())

