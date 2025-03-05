# Tutorial https://www.pythontutorial.net/pyqt/pyqt-qpushbutton/
# Achtung: Fehlende Verbindung signal und slot im Beispiel auf der Webseite

# Voraussetzung: # pip install pyqt6

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon                                           # Icon-Objekt in QtGui (kein Widget)

class AppWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt Label Widget')
        self.setGeometry(100, 100, 320, 210)                           

        btntext = QPushButton("Ich habe Text")
        btntext.clicked.connect(self.btntext_clicked)
        
        btnimage = QPushButton("Ich habe auch ein Logo")
        logo = QIcon("logo-zm.png")
        btnimage.setIcon(logo)
        btnimage.clicked.connect(self.btnimage_clicked)

        btntoggle = QPushButton("Ich bin ein Schalter")
        btntoggle.setCheckable(True)
        btntoggle.clicked.connect(self.btntoggle_clicked)
    
        layout = QVBoxLayout()                                          # (Layout siehe XXX)
        layout.addWidget(btntext)                                         
        layout.addWidget(btnimage)  
        layout.addWidget(btntoggle)
        self.setLayout(layout)

        self.show()                                                    

    def btntext_clicked(self):
        print("Der Button mit dem Text wurde gedrückt!")
    def btnimage_clicked(self):
        print("Der Button mit dem Image wurde gedrückt!")
    def btntoggle_clicked(self, checked):
        print("Der Status des Toogle-Buttons hat sich geändert zu:", checked)

if __name__ == '__main__':
    app = QApplication(sys.argv)   
    window = AppWindow()
    sys.exit(app.exec())
