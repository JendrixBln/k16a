#Tutorial https://www.pythontutorial.net/pyqt/pyqt-qmainwindow/
# ACHTUNG: Leider ein paar Fehler drin

# QWidget bietet ein einfaches Fenster oder kann als unsichtbarer Container verwendet werden. 
# Ein vollumfängliches Anwendungsfenster besitzt aber Menüs, Toolbars und eine Statusbar, die man hinzufügen oder weglassen kann

import sys
from PyQt6.QtWidgets import QApplication, QStatusBar, QPushButton, QToolBar, QLineEdit, QMainWindow, QGroupBox, QFormLayout, QMessageBox
from PyQt6.QtGui import QIcon, QAction

class AppWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QMainWindow')
        self.setWindowIcon(QIcon('./editor.png'))
        self.setGeometry(100, 100, 300, 150)

        self.grpbox = QGroupBox("")                                                 # Hier kommen alle Widgets hinein. QMainWindow ha nur ein 
        self.setCentralWidget(self.grpbox)                                          # zentrales Widget. Um mehr als ein Steuerelement haben zu können, 
                                                                                    # brauchen wir einen Container, 
        layoutgrp = QFormLayout()                                                   # der auch wieder ein Layout bekommt
        self.grpbox.setLayout(layoutgrp)                  
        
        self.editwidget = QLineEdit()                                               # Demo mit Eingabefeld 
        self.submitbutton = QPushButton("Submit")                                   # und Schaltfläche
        layoutgrp.addRow("Username:", self.editwidget)                              # diese Widgets werden dem Container hinzugefügt
        layoutgrp.addRow(self.submitbutton)

        mymenu = self.menuBar()                                                     # Menübar hinzufügen. QMainWindow bietet hier eigene Funktionalität. 
                                                                                    # selfmenuBar() liefert die aktuelle Menübar (QMenuBar) oder legt 
                                                                                    # eine neue an, wenn noch keine da ist
                                                                                    
        mymenuFile = mymenu.addMenu("&Datei")                                       # In diese Menübar können wir nun Menüs hinzufügen. WIr erhalten 
        mymenuEdit = mymenu.addMenu("&Bearbeiten")                                  # QMenu-Widgets
        mymenuHelp = mymenu.addMenu("&?")

        mymenuFile.addAction("&Öffnen", lambda: self.showMenuChoice("Öffnen"))        # Einzelne Menüpunkte werden als QAction eingefügt
        mymenuFile.addAction("&Schließen", lambda: self.showMenuChoice("Schließen"))  # Ein QAction-Objekt benötigt eine CallBack-Funktion, die aufgerufen wird,
        mymenuFile.addAction("&Beenden", QApplication.quit )                          # wenn der Menüpunkt ausgewählt wurde. Ein lambda in Python erzeugt eine 
                                                                                      # anonyme Funktion, die erst beim Anklicken des Menüeintrags ausgeführt wird.
                                                                                      # Ansonsten würde die Funktion direkt ausgeführt. 
        #SHOWME: Untermenüs
        #mymenuFileRecent= mymenuFile.addMenu("Zuletzt geöffnete Dateien...")        
        #mymenuFileRecent.addAction("Projektbericht.docx", lambda: self.showMenuChoice("Projektbericht.docx"))
        #mymenuFileRecent.addAction("PSP.TDL", lambda: self.showMenuChoice("PSP.TDL"))

        myToolbar = QToolBar("Zeige Toolbar")                                         # Toolbar erzeugen 
        self.addToolBar(myToolbar)                                                  # und dem QMainWindow hinzufügen
        
        fileOpenAction = QAction(QIcon("./open.png"), "Öffnen", self)               # Wir brauchen hier wieder Instanzvariablen, 
        fileOpenAction.setShortcut("Ctrl+O")                                        # Um einen Shortcut anlegen zu können
        fileOpenAction.triggered.connect(lambda: self.showMenuChoice("Öffnen"))     # und um das Signal triggered an den Slot showMenuChoice binden zu können
        myToolbar.addAction(fileOpenAction)                                         # Jetzt endlich können wir die Toolbar Action zur Toolbar hinzufügen

        fileCloseAction = QAction(QIcon("./close.png"), "Schließen", self)          # Jetzt noch für FileClose-Action
        fileCloseAction.setShortcut("Ctrl+F4")                                      
        fileCloseAction.triggered.connect(lambda: self.showMenuChoice("Schließen"))     
        myToolbar.addAction(fileCloseAction)                                         
        #SHOWME: fileCloseAction.setToolTip("Strg+F4")                  
        #SHOWME: setShortcut("Alt+F4") auf Menü, Änderung, wir brauchen eine Instanzvariable (oben)
        
        self.myStatusBar=QStatusBar()
        self.setStatusBar(self.myStatusBar)
        self.myStatusBar.showMessage('Nicht angemeldet',5000)                       # Einer StatusBar können Widgets hinzugefügt werden (out of scope)

        self.show()

    def showMenuChoice(self, value):
        QMessageBox.information(self, "Information", f"Menü {value} ausgewählt.")
    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec())