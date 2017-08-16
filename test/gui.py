import sys
#sys.path.insert(1,'/usr/local/lib/python3.6/site-packages/')
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle('PYQt5 lesson 1')
    w.show()
    sys.exit(app.exec_())

window()
