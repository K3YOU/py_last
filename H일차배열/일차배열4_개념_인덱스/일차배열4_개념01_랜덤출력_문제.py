'''
    [문제]
        [조건1] 리스트에 랜덤숫자(1~100) 5개를 추가하고,
        [조건2] 랜덤으로 위 값 중 한 개만 출력하시오. 
    
    [예시]
        a = [1, 43, 22, 77 ,44]
        출력 : 22
'''

a = []


import random

for i in range (5) : #i가 0부터 시작해서 ()의 수는 포함 안 한다고 생각하면 쉽다.
    r = random.randint(1,100)
    a.append(r)
print(a)

r1 = random.randint(0,4)
print("출력 :",end= " ")
if r1 == 0:
    print(a[0])
if r1 == 1:
    print(a[1])
if r1 == 2:
    print(a[2])
if r1 == 3:
    print(a[3])
if r1 == 4:
    print(a[4])


