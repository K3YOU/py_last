'''
	[문제]
		a리스트는 철수 반 중간고사 점수이다. 
		각 학생들이 다른 학생들과 비교하여 자기보다 크거나 같은 점수를 출력하시오.
	[예시]
		10 보다 큰 점수는 54, 90, 20 이다.
		54 보다 큰 점수는 90 이다.
		90 보다 큰 점수는 없다.
		20 보다 큰 점수는 54, 90 이다. 
'''
a = [10, 54, 90, 20]

for i in range(len(a)):
	c = 0
	for j in range(len(a)):
		if i != j and a[i] <= a[j]: # 본인 인덱스는 제외해야 한다.
		
			print(a[i],"보다 큰 점수는" ,a[j], "이다" )
		else: #i == j or a[i] > a[j]   90이 90을 만났을 때 -> 아이인덱스랑 제이인덱스랑 결국 같은 거
			c += 1
			#print(a[i],c)
	if c == len(a):
		print(a[i],"보다 큰 값은 없다")
