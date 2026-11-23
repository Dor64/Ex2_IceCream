import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)

    # Load external QSS stylesheet
    style_path = Path(__file__).resolve().parent / "style.qss"
    if style_path.exists():
        with open(style_path, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
