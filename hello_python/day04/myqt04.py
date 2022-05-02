import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import random


form_class = uic.loadUiType('myqt04.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.clickedPb)
        self.show()
        
    def clickedPb(self):
        rnd = random.random()
        mine = self.le_mine.text()
        if(rnd > 0.5):
            com = "홀"
        else:
            com = "짝"
        
        if(mine == com): result = "이겼습니다"
        else: result = "졌습니다"
        
        self.le_com.setText(com)
        self.le_result.setText(result)
        
            
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()
