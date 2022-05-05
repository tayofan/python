import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import random


form_class = uic.loadUiType('myqt09.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le_mine.returnPressed.connect(self.myclick)
        self.show()
        
    def myclick(self):
        mine = self.le_mine.text()
        com = ""
        result = ""
        
        rnd = random.random()
        if rnd > 0.66:
            com = "가위"
        elif rnd > 0.33:
            com = "바위"
        else:
            com = "보"
        
        if mine == "가위" and com == "가위": result += "비겼습니다"
        if mine == "가위" and com == "바위": result += "졌습니다"
        if mine == "가위" and com == "보": result += "이겼습니다"
        
        if mine == "바위" and com == "가위": result += "이겼습니다"
        if mine == "바위" and com == "바위": result += "비겼습니다"
        if mine == "바위" and com == "보": result += "졌습니다"
        
        if mine == "보" and com == "가위": result += "졌습니다"
        if mine == "보" and com == "바위": result += "이겼습니다"
        if mine == "보" and com == "보": result += "비겼습니다"
        
        self.le_com.setText(com)
        self.le_result.setText(result)
        
    # def keyPressEvent(self, e):
    #     if e.key() == 16777220:
    #         self.clickedPb()
    #         print(self.cursor())
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()
