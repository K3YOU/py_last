'''
	[문제]
		3~6 사이의 랜덤 숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙으로 출력하시오.
		단, 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시]
		r = 6
	[출력]
		3 2 1    #0+3 0+2 0+1
		6 5 4    #1+5 1+4 1+3
		9 8 7    #2 +7 2+6 2+5
		12 11 10
		15 14 13
		18 17 16
'''


import random

r= random.randint(3,6)
print(r)

for i in range(r):
	a = i +j 
	for j in range(3):
		j = 3
		print(j-a,end= " " )
		j -= 1
	print()


