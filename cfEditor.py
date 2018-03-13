# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

import cf

if __name__ == '__main__':
    cfile = cf.command_file("./commnad.csv")

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250,250)
    w.setWindowTitle("Command File Editor")

    table = QTableWidget(w)
    #tableItem = QTableWidgetItem()

    table.setRowCount(2)
    table.setColumnCount(2)

    horzHeaders = ["Name", "Age"]
    table.setHorizontalHeaderLabels( horzHeaders )

    table.setItem(0,0, QTableWidgetItem("tom"))
    table.setItem(0,1, QTableWidgetItem("15"))
    table.setItem(1,0, QTableWidgetItem("Ken"))
    table.setItem(1,1, QTableWidgetItem("44"))
    
    w.show()

    sys.exit(app.exec_())
