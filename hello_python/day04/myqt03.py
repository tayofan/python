import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


form_class = uic.loadUiType('myqt03.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.clickedPb)
        self.show()
        
    def clickedPb(self):
        a = int(self.le1.text())
        b = int(self.le2.text())
        
        c = a + b
        self.le3.setText(str(c))        
            
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()
