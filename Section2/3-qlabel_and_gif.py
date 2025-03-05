# Tutorial https://www.pythontutorial.net/pyqt/pyqt-qlabel/

# Voraussetzung: # pip install pyqt6

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QMovie                                          # Movie-Objekt in QtGui (kein Widget)

class AppWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt Label Widget')
        self.setGeometry(100, 100, 320, 210)                            

        label = QLabel()                                                # Erzeugen des QLabel-Objekts, ohne Text
        video = QMovie('b2f.gif')                                       # laden des animierten Gifs (von https://knowyourmeme.com/photos/1033612-back-to-the-future-day)
        label.setMovie(video)                                           # Platzieren im label
        video.start()                                                   # Starten der Animation

        layout = QVBoxLayout()                                          # (Layout siehe Section3)
        layout.addWidget(label)                                         
        self.setLayout(layout)

        self.show()                                                    

if __name__ == '__main__':
    app = QApplication(sys.argv)   
    window = AppWindow()
    sys.exit(app.exec())