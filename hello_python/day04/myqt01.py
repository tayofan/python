import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


form_class = uic.loadUiType('myqt01.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.clickedPb)
        self.show()
        
    def clickedPb(self):
        lblText = self.lbl.text();
        
        if lblText == 'Good Morning':
            self.lbl.setText("Good Evening")
        else:
            self.lbl.setText("Good Morning")
            
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()
