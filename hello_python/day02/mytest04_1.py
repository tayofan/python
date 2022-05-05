# 첫수를 넣으세요 1
# 끝수를 넣으세요 5
# 배수를 넣으세요 2
# 1에서 부터 5까지의 2의 배수의 합은 6입니다.

#입력
start = int(input("첫수를 넣으세요"))
end = int(input("끝수를 넣으세요"))
num = int(input("배수를 넣으세요"))
sum = 0

#처리
for i in range(start,end+1):
    if i % num == 0:
        sum += i

#출력
print(sum)