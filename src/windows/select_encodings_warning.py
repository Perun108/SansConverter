from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox, QPushButton


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

        # self.buttonBox = QDialogButtonBox(self)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        self.buttonBox.button(QDialogButtonBox.Yes).setText("Use All")
        self.buttonBox.button(QDialogButtonBox.No).setText("Go Back")
        self.buttonBox.accepted.connect(self.accept)  # Yes
        self.buttonBox.rejected.connect(self.reject)  # No

        # self.useAllButton = QPushButton("Use all", self)
        # self.selectButton = QPushButton("Select", self)

        # self.buttonBox.addButton(self.useAllButton, QDialogButtonBox.AcceptRole)
        # self.buttonBox.addButton(self.selectButton, QDialogButtonBox.RejectRole)

        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

        # self.useAllButton.clicked.connect(self.accept)
        # self.selectButton.clicked.connect(self.reject)

    # def useAllEncodings(self):
    #     print("USE ALL!")
    #     # Set all available encodings in the parent dialog
    #     self.parent_dialog.selected_encodings = [item.value for item in Encodings]
    #     self.parent_dialog.accept()
    #     self.accept()
