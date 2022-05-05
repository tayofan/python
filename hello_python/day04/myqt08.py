import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


form_class = uic.loadUiType('myqt08.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb0.clicked.connect(self.myclick)
        self.pb_call.clicked.connect(self.mycall)
        self.show()
        
   
    def mycall(self):
        tel = self.le.text()
        QMessageBox.about(self,'통화중',tel+"로 전화를 거는중 입니다")
        self.le.setText("")
        
    def myclick(self):
        old = self.le.text()
        new = self.sender().text()
        self.le.setText(old + new)
            
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()
