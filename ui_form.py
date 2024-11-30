# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_NurOSHello(object):
    def setupUi(self, NurOSHello):
        if not NurOSHello.objectName():
            NurOSHello.setObjectName(u"NurOSHello")
        NurOSHello.resize(800, 600)
        self.pushButton = QPushButton(NurOSHello)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 460, 151, 41))
        self.pushButton.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label = QLabel(NurOSHello)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 0, 181, 91))
        font = QFont()
        font.setFamilies([u"Cantarell"])
        font.setPointSize(20)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(NurOSHello)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 40, 261, 131))
        font1 = QFont()
        font1.setFamilies([u"Cantarell"])
        font1.setPointSize(48)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setCursor(QCursor(Qt.CursorShape.ClosedHandCursor))
        self.label_2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(NurOSHello)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 170, 781, 281))
        font2 = QFont()
        font2.setFamilies([u"Cantarell"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_3.setFont(font2)
        self.label_3.setLocale(QLocale(QLocale.English, QLocale.Netherlands))
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_4 = QLabel(NurOSHello)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 510, 141, 18))
        self.label_5 = QLabel(NurOSHello)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 510, 51, 18))
        self.label_5.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label_6 = QLabel(NurOSHello)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(490, 510, 58, 18))
        self.label_6.setLocale(QLocale(QLocale.English, QLocale.Ghana))
        self.label_7 = QLabel(NurOSHello)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(220, 530, 371, 51))
        font3 = QFont()
        font3.setFamilies([u"Cantarell"])
        font3.setPointSize(8)
        font3.setItalic(False)
        self.label_7.setFont(font3)
        self.label_7.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.retranslateUi(NurOSHello)

        QMetaObject.connectSlotsByName(NurOSHello)
    # setupUi

    def retranslateUi(self, NurOSHello):
        NurOSHello.setWindowTitle(QCoreApplication.translate("NurOSHello", u"NurOSHello", None))
        self.pushButton.setText(QCoreApplication.translate("NurOSHello", u"Continue with NurOS", None))
        self.label.setText(QCoreApplication.translate("NurOSHello", u"Welcome To...", None))
        self.label_2.setText(QCoreApplication.translate("NurOSHello", u"NurOS", None))
        self.label_3.setText(QCoreApplication.translate("NurOSHello", u"<html><head/><body><p>The new and indepent operating system based on Linux! You can work with your favourite programs such as FreeOffice OBS Studio,</p><p>Blender and Google Chrome with comfort quality and performance.</p><p>We are developers from non-big company and we can know about user's issues. You can support us via Patreon or go to work with us!</p><p>Check our Telegram below for news, updates and questions. If you have any questions or ideas</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("NurOSHello", u"<html><head/><body><p><a href=\"https://t.me/nuros_tg\"><span style=\" text-decoration: underline; color:#2980b9;\">Telegram (@nuros_tg)</span></a></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("NurOSHello", u"<html><head/><body><p><a href=\"https://github.com/nuros-linux\"><span style=\" text-decoration: underline; color:#2980b9;\">GitHub</span></a></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("NurOSHello", u"<html><head/><body><p><a href=\"https://nuros.anmitali.kz\"><span style=\" text-decoration: underline; color:#2980b9;\">Main website</span></a></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("NurOSHello", u"<html><head/><body><p><span style=\" font-size:6pt;\">Copyright </span><span style=\" font-family:'sans-serif'; font-size:6pt; color:#202122; background-color:#ffffff;\">\u00a9 NurOS - AnmiTali 2024</span></p><p><span style=\" font-size:6pt;\">Linux</span><span style=\" font-family:'sans-serif'; font-size:6pt; font-weight:700; color:#202122; background-color:#ffffff;\">\u00ae </span><span style=\" font-family:'sans-serif'; font-size:6pt; color:#202122; background-color:#ffffff;\">is registered trademark of Linus Torvalds in Kazakhstan and in other countries.</span></p></body></html>", None))
    # retranslateUi

