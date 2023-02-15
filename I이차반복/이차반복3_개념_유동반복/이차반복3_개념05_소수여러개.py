'''
	[문제]
		2~100 사이의 랜덤 숫자 하나를 저장하고, 
		2부터 그 숫자 사이의 모든 소수를 출력하시오.

	[예시]
		r = 20
	 	소수 = 2, 3, 5, 7, 11, 13, 17, 19	
'''

import random

#2/14 : 어려워
#필요한게 뭔지 다시 생각하기 => 소수를 구하는 것이 제일 관건 : 소수는 나누기를 통해서 판명된다 => 나뉠 수, 몫이 필요
#랜덤 숫자는 변수가 아니라 범위를 지정해주는 수라고 생각할 것
#i는 소수가 될 수(나뉠 수) 
#j는 몫이 될 수    =>j의 for문이 i 안에 들어가야 함

r = random.randint(2,100)
print("r =",r)

for i in range(r+1): # 2  
	if i <=1:
		continue

	count = 0
	for j in range(i + 1):# 1부터
	
		if j <= 0: 
			continue
		else :
			if i % j == 0 :
				count += 1
			
	if count == 2:
		print(i ,end=" ")




# ################## for문 #######################

# r = 19
# print("r =", r)

# for z in range (r-1):
# 	i = 2+z #소수로 나올 수

# 	count = 0  #count == 2 소수로 출력된ㄱ
# 	 = 1 #몫
# 	while  <= i:
# 		if i %  == 0 :
# 			count += 1
# 		 += 1

# 	if count == 2:
# 		print(i,end= " ")
# 	#i += 1  : z로 커진다
# 	#if i ==r : i 항상 2
	



#정답
# i = 2  //소수가 될 수
# while i <= r:
# 	count = 0  // count = 2이면 소수입니당
# 	j = 1  // 몫
# 	while j <= i:
# 		if i % j == 0:
# 			count += 1
# 		j += 1

# 	if count == 2:
# 		print(i, end=" ")
# 	i += 1