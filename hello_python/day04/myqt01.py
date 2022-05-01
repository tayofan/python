import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *


form_class = uic.loadUiType('myqt01.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.clickedPb)
        
    def clickedPb(self):
        lblText = self.lbl.text();
        
        if lblText == 'Good Morning':
            self.lbl.setText("Good Evening")
        else:
            self.lbl.setText("Good Morning")
            
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
