import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import random


form_class = uic.loadUiType('myqt06.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.clickedPb)
        self.show()
        
    def clickedPb(self):
        arr = list(range(1,45+1))
        res = []
        
        while(True):
            if(len(res) == 6): break
            rnd = int(random.random() * 45)
            if(arr[rnd] == -1): continue
            tmep = arr[rnd]
            arr[rnd] = -1
            res.append(tmep)
         
        self.lbl1.setText(str(res[0]))
        self.lbl2.setText(str(res[1]))
        self.lbl3.setText(str(res[2]))
        self.lbl4.setText(str(res[3]))
        self.lbl5.setText(str(res[4]))
        self.lbl6.setText(str(res[5]))
            
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()
