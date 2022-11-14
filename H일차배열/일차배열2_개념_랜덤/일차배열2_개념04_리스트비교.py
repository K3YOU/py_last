'''
    [문제]
        리스트 a와 리스트 b에 랜덤 숫자(1~10) 다섯 개씩 저장한다.
        a와 b를 각각 비교해서 더 큰 값을 출력하시오.
        서로 같으면 둘 다 출력하시오.
'''
import random

a = []
b = []
for i in range(5): #랜덤 숫자 다섯 개씩 저장한다.
    r = random.randint(1, 10)
    a.append(r)
    r = random.randint(1, 10)
    b.append(r)

print("a : " , a)
print("b : " , b)

for i in range(len(a)): #리스트들의 각 값들을 비교한다.
    if a[i] > b[i]:
        print("a : " , a[i])
    elif a[i] < b[i] : 
        print("b : " , b[i])
    else:
        print("a : " , a[i] , ", b : " , b[i])


