'''
    [문제]
        [조건1] 배열에 랜덤숫자(1~100) 5개를 추가하고,
        [조건2] 짝수만 출력하시오.
        [조건3] 짝수의 누적 합을 저장 후 출력하시오.
        [조건4] 짝수의 개수를 출력하시오.
    
    [예시]
        arr = [68, 81, 84, 72, 81]
        68
        84
        72

        개수 = 3
        합 = 224
'''

arr = []

sum = 0
count = 0

import random

for i in range (5) :
    a =random.randint(1,100)
    arr.append(a)
    if arr[i] % 2== 0 :
        print("even :",arr[i])
        sum += arr[i]
        count += 1
    i += 1
print(arr)
print("count",count)
print("sum",sum)



