'''
	[문제]
		(1) 랜덤(1 ~ 9) 사이의 랜덤값을 4개를 저장 후 비교한다. 
		(2) 4개의 랜덤값이 모두 홀수이면 1을 total에 추가,
			하나라도 홀수가 아니면 2를 total에 추가한다.
		(3) (1~2)를 5번 반복한다. 

		[예시] 
			[3, 1, 5, 1] 모두홀수 => total = [1]
			[5, 2, 1, 4] 모두홀수x => total = [1,2]
			...
'''
import random
total = []


for j in range (5) :
	count = 0  #돌 때 마다 리셋    
	a = []
	for i in range(4):
		r = random.randint(1,9)
		a.append(r)
		if r % 2 != 0 :
			count +=1
			
		# else :
		# 	count = 0
	
	if count == 4:
		total.append(1)
	else :
		total.append(2)

	print(j,a)
print(total, end = " ")
