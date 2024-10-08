"""Select Encodings dialog window generated by QtDesigner with edits"""

from PyQt6.QtCore import QCoreApplication, QMetaObject, Qt
from PyQt6.QtWidgets import (
    QCheckBox,
    QDialog,
    QDialogButtonBox,
    QGridLayout,
    QVBoxLayout,
)

from src.windows.select_encodings_warning import WarningDialog


class UiSelectEncodingsDialog(QDialog):
    """Enable/Disable encodings GUI"""

    def __init__(self, parent):
        super().__init__(parent)
        # parent dialog will be SansConverter
        self.parent_dialog = parent
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Select encodings", None))
        self.mainLayout = QVBoxLayout(Dialog)
        self.gridLayout = QGridLayout()
        self.mainLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)
        self.mainLayout.addWidget(self.buttonBox)

        self._add_checkboxes(Dialog)

        self.buttonBox.accepted.connect(self.check_selected_encodings)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(Dialog)

    def _add_checkboxes(self, dialog):
        """Add checkBoxes for all encodings for users to select from"""

        self.checkboxes = []
        for idx, encoding in enumerate(self.parent_dialog.all_encodings):
            checkbox = QCheckBox(dialog)
            checkbox.setObjectName(f"checkBox_{idx}")
            checkbox.setText(QCoreApplication.translate("Dialog", encoding, None))
            if encoding in self.parent_dialog.selected_encodings:
                checkbox.setChecked(True)
            # We won't have more than 8 encodings, so 4 is good for the foreseen future
            self.gridLayout.addWidget(checkbox, idx % 4, idx // 4, 1, 1)
            self.checkboxes.append(checkbox)

    def get_selected_encodings(self):
        """Returns a list of selected encodings"""
        return [cb.text() for cb in self.checkboxes if cb.isChecked()]

    def check_selected_encodings(self):
        selected_encodings = self.get_selected_encodings()
        if not selected_encodings:
            warning_dialog = WarningDialog(self)
            # Accepted here means 'Use All Available Encodings'
            if warning_dialog.exec() == QDialog.DialogCode.Accepted:
                self.selected_encodings = self.parent_dialog.all_encodings
                self.accept()
            else:
                return
        else:
            self.selected_encodings = selected_encodings
            self.accept()
