'''
	[문제]
		a리스트에 랜덤(1~4) 숫자 4개를 저장한다. 
		단, 중복없는 숫자로 저장한다.
	
	[예시]
		[1,4,2,3]
'''
import random

a = []

count = 0



# 2/10  : 
## 피드백 : 시간이 오래걸렸지만 정확하게 풀었다~!, check = False 생각하는데까지 오래걸림

while (True) :

	r = random.randint(1,4)
	check = False

	for j in range(len(a)):
		
		if (r == a[j]):
			check = True
			break

	if check == False:
		a.append(r)
		count += 1
		if count == 4:
			break
print(a)		
























# while True:    #여기에 i가 들어가면 4개를 다 못 채워서 다온다.
	
# 	r = random.randint(1,4)
# 	j = 0
	
# 	check = False

# 	for j in range(len(a)):
# 		if ( a[j]== r):
# 			check = True
# 			break
# 	if check == False : #거짓이면 배열에 추가해줘야한다.
# 		a.append(r)
# 		count += 1
# 	if count == 4:
# 		break
	
# print(a)




## 내가 푼 방법들

# 	a.append(r)     ##거짓이면 넣어줘야한다,
# 	count += 1
# 	check = False 

# 	j = 0
# 	while j < i :
# 		if (a[i] == a[j]):
# 			check = True
# 			break
# 	if check == False :
# 		if count == 4:
# 			break

# 	i += 1
# print(a)



############################################################################################



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



# count = 0
# while True:
# 	r = random.randint(1,4)
# 	check = False
# 	for i in range(len(a)):
# 		if a[i] == r:
# 			check = True
# 			break
# 	if check == False:
# 		a.append(r)
# 		count += 1
# 	if count == 4:
# 		break
# print(a)

