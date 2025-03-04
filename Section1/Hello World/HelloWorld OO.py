# Tutorial https://www.pythontutorial.net/pyqt/pyqt-hello-world/

# Vorausstetzung: # pip install pyqt6

import sys                                                          # sys: Informationen in Konstanten, Funktionen und Methoden über den Python-Interpreter
from PyQt6.QtWidgets import QApplication, QWidget           

class MainWindow(QWidget):                                          # Erzeuge Klasse und ergbe von QWidget
    def __init__(self, *args, **kwargs):                            # Konstruktor der Klasse, beliebige unbenannte und benannte Argumente *args und **kwargs (Key-Value-Pairs)
        super().__init__(*args, **kwargs)                           # Aufruf Elternklasse, falls Vererbung genutzt wird
                                                                    
                                                                    # self ist der Zeiger auf die aktuelle Instanz (das aktuelle Fenster)
        self.setWindowTitle("Hello World")                          # geerbte Methode setWindowTitle (vgl. windowTitle im Konstruktor)
        self.show()                                                 # show() ist evenfalls vererbt


if __name__ == '__main__':                                          # führe aus, wenn als Programm gestartet wird (und nicht importiert)
    app = QApplication(sys.argv)                                    # Jede GUI benötigt genau ein APP-Objekt

    # create the main window
    window = MainWindow()                                           # Instanz des Hauptfensters erzeugen 
    #window2 = MainWindow()                                         # 2.Instanz möglich, jedes Fenster wird nur in seiner Klasse aufgerufen, die beiden Fenster wissen nichts voneinander

    # start the event loop
    sys.exit(app.exec())                                            # liefert einen Returncode zurück (0 wenn erfolgreich). Bei einer GUI-App nicht zwingend notwendig