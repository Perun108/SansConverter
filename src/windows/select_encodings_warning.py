from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox, QPushButton
from PyQt5.QtCore import Qt


class WarningDialog(QDialog):
    def __init__(self, parent=None):
        super(WarningDialog, self).__init__(parent)
        self.parent_dialog = parent
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Warning")
        self.resize(300, 100)

        self.layout = QVBoxLayout(self)
        self.label = QLabel(
            "No encodings selected. All available encodings will be used.\nDo you want to proceed or go back and select encodings?",
            self,
        )
        self.layout.addWidget(self.label)

        self.buttonBox = QDialogButtonBox(self)

        self.useAllButton = QPushButton("Use all", self)
        self.selectButton = QPushButton("Select", self)

        self.buttonBox.addButton(self.useAllButton, QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton(self.selectButton, QDialogButtonBox.RejectRole)

        self.layout.addWidget(self.buttonBox)

        self.useAllButton.clicked.connect(self.useAllEncodings)
        self.selectButton.clicked.connect(self.reject)

    def useAllEncodings(self):
        # Set all available encodings in the parent dialog
        self.parent_dialog.selected_encodings = [
            cb.text() for cb in self.parent_dialog.checkboxes
        ]
        self.accept()
