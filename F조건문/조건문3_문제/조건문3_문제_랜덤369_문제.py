'''
[문제]
	[1] 1~99 사이의 랜덤 숫자를 저장한다.
	
	랜덤 숫자 중에서 3이나 6이나 9의 개수가
	[2-1] 2개이면, 짝짝을 출력한다.
	[2-2] 1개이면, 짝을 출력한다.
	[2-3] 0개이면, 해당 숫자를 출력하시오.
	
	[예]
		33	==> 짝짝
		16	==> 짝
		 7	==> 7
'''

import random

a = random.randint(1,99)
print(a)


#a = 30
b = a // 10
c = a % 10


#count = 2
if b % 3 == 0 and c % 3 == 0 :
	print("짝짝")

#count = 1
if b % 3 != 0 and c % 3 == 0 :
	print("짝")

if b % 3 == 0 and c % 3 != 0 :
	print("짝")

#count = 0
if b % 3 != 0 and c % 3 != 0 :
	print(a)
	
	
