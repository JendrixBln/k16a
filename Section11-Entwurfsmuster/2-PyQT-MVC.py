import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QListView
from PyQt6.QtCore import Qt, QStringListModel


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('PyQt Model/View')

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        model = QStringListModel()
        model.setStringList(['Apple','Banana','Orange'])
        
        self.list_view = QListView()
        self.list_view.setModel(model)
        
        self.combo_box = QComboBox()
        self.combo_box.setModel(model)
        
        layout.addWidget(self.combo_box) 
        layout.addWidget(self.list_view)
                       
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
