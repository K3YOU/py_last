'''
[최대값]
    [1] 숫자 3개를 랜덤으로 저장한다. (-100 ~ 100 사이의 숫자)
    [2] 3개의 랜덤 숫자를 비교한다.
    [3] 가장 작은 수(MIN)를 출력한다.    
'''


import random

a = random.randint(-100,100)
b = random.randint(-100,100)
c = random.randint(-100,100)

print("a =",a,"b=",b,"c=",c)

min = a

if min > b :     # a>b라고 쓰면 안된다! min은 계속 바뀌는 숫자이므로 if절에서도 계속 mim으로 써줘야한다! 
   min = b 


'''
if b > c :
    min = c
  

if b < c :
    min = b
   ''' 



if min> c :
    min = c


print(min)

