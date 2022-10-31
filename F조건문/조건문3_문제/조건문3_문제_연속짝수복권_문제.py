'''
[문제]
	100~900 사이의 랜덤숫자를 출력한다. 
	세 자리의 숫자를 전부 한 자리씩 분리한다.		
	[규칙]
		[1] 세 자리 모두 짝수이면 "1등"을 출력한다.
		[2] 두 자리가 짝수이고, 짝수인 숫자가 연속이면 "2등"을 출력한다.
		[3] 그 외는 "꽝"을 출력한다.
		[4] 단, 0은 짝수이다.
		[예]
			462 ==> 4,6,2 세 자리 모두 짝수이므로 ==> 1등
			245 ==> 2,4,5 두 자리가 짝수이고 2, 4연속이므로 ==> 2등
			456 ==> 4,5,6 두 자리가 짝수이지만 연속이 아니므로 ==> 꽝
			782 ==> 7,8,2 두 자리가 짝수이고 8, 2연속이므로 ==> 2등 	
'''


import random

a = random.randint(100,900)

b = a // 100
c = a  % 100 // 10
d = a % 10 

print("step 1", a, b,c,d)

# 내가 푼 방식
'''
#1
if b % 2 == 0 and  c % 2 == 0 and  d % 2 == 0:
	print("1")

#2
if b % 2 == 0 and  c % 2 == 0 and  d % 2 != 0:
	print("2")
if b % 2 != 0 and  c % 2 == 0 and  d % 2 == 0:
	print("2")

#lot

if b % 2 != 0 and  c % 2 != 0 and  d % 2 != 0:
	print("lot")

if b % 2 == 0 and  c % 2 != 0 and  d % 2 == 0:
	print("lot")	

'''

#선생님풀이

#먼저 결과값을 먼저 선언한다.
result = 0

#result = 1 or result =2으로 버전을 나눈다.

if (a % 2 == 0 and b % 2 == 0 and c % 2 == 0):
	result = 1 #result = 1 버전

if (a % 2 == 0 and b % 2 == 0 ) or  (b % 2 == 0 and c % 2 == 0):
	result = 2

if result == 0:
	print("lot")
		
if result == 1:
	print("1")

if result == 2:
	print("2")			
