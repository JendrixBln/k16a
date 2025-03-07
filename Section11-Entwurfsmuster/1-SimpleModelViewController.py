import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel
from PyQt6.QtCore import QStringListModel

class SimpleModelView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Einfaches MVA Beispiel")
        self.setGeometry(100, 100, 300, 100)

        # Layout
        layout = QVBoxLayout()

        # Model: Speichert die Daten (ein einfacher String)
        self.model = QStringListModel()
        self.model.setStringList([""])

        # View 1: Eingabefeld (schreibt ins Modell)
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Gib etwas ein...")
        layout.addWidget(self.input_field)

        # View 2: Label (zeigt die Daten aus dem Modell)
        self.label = QLabel("Hier erscheint dein Text")
        layout.addWidget(self.label)

        # Verbindung zwischen Model und Views
        self.input_field.textChanged.connect(self.update_model)

        self.setLayout(layout)

    def update_model(self, text):
        """Aktualisiert das Modell und zeigt die Änderung in der View an"""
        self.model.setStringList([text])  # Modell aktualisieren
        self.label.setText(self.model.stringList()[0])  # View aktualisieren

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleModelView()
    window.show()
    sys.exit(app.exec())
