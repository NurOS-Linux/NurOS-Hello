import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPalette, QColor

class NurOSHello(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Welcome To NurOS")
        self.setGeometry(100, 100, 800, 600)
        
        # Установка светлого фона
        self.setStyleSheet("background-color: #f5f5f5;")  # Светлый фон

        # Установка шрифта
        font = QFont("San Francisco", 12)  # Используйте шрифт, похожий на San Francisco
        self.setFont(font)

        # Создание элементов интерфейса
        self.label = QLabel("Welcome To...", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")

        self.label_2 = QLabel("NurOS", self)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setStyleSheet("font-size: 64px; font-weight: bold; color: #007AFF;")  # Синий цвет, как в MacOS

        self.label_3 = QLabel(
            "<html><head/><body>"
            "<p style='font-size: 16px; color: #555;'>The new and independent operating system based on Linux! You can work with your favourite programs such as FreeOffice, OBS Studio, Blender and Google Chrome with comfort quality and performance.</p>"
            "<p style='font-size: 16px; color: #555;'>We are developers from a non-big company and we can know about user's issues and you can install or delete from the system any packages. Our Linux distribution is minimal and clean out-of-box, but you can still install any other packages such as proprietary. You can support us via Patreon or go to work with us! Check our Telegram below for news, updates and questions. If you have any questions or ideas, you can ask on our Telegram channel.</p>"
            "<p style='font-size: 16px; color: #555;'>By pressing the button below, you will be a member of NurOS.</p>"
            "</body></html>", self)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.label_3.setWordWrap(True)

        self.pushButton = QPushButton("Continue with NurOS", self)
        self.pushButton.setStyleSheet("""
            background-color: #007AFF; 
            color: white; 
            font-weight: bold; 
            padding: 15px; 
            border: none; 
            border-radius: 8px; 
            font-size: 18px;
        """)
        self.pushButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.pushButton.clicked.connect(self.on_continue_button_clicked)

        self.label_4 = QLabel('<a href="https://t.me/nuros_tg"><span style="text-decoration: underline; color:#007AFF;">Telegram (@nuros_tg)</span></a>', self)
        self.label_4.setOpenExternalLinks(True)

        self.label_5 = QLabel('<a href="https://github.com/nuros-linux"><span style="text-decoration: underline; color:#007AFF;">GitHub</span></a>', self)
        self.label_5.setOpenExternalLinks(True)

        self.label_6 = QLabel('<a href="https://nuros.anmitali.kz"><span style="text-decoration: underline; color:#007AFF;">Main website</span></a>', self)
        self.label_6.setOpenExternalLinks(True)

        # Создание компоновки
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.label_2)
        layout.addWidget(self.label_3)
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label_4)
        layout.addWidget(self.label_5)
        layout.addWidget(self.label_6)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def on_continue_button_clicked(self):
        self.close()  # Закрывает текущее окно

def main():
    app = QApplication(sys.argv)
    widget = NurOSHello()
    widget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()