import sys

from PyQt5 import uic, QtGui
from PyQt5.Qt import QSize
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox


#글씨없음 icon40*40 geo 40*40
form_class = uic.loadUiType('myomok02.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.flag_wb = True
        self.flag_over = False
        self.pb2d = []
        self.arr2d = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
           
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
        ]
                
        for i in range(10):
            line = []
            for j in range(10):
                obj = QPushButton(self)
                obj.setText('')
                obj.setIcon(QtGui.QIcon('0.png'))
                obj.setIconSize(QSize(40,40))
                obj.setGeometry(40*j,40*i,40,40)
                obj.clicked.connect(self.myclick)
                obj.setToolTip("{},{}".format(i,j))
                line.append(obj)
            self.pb2d.append(line)
        
        self.myrender()
        self.pb.clicked.connect(self.myreset)
        self.show()
    
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2d[i][j] == 1:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('1.png'))
                    
                if self.arr2d[i][j] == 2:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('2.png'))
                    
                if self.arr2d[i][j] == 0:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('0.png'))
        
    def myclick(self):
        if self.flag_over:
            return
        
        str = self.sender().toolTip()
        xy = str.split(",")
        i = int(xy[0])
        j = int(xy[1])
        if self.arr2d[i][j] > 0: return
        
        stone = -1    
        if self.flag_wb:
            self.arr2d[i][j] = 1
            stone = 1
        else:
            self.arr2d[i][j] = 2
            stone = 2
        
        up = self.checkUP(i,j,stone)
        dw = self.checkDW(i,j,stone)
        ri = self.checkRI(i, j, stone)
        le = self.checkLE(i, j, stone)
        ur = self.checkUR(i, j, stone)
        ul = self.checkUL(i, j, stone)
        dr = self.checkDR(i, j, stone)
        dl = self.checkDL(i, j, stone)
        
        d1 = up + dw + 1
        d2 = ri + le + 1
        d3 = ur + dl + 1
        d4 = ul + dr + 1
        
        self.myrender()
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            self.flag_over = True
            if self.flag_wb : res = "흰돌"
            else: res = "흑돌"
            QMessageBox.about(self,'이김',res+"이김")
            
        
        self.flag_wb = not self.flag_wb
    
    def checkUR(self,i,j,stone):
        cnt = 0
        try:
            while(True):
                i -= 1
                j += 1
                if j < 0: return cnt
                if i < 0: return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt    
        except:
            return cnt
        
    def checkUL(self,i,j,stone):
        cnt = 0
        try:
            while(True):
                i -= 1
                j -= 1
                if j < 0: return cnt
                if i < 0: return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt    
        except:
            return cnt
        
    def checkDR(self,i,j,stone):
        cnt = 0
        try:
            while(True):
                i += 1
                j += 1
                if j < 0: return cnt
                if i < 0: return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt    
        except:
            return cnt
        
    def checkDL(self,i,j,stone):
        cnt = 0
        try:
            while(True):
                i += 1
                j -= 1
                if j < 0: return cnt
                if i < 0: return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt    
        except:
            return cnt
     
    def checkUP(self,i,j,stone):
        cnt = 0
       
        while True :
            i -= 1
            if i < 0: return cnt
            if self.arr2d[i][j] == stone:
                cnt += 1
            else:
                return cnt
             
                
    def checkDW(self,i,j,stone):
        cnt = 0
        try:
            while(True):
                i += 1
                if i < 0: return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt    
        except:
            return cnt 
                 
    def checkRI(self,i,j,stone):
        cnt = 0
        try:
            while(True):
                j += 1
                if j < 0: return cnt
                if i < 0: return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt    
        except:
            return cnt 
                 
    def checkLE(self,i,j,stone):
        cnt = 0
        try:
            while(True):
                j -= 1
                if j < 0: return cnt
                if i < 0: return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt    
        except:
            return cnt          
    
    # RI, LE, UR, UL, DR, DL
    # D1 = up + dw + 1
    # D2 = ur + dl + 1
    # D3 = ri + le + 1
    # D4 = ul + dr + 1    
    def myreset(self):
        self.flag_wb = True
        self.flag_over = False
        self.arr2d = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
           
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
        ]    
        self.myrender()    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()
