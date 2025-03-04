# Tutorial https://www.pythontutorial.net/pyqt/pyqt-qgridlayout/

# Voraussetzung: # pip install pyqt6

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit
from PyQt6.QtCore import Qt                                     # enums für Funktionen, einfacher als Werte einzutragen

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QGridLayout')

        layout = QGridLayout()                                                  # Grid-Layout erzeugen
        self.setLayout(layout)                                                  # Layout dem Fenster hinzufügen

        # username
        layout.addWidget(QLabel('Benutzername:'),0, 0)                          # Spalte 0, Zeile 0
        layout.addWidget(QLineEdit(), 0, 1)                                     # Spalte 1, Zeile 0

        # password
        layout.addWidget(QLabel('Password:'), 1, 0)                             # Spalte 0, Zeile 1
        layout.addWidget(QLineEdit(echoMode=QLineEdit.EchoMode.Password),1, 1)  # Spalte 1, Zeile 1

        # buttons
        layout.addWidget(QPushButton('Anmelden'), 2, 0,                         # Spalte 0, Zeile 2
                         alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QPushButton('Schließen'), 2, 1,                        # Spalte 1, Zeile 2
                         alignment=Qt.AlignmentFlag.AlignRight)

        layout.addWidget(QLineEdit(),3, 0, 2,2, alignment=Qt.AlignmentFlag.AlignRight)



        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)   
    window = MainWindow()
    sys.exit(app.exec())