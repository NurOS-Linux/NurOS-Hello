/********************************************************************************
** Form generated from reading UI file 'nuroshello.ui'
**
** Created by: Qt User Interface Compiler version 6.8.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_NUROSHELLO_H
#define UI_NUROSHELLO_H

#include <QtCore/QLocale>
#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_NurOSHello
{
public:
    QWidget *centralwidget;
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QPushButton *pushButton;
    QLabel *label_4;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *NurOSHello)
    {
        if (NurOSHello->objectName().isEmpty())
            NurOSHello->setObjectName("NurOSHello");
        NurOSHello->resize(800, 600);
        QIcon icon(QIcon::fromTheme(QIcon::ThemeIcon::UserAvailable));
        NurOSHello->setWindowIcon(icon);
        NurOSHello->setToolButtonStyle(Qt::ToolButtonStyle::ToolButtonIconOnly);
        centralwidget = new QWidget(NurOSHello);
        centralwidget->setObjectName("centralwidget");
        label = new QLabel(centralwidget);
        label->setObjectName("label");
        label->setGeometry(QRect(320, 10, 151, 51));
        QFont font;
        font.setPointSize(15);
        font.setItalic(true);
        label->setFont(font);
        label->setLocale(QLocale(QLocale::English, QLocale::UnitedStates));
        label->setAlignment(Qt::AlignmentFlag::AlignCenter);
        label_2 = new QLabel(centralwidget);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(270, 40, 251, 101));
        QPalette palette;
        QBrush brush(QColor(98, 160, 234, 255));
        brush.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Text, brush);
        palette.setBrush(QPalette::Active, QPalette::Accent, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Text, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Accent, brush);
        palette.setBrush(QPalette::Disabled, QPalette::Accent, brush);
        label_2->setPalette(palette);
        QFont font1;
        font1.setFamilies({QString::fromUtf8("Comfortaa")});
        font1.setPointSize(40);
        label_2->setFont(font1);
        label_2->setCursor(QCursor(Qt::CursorShape::ClosedHandCursor));
        label_2->setStyleSheet(QString::fromUtf8("label_2{\n"
"rgb(98, 160, 234)\n"
"}"));
        label_2->setLocale(QLocale(QLocale::English, QLocale::UnitedStates));
        label_2->setTextFormat(Qt::TextFormat::AutoText);
        label_2->setAlignment(Qt::AlignmentFlag::AlignCenter);
        label_3 = new QLabel(centralwidget);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(30, 140, 731, 291));
        QFont font2;
        font2.setFamilies({QString::fromUtf8("Comfortaa")});
        font2.setPointSize(13);
        font2.setItalic(false);
        label_3->setFont(font2);
        label_3->setCursor(QCursor(Qt::CursorShape::PointingHandCursor));
        label_3->setLayoutDirection(Qt::LayoutDirection::LeftToRight);
        label_3->setTextFormat(Qt::TextFormat::AutoText);
        label_3->setScaledContents(false);
        label_3->setAlignment(Qt::AlignmentFlag::AlignLeading|Qt::AlignmentFlag::AlignLeft|Qt::AlignmentFlag::AlignTop);
        label_3->setWordWrap(true);
        pushButton = new QPushButton(centralwidget);
        pushButton->setObjectName("pushButton");
        pushButton->setGeometry(QRect(290, 430, 221, 61));
        label_4 = new QLabel(centralwidget);
        label_4->setObjectName("label_4");
        label_4->setGeometry(QRect(180, 530, 531, 20));
        QFont font3;
        font3.setPointSize(10);
        font3.setItalic(true);
        label_4->setFont(font3);
        NurOSHello->setCentralWidget(centralwidget);
        menubar = new QMenuBar(NurOSHello);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 800, 25));
        NurOSHello->setMenuBar(menubar);
        statusbar = new QStatusBar(NurOSHello);
        statusbar->setObjectName("statusbar");
        NurOSHello->setStatusBar(statusbar);

        retranslateUi(NurOSHello);
        QObject::connect(pushButton, &QPushButton::clicked, NurOSHello, qOverload<>(&QMainWindow::close));

        QMetaObject::connectSlotsByName(NurOSHello);
    } // setupUi

    void retranslateUi(QMainWindow *NurOSHello)
    {
        NurOSHello->setWindowTitle(QCoreApplication::translate("NurOSHello", "Hello, NurOS!", nullptr));
        label->setText(QCoreApplication::translate("NurOSHello", "Welcome To...", nullptr));
#if QT_CONFIG(tooltip)
        label_2->setToolTip(QCoreApplication::translate("NurOSHello", "<html><head/><body><p>NurOS</p></body></html>", nullptr));
#endif // QT_CONFIG(tooltip)
        label_2->setText(QCoreApplication::translate("NurOSHello", "NurOS", nullptr));
        label_3->setText(QCoreApplication::translate("NurOSHello", "The new and independent operating system based on Linux! You can work with your favourite programs with comfort quality and performance.\n"
"\n"
"We are developers from a non-big company. You can install and delete from the system any packages. Our Linux distribution is minimalistic and clean out-of-box, but you can still install any other packages such as proprietary.\n"
"\n"
"You can support us via Patreon or go to work with us! Check our Telegram below for news, updates and questions. If you have any questions or ideas, you can ask on our Telegram channel.\n"
"\n"
"\n"
"\n"
"\n"
"By pressing the button below you will be a member of NurOS!", nullptr));
        pushButton->setText(QCoreApplication::translate("NurOSHello", "Continue", nullptr));
        label_4->setText(QCoreApplication::translate("NurOSHello", "Copyright \302\251 AnmiTali - NurOS (nuros.org; @nuroslinux). All rights reserved", nullptr));
    } // retranslateUi

};

namespace Ui {
    class NurOSHello: public Ui_NurOSHello {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_NUROSHELLO_H
