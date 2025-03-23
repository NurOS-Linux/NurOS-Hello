#include "nuroshello.h"
#include "./ui_nuroshello.h"

NurOSHello::NurOSHello(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::NurOSHello)
{
    ui->setupUi(this);
}

NurOSHello::~NurOSHello()
{
    delete ui;
}
