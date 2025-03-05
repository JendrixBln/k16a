# Quelle:   https://www.pythontutorial.net/pyqt/pyqt-qmessagebox/

import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox, QGridLayout, QPushButton
from PyQt6.QtCore import Qt


class AppWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQT QMessagebox')
        
        layout = QGridLayout(self)
        self.setLayout(layout)

        btn_question = QPushButton('Programm beenden')
        btn_question.clicked.connect(self.quit)

        btn_info = QPushButton('Information ausgeben')
        btn_info.clicked.connect(self.info)

        btn_warning = QPushButton('Warnmeldung ausgeben')
        btn_warning.clicked.connect(self.warning)

        btn_critical = QPushButton('Fehlermeldung ausgeben')
        btn_critical.clicked.connect(self.error)

        layout.addWidget(btn_info)
        layout.addWidget(btn_warning)
        layout.addWidget(btn_critical)
        layout.addWidget(btn_question)

        # show the window
        self.show()
    def quit(self):
        answer =  QMessageBox.question(self,'Bestätigung','Programm beenden?'
                , QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)                   # | ist hier bitweises OR, nicht PIPE
        if answer == QMessageBox.StandardButton.Yes:
            QMessageBox.information(self, 'Information',"Du hast 'ja' gesagt, ich schließe das Programm!", QMessageBox.StandardButton.Ok)
            self.close()
        else:
            QMessageBox.information(self, 'Information',"Du hast 'nein' gesagt, also bleibe ich aktiv.", QMessageBox.StandardButton.Ok)
    def info(self):
        QMessageBox.information(self, 'Information', 'So sieht eine information aus.')              # OK ist default
    def warning(self):
        QMessageBox.warning(self, 'Information', 'Warnmeldungen sehen so aus.')
    def error(self):
        QMessageBox.critical(self, 'Information', 'Das ist eine Fehlermeldung.')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec())