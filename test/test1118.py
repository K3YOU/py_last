"""
[문제]
    아래 리스트에 랜덤숫자 (1~30) 을  10개 저장한다. 
    단, 홀수만 저장하고 , 중복숫자는 없어야 한다. 
[예시]
    a = [29, 1, 5, 9 , 21, 25, 7, 3, 13, 15]

"""
import random
'''
a = []
b = 0

for i in range(10) :
    
    r=random.randint(1,30)
    if r % 2 != 0 :

        b = a.append(r)

        r1=random.randint(1,30)
        if b != r1 and r1 %2 != 0:
            a.append(r1)
            
print(a)
'''


##중복숫자 없애는거 모르겠어

#-1. 홀수만 출력하기

a = []
b = []
i = 1
while i <= 30:
    if i % 2 == 1:
        b.append(i)
    i += 1
print("홀수만",b)

#-2. 중복안되게 배열

i = 0
while i < 10000:
    r = random.randint(0, 14) #배열의 '순서'를 랜덤으로 뽑는다   #a라는 배열은 요소가 30개였는데 b는 홀수만 다루므로 요소들의 수가 15개가 된다.
    temp = b[0] 
    b[0] = b[r]
    b[r] = temp 
    i += 1
print("홀수로 배열 랜덤",b)

#-3. a배열에 b배열넣기

for i in range(10): 
    a.append(b[i])
print(a)