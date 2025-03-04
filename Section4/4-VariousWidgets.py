
# Quelle: https://www.pythontutorial.net/pyqt
# Aufgabe: Verschafft Euch einen kurzen Überblick über die Steuerelemente und schaut ins Tutorial. Stellt sicher, dass Ihr bei Bedarf
#          schnell auf benötigte Informationen zugreifen könnt

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QFormLayout, QComboBox, QSpinBox
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Verschiedene Steuerelemente')
        
        # create a grid layout
        layout = QFormLayout()
        self.setLayout(layout)

        spin = QSpinBox(minimum=1, maximum=200, value=100, prefix='€')
        layout.addRow("Preis:", spin)

        
        

        # show the window
        self.show()

    def update(self):
        self.result_label.setText(
            f'You selected {self.cb_platform.currentText()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())