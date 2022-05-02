import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


form_class = uic.loadUiType('myqt05.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.clickedPb)
        self.show()
        
    def clickedPb(self):
        dan = int(self.le.text())
        res = ""
        res += "{} * 1 = {}\n".format(dan,dan*1)
        res += "{} * 2 = {}\n".format(dan,dan*2)
        res += "{} * 3 = {}\n".format(dan,dan*3)
        res += "{} * 4 = {}\n".format(dan,dan*4)
        res += "{} * 5 = {}\n".format(dan,dan*5)
        res += "{} * 6 = {}\n".format(dan,dan*6)
        res += "{} * 7 = {}\n".format(dan,dan*7)
        res += "{} * 8 = {}\n".format(dan,dan*8)
        res += "{} * 9 = {}\n".format(dan,dan*9)
        
        self.te.setText(res) 
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()
