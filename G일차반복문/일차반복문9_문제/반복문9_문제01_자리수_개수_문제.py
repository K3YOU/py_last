'''
[문제]
	10000~99999 사이의 랜덤숫자를 저장하고 
	자리별숫자가 5 이상인 개수를 출력하시오.
	
		예) 19200 ==> 9 하나만 5 이상 ==> 1
		예) 98436 ==> 9,8,6, 세 개가 5 이상 ==> 3
'''

import random

a = random.randint(10000,99999)
print("a :",a)

만 = a // 10000
천 = a % 10000 // 1000 
백 = a % 10000 % 1000 // 100
십 = a % 10000 % 1000 % 100 // 10
일 = a % 10

print(만,천,백,십,일, end = " ")

count = 0

run = 1
while run == 1:

	if 만 >= 5 :
		count += 1
	if 천 >= 5 :
		count += 1
	if 백 >= 5 :
		count += 1
	if 십 >= 5 :
		count += 1
	if 일 >= 5 :
		count += 1
	print()
	print("count :",count, )
	
	run = 0
    


# 계획
# 각 자리 별 숫자를 뽑아낸다
# 5이상인 개수를 세는 변수를 정한다 = count
# 