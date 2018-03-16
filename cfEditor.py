# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

#import cf
import csvParse

if __name__ == '__main__':
    #cfile = cf.command_file("./commnad.csv")
    csvfile = csvParse.csvParse("./command.csv")

    print("Col="+str(csvfile.CountCol()))
    print("Row="+str(csvfile.CountRow()))

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500,500)
    w.setWindowTitle("Command File Editor")

    table = QTableWidget()
    table.resize(w.size().width(),w.size().height())
    table.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
    #tableItem = QTableWidgetItem()

    table.setRowCount(csvfile.CountCol())
    table.setColumnCount(csvfile.CountRow())

    horzHeaders = []
    for i in range(1,csvfile.CountCol()+1):
        horzHeaders.append("Col"+str(i))
    table.setHorizontalHeaderLabels( horzHeaders )

    for i in range(0,csvfile.CountRow()):
        for j in range(0,len(csvfile.data[i])):
            table.setItem(i,j, QTableWidgetItem(csvfile.data[i][j]))
    
    layout = QHBoxLayout()
    layout.addWidget(table)
    w.setLayout(layout)

    w.show()

    sys.exit(app.exec_())
