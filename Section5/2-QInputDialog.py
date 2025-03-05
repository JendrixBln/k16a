# Quelle:     https://www.pythontutorial.net/pyqt/pyqt-qinputdialog/

# Aufgabe 1:  Analysiert den Quellcode, versteh, wie InputDialog genutzt werden kann
# Aufgabe 2:  Erweitert das Programm, sodass auch die Methoden getInt(), getDouble(), getMultiLineText() und getItem() getestet werden können.
#             Fügt also weitere Buttons hinzu und verfahrt nach dem selben Schema wie in GetText()  

import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox, QGridLayout, QPushButton, QInputDialog
from PyQt6.QtCore import Qt


class AppWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQT QInputDialog')
        
        layout = QGridLayout(self)
        self.setLayout(layout)
        btn = QPushButton("Start Demo")
        btn.clicked.connect(self.btn_clicked)
        layout.addWidget(btn)
        self.show()
        
    
    def btn_clicked(self):
        input, ok = QInputDialog.getText(self, "Dein Name", "Name eingeben:")
        if ok and input:                                                                # Benutzer hat etwas eingegeben und OK gedrückt
            QMessageBox.information(self, "Danke!", f"Dein Name ist {input}!")
        elif ok == True and input == "":
            QMessageBox.warning(self, "Schade", "Du hast nichts eingegeben!")
        elif not ok: 
            QMessageBox.critical(self, "Schade", "Du hast auf Abbrechen gedrückt!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec())