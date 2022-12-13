'''
	[문제] 
		1~45사이의 랜덤값 6개를 lotto에 저장하려 한다.
		단, 중복되는 숫자는 없어야 하며,
		내림차순 정렬 후 출력하시오.
	[예시]
        [40, 38, 27, 26, 18, 5]
'''
lotto = []

import random

#중복없이 넣기
for i in range(6):
	check = False
	r = random.randint(1,45)
	lotto.append(r)
	
	for j in range(i):
		if(lotto[i]==lotto[j]):
			check == True
			break

#큰수부터 정렬하기
for i in range(len(lotto)):
	index = i
	max = lotto[i]
	for j in range(len(lotto)-i):
		if max< lotto[j+i]:
			
			
			max = lotto[j+i]
			index = j
	temp = lotto[index]
	lotto[index] = lotto[i]
	lotto[i] = temp

print(lotto)