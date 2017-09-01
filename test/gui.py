#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
"""
ZetCode PyQt5 tutorial
 
In this example, we create a simple
window in PyQt5.
 
author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""
 
import sys
sys.path.insert(1,'/usr/local/lib/python3.6/site-packages/PyQt5/QtWidgets.so')
from PyQt5.QtWidgets import QApplication, QWidget
 
if __name__ == '__main__':
 
    app = QApplication(sys.argv)
 
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
 
    sys.exit(app.exec_())
