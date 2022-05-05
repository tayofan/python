import sys

from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.Qt import QSize


#글씨없음 icon40*40 geo 40*40
form_class = uic.loadUiType('myomok01.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.flag_wb = True
                
        for i in range(10):
            for j in range(10):
                obj = QPushButton(self)
                obj.setText('')
                obj.setIcon(QtGui.QIcon('0.png'))
                obj.setIconSize(QSize(40,40))
                obj.setGeometry(0+40*j,0+40*i,40,40)
                obj.clicked.connect(self.myclick)
            
        
        self.pb.clicked.connect(self.myreset)
        self.show()
        
    def myclick(self):
        if self.flag_wb:
            self.sender().setIcon(QtGui.QIcon('1.png'))
        else:
            self.sender().setIcon(QtGui.QIcon('2.png'))
        self.flag_wb = not self.flag_wb
    def myreset(self):
        print()
            
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()
