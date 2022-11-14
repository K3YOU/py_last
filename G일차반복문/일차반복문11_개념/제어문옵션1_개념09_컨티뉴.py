'''
    [반복문 옵션 continue]
        반복문은 내부의 모든 식을 실행하고 다시 조건으로 올라가서,
        조건이 사실이면 또 반복하는 방법으로 사용된다.
        continue는 반복문의 내부식을 실행하는 도중에 조건으로 바로 올라갈 때 사용한다.
        break와 마찬가지로 continue도 옵션이기 때문에 
        굳이 사용하지않고도 식을 작성하는데 크게 문제없다.
'''
'''     
    [문제]
        무한반복문안에서 랜덤(1~10) 숫자 하나를 저장한다. 
        숫자가 5이하이면 출력하고, 5초과이면 출력하지않는다.
        총 숫자가 10개 출력되면 종료한다. 
'''
import random

# 기존방법
a = 0
while a < 10:
    r = random.randint(1, 10)   
    if r <= 5:
        print(r , end=" ")
        a += 1
              
print()
print("-------------------")

# continue 사용시
b = 0
while b < 10:
    r = random.randint(1, 10)
    if r > 5:
        continue # 5이하가 아니면 프린트를 하지 말고 계속하라는 뜻이다.
    print(r , end=" ") #5이하이면 프린트를 해라
    b += 1
    
