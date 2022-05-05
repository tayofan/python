import random

arr45 = list(range(1,45+1))
arr6 = []

while True:
    rnd = int(random.random() * 45)
    if arr45[rnd] == -1:
        pass
    else:
        arr6.append(arr45[rnd])
        arr45[rnd] = -1
    if len(arr6) >= 6:
        break
    
print(arr6)