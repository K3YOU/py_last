'''
	[문제]
		a리스트에 랜덤(1~4) 숫자 4개를 저장한다. 
		단, 중복없는 숫자로 저장한다.
	
	[예시]
		[1,4,2,3]
'''
import random

a = []
# count = 0

# while True :
# 	r= random.randint(1,4)
# 	#print(r,end= " ")
# 	check = False    #틀린거를 출력해라

# 	for j in range(len(a)):
# 		if a[j] == r :   #같으면 
# 			check = True   # 맞다.
# 			break          #맞으면 빠져나와
# 	if check == False :  #틀리면
# 						#다르다
# 		a.append(r) #출력을 해야하니깐 다르면, 하나 넣고
# 		count += 1
# 	if count == 4:
# 		break
# print(a)



count = 0
while True:
	r = random.randint(1,4)
	check = False
	for i in range(len(a)):
		if a[i] == r:
			check = True
			break
	if check == False:
		a.append(r)
		count += 1
	if count == 4:
		break
print(a)

