
# Quelle: https://www.pythontutorial.net/pyqt
# Aufgabe 1: Verschafft Euch einen kurzen Überblick über die Steuerelemente und schaut ins Tutorial. 
#            Stellt sicher, dass Ihr bei Bedarf schnell auf benötigte Informationen zugreifen könnt
# Aufgabe 2: Recherchiert je Widget mindestens ein Ereignis, welches abgefangen werden sollte. 
#            Schreibt eine Slot-Funktion und verbindet sie jeweils mit dem richtigen Signal

import sys
from PyQt6.QtWidgets import *                                               # man kann auch einfach alles importieren
from PyQt6.QtCore import Qt


class AppWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQT Verschiedene Steuerelemente')
        
        layout = QFormLayout()
        self.setLayout(layout)

        spin = QSpinBox(minimum=1, maximum=200, value=100, prefix='€')
        layout.addRow("Spin:", spin)

        self.date = QDateEdit(self)
        layout.addRow('DateEdit:', self.date)
        
        self.time = QTimeEdit(self)
        layout.addRow('TimeEdit:', self.time)

        self.datetime = QDateTimeEdit(self)
        layout.addRow('DateTime:', self.datetime)

        self.vertslider = QSlider(Qt.Orientation.Vertical, self)
        self.vertslider.setRange(0,100)
        layout.addRow('Vert. Slider 1-100:', self.vertslider)
        
        self.horizslider = QSlider(Qt.Orientation.Horizontal, self)
        self.horizslider.setRange(0,100)
        layout.addRow('Horiz. Slider 50-60:', self.horizslider)        

        self.progressbar = QProgressBar(self)
        self.progressbar.setRange(1,100)
        self.progressbar.setValue(50)
        layout.addRow('Fortschritt:', self.progressbar)        

        text_edit = QTextEdit(self)
        layout.addRow("Multiline Text:", text_edit)

        # show the window
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec())