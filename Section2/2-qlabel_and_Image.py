import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap                                         # Bitmap Objekt in QtGui (kein Widget)

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt Label Widget')
        self.setGeometry(100, 100, 320, 210)                            # Größe des Objekts setzen. Self ist das Fenster, wir müssen die Größe ändern, damit das Label platz hat

        label = QLabel('This is a QLabel widget')                       # Erzeugen des QLabel-Objekts. De Konstruktor enthält die Beschriftung (unterschiedlich von Objekt zu Objekt)

        layout = QVBoxLayout()                                          # (Layout siehe XXX)
        layout.addWidget(label)                                         
        self.setLayout(layout)

        self.show()                                                     # Fenster zeigen

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window and display it
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())