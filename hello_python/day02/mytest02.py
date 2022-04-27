#1~9까지 수중에서 3가지를 랜덤 중복없이
#출력하시오
from random import random

class choice_random:
    def __init__(self,range,count):
        self.arr = list(range(1,range+1))
        self.res = []
        self.count = count
    
    def getres(self):
        for i in range(1,self.count+1):
            rnd = int(random() * self.arr.__len__())
            self.res.append(self.arr[rnd])
            self.arr.remove(self.arr[rnd])


def choice_random_N(a,b):
    arr = list(range(1,a+1))
    res = []

    for i in range(1,b+1):
        rnd = int(random() * arr.__len__())
        res.append(arr[rnd])
        arr.remove(arr[rnd])

    return res

if __name__ == '__main__':
    print(choice_random_N(9, 3))



        
    