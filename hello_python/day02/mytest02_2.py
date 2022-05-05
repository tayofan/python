import random

arr9 = [1,2,3,4,5,6,7,8,9]
arr3 = []

while True:
    rnd = int(random.random() * 9)
    if arr9[rnd] == -1:
        pass
    else:
        arr3.append(arr9[rnd])
        arr9[rnd] = -1
    if len(arr3) >= 3:
        break
    
print(arr3)
   
