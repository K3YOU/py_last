'''
    [문제]
        a리스트와 b리스트에 랜덤 숫자(1~100)를 다섯 개씩 저장하고,
        a리스트의 전체 합과 b리스트의 값들 중 홀수의 합만 출력하시오. 
        a리스트의 홀수 합과 b리스트의 홀수 합을 비교해서 더 큰 값을 출력하시오.
        서로 같으면 둘 다 출력하시오.
    [예시]
        a = [28, 79, 47, 70, 36]
        b = [63, 4, 45, 54, 87]
        total1 = 126
        total2 = 195
        195    
'''
import random

a = []
b = []

sum1 =0
sum2 =0 

i = 0
for i in range (6) :
    r =random.randint(1,100)
    a.append(r)
    
    r1 =random.randint(1,100)
    b.append(r1)
    
    if a[i] % 2 !=  0 :
        sum1 += a[i]
    if b[i] % 2 !=0 :
        sum2 +=b[i]

i += 1

print(a)
print(b)
print(sum1)
print(sum2)

if sum1 == sum2:
    print(sum1,sum2)
elif sum1 > sum2 :
    print(sum1)
else:
    print(sum2)