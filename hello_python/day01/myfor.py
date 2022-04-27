import random

a = input("홀/짝을 입력하세요")
result = ""
com = ""

rnd = random.random()
if rnd > 0.5:
    com = "홀"
else:
    com = "짝"

if com == a:
    result = "이김"
else:
    result = "짐"

print("com",com)
print("mine",a)
print("result",result)

