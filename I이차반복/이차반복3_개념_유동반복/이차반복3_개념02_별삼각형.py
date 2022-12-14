'''
	[문제]
		아래와 같이 삼각형을 그려보시오.  	
   
	[예시]
		*
		**
		***
		****	
'''
for i in range(4): #vertical
	for j in range(i+1): #i=0에서 시작을 하므로 +1해주기
		print("*",end= "")
	print()







# for i in range(4):
# 	for j in range(i + 1):
# 		print("*", end="")
# 	print()