# Tutorial https://www.pythontutorial.net/pyqt/pyqt-qlabel/

# Voraussetzung: # pip install pyqt6

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap                                         # Pixmap Objekt in QtGui (kein Widget)

class AppWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt Label Widget')
        self.setGeometry(100, 100, 320, 210)                            

        
        label = QLabel()                                                # Erzeugen des QLabel-Objekts, ohne Text
        pixmap = QPixmap('logo-zm.png')                                 # Laden des Bildes
        label.setPixmap(pixmap)


        layout = QVBoxLayout()                                          # (Layout siehe Section3)
        layout.addWidget(label)                                         
        self.setLayout(layout)

        self.show()                                                     # Fenster zeigen

if __name__ == '__main__':
    app = QApplication(sys.argv)   
    window = AppWindow()
    sys.exit(app.exec())