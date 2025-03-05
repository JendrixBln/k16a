# Tutorial https://www.pythontutorial.net/pyqt/pyqt-qhboxlayout/

# Voraussetzung: # pip install pyqt6

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

class AppWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QHBoxLayout')

        layout = QHBoxLayout()                                  # Vertikales Layout-Objekt erzeugen 
        self.setLayout(layout)                                  # Layout dem Fenster hinzufügen

        # SHOWME1: layout.addStretch()

        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")
        btn3 = QPushButton("Button 3")
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)            

        # SHOWME2: layout.addStretch()                          # am Anfang, am Ende, mittendrin
        # SHOWME3: layout.setSpacing(100)                       # Abstand zwischen allen widgets
        # SHOWME4: layout.setStretchFactor(btn1, 1) -> Wirkt NICHT bei Buttons (mit label schon)
        # SHOWME5: layout.setContentsMargins(0,0,0,0)
        
        


        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)   
    window = AppWindow()
    sys.exit(app.exec())