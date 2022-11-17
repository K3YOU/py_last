'''
    [문제]
        [조건1] 리스트에 랜덤숫자(1~100) 5개를 추가하고,
        [조건2] 랜덤으로 위 값 중 한 개만 출력하시오. 
    
    [예시]
        a = [1, 43, 22, 77 ,44]
        출력 : 22
'''

import random

a = []

for i in range(5):
    r = random.randint(1, 100)
    a.append(r)
print("a =", a)

index = random.randint(0, len(a) - 1) #랜덤넘버에서 0에서 4까지를 나타내기/for처럼 범위미포함이 아니니깐

print("index =", index)
print(a[index]) #a[i]대신에 index를 넣기


