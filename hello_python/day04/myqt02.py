import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


form_class = uic.loadUiType('myqt02.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show()
        
    def myclick(self):
        a = self.le.text()
        aa = int(a)
        aa -= 1
        self.le.setText(str(aa))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()