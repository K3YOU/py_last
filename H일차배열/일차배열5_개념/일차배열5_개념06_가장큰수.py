'''
	[문제]
		a리시트에 -100~100 사이의 랜덤 값 중 홀수만 5개 저장한다. 
		그중 가장 큰 수와 가장 작은 수를 출력하시오. 
		[예시]
			[37, 53, 90, -82, -17]
			90
			-82
'''

import random

a = []

max = -100 #
min = 100 #최소값은 가진 수들 중에서 제일 큰 값으로, 값을 낮추기

for i in range(5):
	r = random.randint(-100, 100) # 37,53,90,-82,-17
	a.append(r) #37,53,90,-82, -17

	if max < a[i]: # -100<37, 37<53, 53<90
		max = a[i] #max = 37,53,90
	if min > a[i]: #100 > 37, 37>-82
		min = a[i] #min = 37,-82


print(a) #-17

print(max)
print(min)



