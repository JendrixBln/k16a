import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeView
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtCore import QDir

class FileExplorer(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Ordnerstruktur von C:\\")
        self.setGeometry(100, 100, 800, 600)
        
        self.model = QFileSystemModel()
        self.model.setRootPath("C:\\")
        self.model.setFilter(QDir.Filter.AllDirs | QDir.Filter.NoDotAndDotDot)
        
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index("C:\\"))
        
        self.setCentralWidget(self.tree_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileExplorer()
    window.show()
    sys.exit(app.exec())
