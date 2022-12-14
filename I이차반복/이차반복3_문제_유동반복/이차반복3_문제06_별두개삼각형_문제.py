'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
  
	[예시]
		** 2
		**** 4
		****** 6
		******** 8
'''

for i in range(4) :
	for j in range (2*(i+1)):
		print("*",end= " ")
	print()