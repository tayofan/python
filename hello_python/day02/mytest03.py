#1~45까지 수중에서 6가지를 랜덤 중복없이
#출력하시오
from random import random

def choice_random_N(a,b):
    arr = list(range(1,a+1))
    res = []

    for i in range(1,b+1):
        rnd = int(random() * arr.__len__())
        res.append(arr[rnd])
        arr.remove(arr[rnd])

    return res

if __name__ == '__main__':
    print(choice_random_N(45, 6))
    #오늘 오류 IndexError: list index out of range

