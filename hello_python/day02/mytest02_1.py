import random

arr9 = [1,2,3,4,5,6,7,8,9]

for i in range(100):
    rnd = int(random.random() * 9)
    a = arr9[rnd]
    b = arr9[0]
    arr9[0] = a
    arr9[rnd] = b

# print(arr9[0],arr9[1],arr9[2])
print(arr9[0:3])

