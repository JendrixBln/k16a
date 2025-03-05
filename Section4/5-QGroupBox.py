# Quelle:  https://www.pythontutorial.net/pyqt/pyqt-qgroupbox/
# Aufgabe: Analysiert den Beispielcode. Ihr solltet verstehen, wie man Widgets in GroupBox-Widgets einfügen kann. Stellt sicher, dass 
#          Ihr bei Bedarf Widgets in GroupBoxen gruppieren könnt, ohne lange zu recherchieren ("PSP", CodeStub)

import sys
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QGroupBox, QLabel                                             
from PyQt6.QtCore import Qt


class AppWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQT GroupBox')
        
        # create a grid layout
        layoutform = QVBoxLayout()
        layoutgrp1 = QVBoxLayout()
        layoutgrp2 = QVBoxLayout()
        self.setLayout(layoutform)

        grp1 = QGroupBox("Gruppe 1")
        grp1.setLayout(layoutgrp1)
        grp2 = QGroupBox("Gruppe 2")
        grp2.setLayout(layoutgrp2)

        lbl1_1 = QLabel("Ich bin in Gruppe 1", grp1)
        lbl1_2 = QLabel("Ich bin auch in Gruppe 1", grp1)

        lbl2_1 = QLabel("Ich bin in Gruppe 2", grp2)
        lbl2_2 = QLabel("Ich bin auch in Gruppe 2", grp2)

        lbl3 = QLabel("Ich bin auf dem Hauptfenster", self)

        layoutgrp1.addWidget(lbl1_1)
        layoutgrp1.addWidget(lbl1_2)
        layoutgrp2.addWidget(lbl2_1)
        layoutgrp2.addWidget(lbl2_2)
        layoutform.addWidget(grp1)
        layoutform.addWidget(grp2)
        layoutform.addWidget(lbl3)

        # show the window
        self.show()

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec())