import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QComboBox, QTabWidget, QListWidget,
)
from PyQt6 import uic

from main import get_top_artists, get_top_tracks

class StatsWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("stats.ui", self)



app = QApplication(sys.argv)
window = StatsWindow()
window.show()
sys.exit(app.exec())

