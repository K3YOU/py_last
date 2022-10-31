'''
[최대값]
    [1] 숫자 3개를 랜덤으로 저장한다. (1~1000 사이의 숫자)
    [2] 3개의 랜덤 숫자를 비교한다.
    [3] 가장 큰 수(MAX)를 출력한다.    
'''

import random

a = random.randint(1, 1000)     # 263
b = random.randint(1, 1000)     # 417
c = random.randint(1, 1000)     # 320

if a > b and a > c:
    print(a)
if b > a and b > c:
    print(b)
if c > a and c > b:
    print(c)

print("-----------------")

max = a   # max =a 를 써줘야하는 이유! a가 b보다 큰 경우 첫 if 절은 넘어가고 두번째 if절부터 시작
#변수를 추가적으로 더 쓰기!!!

if max < b:
    max = b
if max < c: 
    max = c

print(a , " ", b, " ", c)
print("가장 큰 값 : ", max)



