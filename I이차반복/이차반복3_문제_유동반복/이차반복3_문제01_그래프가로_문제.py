'''
	[문제] 
		0~10 사이의 랜덤 숫자를 다섯 번 반복해서 저장하고
		그 랜덤 숫자만큼 * 을 출력하시오.
  
	[예]
		3   : ***
		10  : **********
		5   : *****
		6   : ******
		0   : 
		1   : *	
'''
#2/15 : 푸는 방법을 먼저 생각하고 접근하기

#1. 필요한 변수 생각
# r : range
# i : 랜덤 숫자들
# j : 별 



import random

# five random numbers 
for i in range( 5):
	r = random.randint(0,10)
	print("randome : ",r,":",end= " ")
	for j in range(r):
		print("*",end= " ")
	print()
		

		






























#2/14
# for i in range(5) :#until a
# 	r = random.randint(0,10)
	
# 	print(r,":",end=" ")

# 	for j in range(r) :
# 		print("&",end= " ")
# 	print()
