# Tutorial https://www.pythontutorial.net/pyqt/pyqt-hello-world/

# Voraussetzung: # pip install pyqt6

from PyQt6.QtWidgets import QApplication, QWidget           

# Anwendungsobjekt erzeugen (Jede App braucht genau ein Anwendungsobjekt)
app = QApplication([])

# Hauptfenster der Anwendung erzeugen (QWidget ist die Basisklasse aller GUI-Objekte - Fenster)
window = QWidget(windowTitle='Hello World')
window.show()

# Endlosschleife starten (event loop)
# Wenn ein Objekt ein Ereignis auslöst, wird dieses in die Event-Warteschlange geschrieben. Für jedes Event in der Warteschlange wird der Event-Handler aufgerufen
app.exec()