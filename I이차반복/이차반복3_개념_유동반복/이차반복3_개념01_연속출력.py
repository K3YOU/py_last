'''
	[문제] 
		1~10 사이의 랜덤 숫자를 다섯 번 반복해서 저장하고, 
		랜덤 숫자 개수만큼 출력하시오.
	
 	[예시]
		예를 들어 4, 5, 3, 1, 2 가 나왔다고 한다면,
  
		4444
		55555
		333
		1
		22
'''

import random

a = []

# 2/ 14  : 큰 어려움없이 풀었다
for i in range(5) :
	r = random.randint(1,10)
	for j in range(r):
		print(r,end= " ")
	print()





















# for i in range(5):
# 	r = random.randint(1,10)
# 	a.append(r)
# print(a) #[4, 6, 3, 10, 2]

# for i in range(5):  #a배열에서 돌아간다,
# 	for j in range(a[i]) : # j는 a[i]만큼 돌아간다.
# 		print(a[i],end=" ")
# 	print()




