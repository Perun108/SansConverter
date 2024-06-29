from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout


class WarningDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # parent dialog will be UiSelectEncodingsDialog
        self.parent_dialog = parent
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Warning")
        self.resize(300, 100)

        self.layout = QVBoxLayout(self)
        self.label = QLabel(
            "No encodings selected. All available encodings will be used.\n"
            "Do you want to proceed or go back and select encodings?",
            self,
        )
        self.layout.addWidget(self.label)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Yes | QDialogButtonBox.StandardButton.No)
        self.buttonBox.button(QDialogButtonBox.StandardButton.Yes).setText("Use All")
        self.buttonBox.button(QDialogButtonBox.StandardButton.No).setText("Go Back")
        self.buttonBox.accepted.connect(self.accept)  # Yes
        self.buttonBox.rejected.connect(self.reject)  # No

        self.layout.addWidget(self.buttonBox)
