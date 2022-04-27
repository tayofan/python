# 가위바위보를 선택하세요 가위 Enter
# 나:가위
# 컴:바위
# 결과:짐
import random

mine = ""
com = 0
result = ""

# 1:가위 2:바위 3:보
mine = input("가위/바위/보를 입력하세요")
com = random.randint(1,4)
if (mine == '가위' and com == 1) or (mine == '바위' and com == 2) or (mine == '보' and com == 3):
    result = "비겼습니다."
elif (mine == '가위' and com == 3) or (mine == '바위' and com == 1) or (mine == '보' and com == 2):
    result = "이겼습니다."
else:
    result = "졌습니다."

print("mine",mine)
print("com",com)
print("result",result)
