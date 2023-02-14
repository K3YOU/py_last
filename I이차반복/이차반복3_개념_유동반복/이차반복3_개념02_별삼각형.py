'''
	[문제]
		아래와 같이 삼각형을 그려보시오.  	
   
	[예시]
		*
		**
		***
		****	
'''
# 2/14 : 별로 나타내는 과정에서 어려움을 겪음, 근데 이해함
for i in range(4):
	for j in range(i+1):
		print("*",end= " ")  
	print()



















# for i in range(4): #vertical
# 	for j in range(i+1): #i=0에서 시작을 하므로 +1해주기
# 		print("*",end= "")
# 	print()







# for i in range(4):
# 	for j in range(i + 1):
# 		print("*", end="")
# 	print()