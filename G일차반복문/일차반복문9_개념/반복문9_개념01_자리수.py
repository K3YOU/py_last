'''
[문제]
	1 ~ 2000 사이의 랜덤숫자를 저장하고, 
	자리수가 얼마인지 출력하시오.
[예시]
	969
	3자리 수
'''

'''
	969 // 10 = 96		1
	96 // 10 = 9		2
	9 // 10 = 0			3
'''
import random

num = random.randint(1, 2000)
print("num = ", num)

#temp = num #새로운변수로지정 #굳이안해줘도된다

count = 0 #자리수

run = 1
while run == 1:
	num = num // 10 #10으로 나누기고 몫만 가져가
	print("십으로 나누고 몫", num)
	count += 1 

	if num == 0: #더 이상 나눌 것이 없으면 끝난다
		run = 0
print("자리수", count)












