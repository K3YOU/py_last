'''
	[문제]
		a리스트에 랜덤(0 ~ 100) 사이의 랜덤 값을 4개 저장한 후 출력한다. 
		배열의 값은 학생들의 성적이다. 
		60점 이상이면 합격이다. 
  		전원합격 시 "상품" 을 출력. 
		전원탈락 시 "벌칙" 를 출력.
		그 외는 리스트만 출력하시오.
		
		[예시] 
			[67, 100, 98, 97] "상품"
			[53, 25, 12, 41] "벌칙"
'''
a = []


passcount =0
failcount =0

import random

for i in range(4):
	r = random.randint(0,100)
	a.append(r)  #67,100,25

	if a[i] >= 60 :
		passcount += 1 #1,2
		if passcount == 4 :
			print(a,"상품")
	else:
		failcount += 1 #1
		#passcount = 0 
		if failcount == 4:
			print(a,"벌칙")
print(a)

