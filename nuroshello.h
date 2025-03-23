#ifndef NUROSHELLO_H
#define NUROSHELLO_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class NurOSHello;
}
QT_END_NAMESPACE

class NurOSHello : public QMainWindow
{
    Q_OBJECT

public:
    NurOSHello(QWidget *parent = nullptr);
    ~NurOSHello();

private:
    Ui::NurOSHello *ui;
};
#endif // NUROSHELLO_H
