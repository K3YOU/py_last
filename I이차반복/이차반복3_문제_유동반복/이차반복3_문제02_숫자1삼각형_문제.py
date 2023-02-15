'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
	[예시]
		1
		1 2
		1 2 3
		1 2 3 4
		1 2 3 4 5	
'''

#2/15 : print()가 어디에 들어갈지 아는게 관건

#1.필요한 변수 생각
#i : 1~5
#j : 출력할 변수

#아래 세 개 중에 뭐가 정답인지 먼저 생각해보기

print("1번")
print()

for i in range(5): 
	for j in range(i+1):
		print(j+1,end= " ") 
	print()   

print()

print("2번")
print()

for i in range(5): 
	for j in range(i+1):
		print(j+1,end= " ") 
		print()   

print()

print("3번")
for i in range(5): 
	for j in range(i+1):
		print(j+1,end= " ")
print()
















# for i in range(5):
# 	count = 1
# 	for j in range(i+1):
# 		#print(i,j)
# 		print(count,end= " ")
# 		count +=1
# 	print()

# #####################################################################
# ######### 변수 안 쓰고 ###############
# for i in range(5):
# 	for j in range(i + 1):
# 		print(j + 1, end=" ")
# 	print()