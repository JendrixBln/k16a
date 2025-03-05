# Tutorial https://www.pythontutorial.net/pyqt/pyqt-qlabel/

# Voraussetzung: # pip install pyqt6

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class AppWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt Label Widget')
        self.setGeometry(100, 100, 320, 210)                            

        label = QLabel('This is a QLabel widget')                       # Erzeugen des QLabel-Objekts. De Konstruktor enthält die Beschriftung (unterschiedlich von Objekt zu Objekt)

        layout = QVBoxLayout()                                          # (Layout siehe XXX)
        layout.addWidget(label)                                         
        self.setLayout(layout)

        self.show()                                                     # Fenster zeigen

if __name__ == '__main__':
    app = QApplication(sys.argv)   
    window = AppWindow()
    sys.exit(app.exec())