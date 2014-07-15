#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
 
class testShadow(QWidget):
 
 
    def __init__(self, parent=None):
 
        super(testShadow, self).__init__(parent)
 
        
        self.resize(960,480)
        self.setStyleSheet("background-color:#ccc")
        self.setWindowTitle(u"PyQt Shadow")
 
        
        self.label = QLabel(self)
        self.label.setStyleSheet("border:5px solid #fff;margin:20px 0 0 20px;")
 
        
        self.img_=QImage(self)
        self.img_.load('saritocat.png')
 
        
        self.label.setPixmap(QPixmap().fromImage(self.img_).scaled(QSize(240,120),Qt.KeepAspectRatio))
 
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setOffset(5,5)
        self.label.setGraphicsEffect(self.shadow)
 
 
 
if __name__ == "__main__":
 
    app = QApplication(sys.argv)
    main = testShadow()
    main.show()
    sys.exit(app.exec_())
