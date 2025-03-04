# Tutorial https://www.pythontutorial.net/pyqt/pyqt-signals-slots/

# Voraussetzung: # pip install pyqt6

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout
)

# "event driven programming" anstelle der Programmierung im "EVA-Prinzip"
# GUI enthält Widgets (Steuerelemente) wie zum Beispiel Label, Eingabefelder, Buttons

# signal: Wenn ein Ereignis ausgelöst wird, erzeugt ein Widget ein Signal. QObjekt ist die Basisklasse, die Signale senden und empfangen kann. QWidget erbt u.a. von QObject
# slot: eine Funktion oder Methode, die Signale empfangen und auf sie antworten kann

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt Signals & Slots')

        button = QPushButton('Click me')                                        # Button anlegen 
        button.clicked.connect(self.button_clicked)                             # und das Event "Clicked" des Buttons mit einem Slot (einer Funktion der Klasse) verbinden

        # Objekte am besten in einem Layout platzieren (siehe XXX)
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(button)

        self.show()

    def button_clicked(self):
        print('ich wurde gedrückt!')


if __name__ == '__main__':
    app = QApplication(sys.argv)   
    window = MainWindow()
    sys.exit(app.exec())