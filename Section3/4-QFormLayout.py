# Tutorial https://www.pythontutorial.net/pyqt/pyqt-qformlayout/

# Voraussetzung: # pip install pyqt6

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLabel, QLineEdit
from PyQt6.QtCore import Qt                                     # enums für Funktionen, einfacher als Werte einzutragen

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Registrieren Sie sich jetzt!')

        layout = QFormLayout()
        self.setLayout(layout)

        layout.addRow('Name:', QLineEdit(self))                                                             # addrow kombiniert label mit einem anderen 
        layout.addRow('Email:', QLineEdit(self))                                                            # Widget (ausprobieren, welche möglich sind)
        # SHOW ME: layout.addRow("Dummy:", QLabel("Dummy", self))
        layout.addRow('Passwort:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
        layout.addRow('Password wiederholen:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
        layout.addRow('Telefon:', QLineEdit(self))

        layout.addRow(QPushButton('Jetzt Registrieren'))

        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)   
    window = MainWindow()
    sys.exit(app.exec())