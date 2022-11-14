'''
    [문제]
        랜덤 숫자(1~5)를 한 개 저장한다. 
        랜덤 숫자만큼 반복문을 돌리고, 
        저장한 랜덤 숫자를 계속 저장한다.
    [예시]
        r = 3 
        arr = [3,3,3]
    [예시]
        r = 5
        arr = [5,5,5,5,5]  
'''
arr = [] #빈리스트인데 저장을 한다 => arr.append()

import random
r=random.randint(1,5)
print(r)

#반복문을 돌린다
#for문 사용
for i in range(r) :
    arr.append(r)
print(arr)

print()

#while문 사용
arr1 = [] 
r1= random.randint(1,5)
print(r1)
i = 0
while i < r1:
    arr1.append(r1)
    i += 1

print(arr1)




