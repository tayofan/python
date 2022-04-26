# 출력하고 싶은 단수를 입력하세요 6 Enter
# 6 * 1 = 6
# .. 출력
dan = input("출력하고 싶은 단수를 입력하세요")
arr = range(1,10)

for i in arr:
    print("{} * {} = {}".format(dan,i,int(dan)*i))
