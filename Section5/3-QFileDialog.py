# Quelle: https://www.pythontutorial.net/pyqt/pyqt-qradiobutton/

# Aufgabe 1: Erschließt Euch selbst die grundlegende Funktionsweise von FileDialogs
# Aufgabe 2: Das Beispiel hier lässt Euch mehrere Dateien auswählen. Erweitert das Programm so, dass Ihr EINE vorhandene Word-Datei auswählen könnt
# Aufgabe 3: Ergänzt das Programm, sodass man eine Datei zum Speichern auswählen (oder neu anlegen) kann

# Erstellt also 2 neue Programme

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path

class AppWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt File Dialog')
        self.setGeometry(100, 100, 300, 150)

        layout = QGridLayout()
        self.setLayout(layout)

        # file selection
        file_browser_btn = QPushButton('Browse')
        file_browser_btn.clicked.connect(self.open_file_dialog)
        layout.addWidget(file_browser_btn, 2 ,0)

        self.show()

    def open_file_dialog(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Images (*.png *.jpg *.gif)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            for filename in filenames:
                print(f"Datei {filename} wurde ausgewählt")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec())