'''
    [문제]
        랜덤 숫자(1~10) 다섯 개를 arr에 추가하고
        그 두 배를 total에 저장 후 출력하시오.
    [예시]
        arr   = [10, 3, 4, 2, 6]
        total = [20, 6, 8, 4, 12]
'''

arr = []
total = []

import random

i = 0
while i < 5:
    a = random.randint(1,10)
    arr.append(a)

    total.append(2*a)
    i += 1    
print(arr)
print(total)

