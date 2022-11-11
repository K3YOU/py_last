'''
   [문제]
      1 ~ 9 사이의 랜덤 값을 4개 출력한다. 
      랜덤 값이 모두 홀수이면 "당첨"을 출력,
      하나라도 홀수가 아니면 "꽝" 출력한다.
      
      [예시] 
         3 1 5 1 : "당첨"
         5 2 1 4 : "꽝"
'''

import random

a = random.randint(1,9)
b = random.randint(1,9)
c = random.randint(1,9)
d = random.randint(1,9)

run = 1
while run == 1:
   if (a % 2 == 0 ) or (b % 2 == 0 ) or (c % 2 == 0 )  or (d % 2 == 0 ) : 
      print(a,b,c,d,"꽝")
   else :
      print(a,b,c,d,"당첨")
   run = 0