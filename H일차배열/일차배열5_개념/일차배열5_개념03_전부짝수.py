'''
	[문제]
		a리스트에 랜덤(0~9) 사이의 랜덤 값을 4개 저장한 후 출력한다. 
		리스트 안의 값들이 모두 짝수면 True를 출력하고,
		하나라도 짝수가 아니면 False를 출력한다.
		단, 0은 짝수이다.
		[예시] 
			[4, 6, 2, 0] True
			[5, 2, 0, 4] False
'''

import random

a = []
#4개를 랜덤으로 뽑아서 저장
for i in range(4):
	r = random.randint(0, 9)
	a.append(r)
print(a)
    
count = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
    	count += 1
		
if count == len(a): #모두 짝수여야 하므로
    print(True)
else:
    print(False)
