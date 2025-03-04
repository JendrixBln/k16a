# Tutorial https://www.pythontutorial.net/pyqt/pyqt-signals-slots/

# Vorausstetzung: # pip install pyqt6

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout
)

# "event driven programming" anstelle der Programmierung im "EVA-Prinzip"
# GUI enthält Widgets (Steuerelemente) wie zum Beispiel Label, Eingabefelder, Buttons

# signal: Wenn ein Ereignis ausgelöst wird, erzeugt ein Widget ein Signal. QObjekt ist die Basisklasse, die Signale senden und empfangen kann. QWidget erbt u.a. von QObject
# slot: eine Funktion oder Methode, die Signale empfangen und auf sie antworten kann

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt Signals with data')
        self.setGeometry(100, 100, 320, 210)                        # Größe des Objekts setzen. Self ist das Fenster, wir müssen die Größe ändern, damit das Label platz hat
        
         # create widgets
        label = QLabel()
        line_edit = QLineEdit()
        line_edit.textChanged.connect(label.setText)                # das Signal textChanged sendet den Text im Eingabefeld an den verbundenen Slot. Der Slot setText wiederum erwartet 
                                                                    # genau einen Text. Dadurch können die Daten weitergegeben werden. 
        # place the widgets
        layout = QVBoxLayout()                                      # Layout siehe XXX
        layout.addWidget(label)
        layout.addWidget(line_edit)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window and display it
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())