import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


form_class = uic.loadUiType('myqt0A.ui')[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.com = []
        self.pb.clicked.connect(self.clickedPb)
        self.le.returnPressed.connect(self.clickedPb)
        self.show()
        
    def clickedPb(self):
        self.getCom()
        sb = self.getResult()
        if sb[0] == 3:
            QMessageBox.about(self,'이김',"이김")
            self.reset()
            return
        
        old = self.te.toPlainText()
        new = "{}-{}S{}B\n".format(self.le.text(),sb[0],sb[1])
        result = old + new
        self.te.setText(result)
        self.le.setText("")
        print(self.com)
        
    def getCom(self):
        arr = [0,1,2,3,4,5,6,7,8,9]
        rnd = random.random()
        while(True):
            if(len(self.com) == 3): break
            rnd = int(random.random() * 10)
            if not(arr[rnd] == -1): 
                tmep = arr[rnd]
                arr[rnd] = -1
                self.com.append(tmep)
    
    def getResult(self):
        s = 0
        b = 0
        mine = self.le.text()
        
        
        if(int(mine[0]) == self.com[0]): s+=1    
        if(int(mine[0]) == self.com[1]): b+=1    
        if(int(mine[0]) == self.com[2]): b+=1
            
        if(int(mine[1]) == self.com[0]): b+=1    
        if(int(mine[1]) == self.com[1]): s+=1    
        if(int(mine[1]) == self.com[2]): b+=1 
           
        if(int(mine[2]) == self.com[0]): b+=1    
        if(int(mine[2]) == self.com[1]): b+=1    
        if(int(mine[2]) == self.com[2]): s+=1
        
        return s,b
    
    def reset(self):
        self.com = []
        self.getCom()
        self.le.setText("")
        self.te.setText("")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()
