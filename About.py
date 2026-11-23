from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("About - Ice Cream Sales Analysis")
        self.setFixedSize(420, 220)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        title_label = QLabel("Ice Cream Sales Analysis")
        title_label.setObjectName("aboutTitleLabel")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        author_label = QLabel("Created by: <b>Dor Tal</b>")
        author_label.setObjectName("aboutTextLabel")
        author_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(author_label)

        repo_url = "https://github.com/Dor64/Ex2_IceCream"
        link_label = QLabel(
            f'GitHub Repository:<br><a href="{repo_url}" style="color: #2563eb;">{repo_url}</a>'
        )
        link_label.setObjectName("aboutLinkLabel")
        link_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        link_label.setTextFormat(Qt.TextFormat.RichText)
        link_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextBrowserInteraction
        )
        link_label.setOpenExternalLinks(True)
        layout.addWidget(link_label)

        layout.addStretch()

        button_layout = QHBoxLayout()
        button_layout.addStretch()

        close_button = QPushButton("Close")
        close_button.setCursor(Qt.CursorShape.PointingHandCursor)
        close_button.clicked.connect(self.accept)
        button_layout.addWidget(close_button)

        button_layout.addStretch()
        layout.addLayout(button_layout)
