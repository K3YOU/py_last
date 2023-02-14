'''
	[문제]
		2~100 사이의 랜덤 숫자 하나를 저장하고, 
		2부터 그 숫자 사이의 모든 소수를 출력하시오.

	[예시]
		r = 20
	 	소수 = 2, 3, 5, 7, 11, 13, 17, 19	
'''
'''
1. for문은 안된다.
=> 
'''
import random

#2/14
r = random.randint(2,100)
print("r =",r)

for i in range(r):
	



























# r = random.randint(2, 100)
# r = 19
# print("r =", r)


# ################## for문 #######################

# for z in range (r-1):
# 	i = 2+z #소수로 나올 수

# 	count = 0  #count == 2 소수로 출력된ㄱ
# 	share = 1 #몫
# 	while share <= i:
# 		if i % share == 0 :
# 			count += 1
# 		share += 1

# 	if count == 2:
# 		print(i,end= " ")
# 	#i += 1  : z로 커진다
# 	#if i ==r : i 항상 2
	




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