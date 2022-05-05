import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


form_class = uic.loadUiType('myqt07.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.clickedPb)
        self.show()
        
    def clickedPb(self):
        first = 0
        last = 0
        result = ""
        
        
        if self.le_first.text() != "":
            first = int(self.le_first.text())
            last = int(self.le_last.text())
        
            for i in range(first, last + 1):
                # for j in range(1,i + 1):
                #     result += "*"
                # result += "\n"
                result += self.drawStar(i)
        
        else:
            result = "첫별수와 끝별수를 모두 입력해주세요"
        
        self.te.setText(result)  
          
    def drawStar(self,cnt):
        ret = ""
        for i in range(cnt):
            ret += "*"
        ret += "\n"
        return ret        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()
