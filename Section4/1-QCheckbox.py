# Tutorial https://www.pythontutorial.net/pyqt/pyqt-qgridlayout/

# Voraussetzung: # pip install pyqt6

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QCheckBox
from PyQt6.QtCore import Qt                                     # enums für Funktionen, einfacher als Werte einzutragen

class AppWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QGridLayout')

        layout = QGridLayout()                                                  # Grid-Layout erzeugen
        self.setLayout(layout)                                                  # Layout dem Fenster hinzufügen

        # Checkbox - wir brauchen jetzt eine Instanzvariable, um das Checkedbox-Changed Ereignis abzufangen
        self.checkboxActive =  QCheckBox('Benutzer aktiv?')
        self.checkboxActive.checkStateChanged.connect(self.checkBoxUser_Changed)
        self.pushbuttonSet = QPushButton("setze")
        self.pushbuttonSet.clicked.connect(self.pushbuttonSetzeaktiv_clicked)

        layout.addWidget(self.checkboxActive, 0, 0)
        layout.addWidget(self.pushbuttonSet, 0, 1)

        self.tristate = QCheckBox('Drei zustände möglich', self)
        self.tristate.setTristate(True)
        layout.addWidget(self.tristate,0,2)
        self.pushbuttonSet = QPushButton("Get Tristate")
        self.pushbuttonSet.clicked.connect(self.gettristate)
        layout.addWidget(self.pushbuttonSet,0,3)

        self.show()
    def gettristate(self):
        match self.tristate.checkState():
            case Qt.CheckState.Checked:
                print("Ausgewählt")
            case Qt.CheckState.Unchecked:
                print("Nicht ausgewählt")
            case Qt.CheckState.PartiallyChecked:
                print("Zum Teil ausgewählt")
            case _:
                print("Das hätte nicht passieren dürfen!")

    def checkBoxUser_Changed(self, value):                                      # value liefert den Status der Checkboy
        print(f"Status der Checkbox verändert zu {value}")

    def pushbuttonSetzeaktiv_clicked(self):
        if self.checkboxActive.checkState() == Qt.CheckState.Unchecked:         # Konstante aus der QT-Bibliothek
            print("Inaktiv, setze auf aktiv")    
            self.checkboxActive.setChecked(True)
        else:
            print("Aktiv, setze auf inaktiv") 
            self.checkboxActive.setChecked(False)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)   
    window = AppWindow()
    sys.exit(app.exec())