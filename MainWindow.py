from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure

from About import AboutDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ice Cream Sales Analysis")
        self.resize(850, 620)

        # TODO: Initialize your two data lists here (e.g., temperatures and revenues)

        self.selected_file = ""

        self._setup_ui()
        self.plot_graph()

    def _setup_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(16)

        # Header / Top Controls Bar
        header_layout = QHBoxLayout()
        header_layout.setSpacing(12)

        title_label = QLabel("Ice Cream Sales Analysis")
        title_label.setObjectName("titleLabel")
        header_layout.addWidget(title_label)

        header_layout.addStretch()

        self.load_button = QPushButton("Load File")
        self.load_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.load_button.clicked.connect(self.load_file)
        header_layout.addWidget(self.load_button)

        self.about_button = QPushButton("About")
        self.about_button.setObjectName("secondaryButton")
        self.about_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.about_button.clicked.connect(self.open_about)
        header_layout.addWidget(self.about_button)

        main_layout.addLayout(header_layout)

        # Chart Container Card (NavigationToolbar + Matplotlib Canvas)
        chart_frame = QFrame(self)
        chart_frame.setObjectName("chartContainer")
        chart_layout = QVBoxLayout(chart_frame)
        chart_layout.setContentsMargins(12, 12, 12, 12)
        chart_layout.setSpacing(8)

        self.figure = Figure(figsize=(8, 5), dpi=100, facecolor="#ffffff")
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.ax = self.figure.add_subplot(111)

        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.toolbar.setObjectName("chartToolbar")

        chart_layout.addWidget(self.toolbar)
        chart_layout.addWidget(self.canvas, stretch=1)

        main_layout.addWidget(chart_frame, stretch=1)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Ice Cream Sales CSV File",
            "",
            "CSV Files (*.csv);;All Files (*)",
        )
        if file_path:
            self.selected_file = file_path

            # TODO: Read the CSV file from file_path, populate your data lists, and call self.plot_graph()

    def plot_graph(self):
        self.ax.clear()

        # TODO: Replace this temporary placeholder plotting logic with your own plot
        dummy_x = [10, 20, 30, 40]
        dummy_y = [250, 500, 700, 900]
        self.ax.plot(
            dummy_x,
            dummy_y,
            marker="o",
            linestyle="--",
            color="#2563eb",
            label="Placeholder Data",
        )
        self.ax.set_title("Ice Cream Sales (Placeholder Chart)")
        self.ax.set_xlabel("Temperature (°C)")
        self.ax.set_ylabel("Revenue ($)")
        self.ax.grid(True, linestyle=":", alpha=0.6)
        self.ax.legend()

        self.figure.tight_layout()
        self.canvas.draw()

    def open_about(self):
        dialog = AboutDialog(self)
        dialog.exec()
