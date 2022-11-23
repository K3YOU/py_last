'''
	[문제] 
		a리스트 안에 1 또는 7을 랜덤으로 7개 추가 후 출력하시오. 
		단, 7의 개수는 3개만 추가하고, 
		1의 개수는 4개만 추가한다.
		
	[예]
		정답 [ 1, 7, 7, 1, 1, 7, 1]  # 개수가 맞다. 
		오답 [ 7, 1, 1, 7, 1, 1, 1]  # 7이 두개이다.
			
'''
import random

a = []

count1 = 0 #1의 개수를 세기
count7 = 0 #7의 개수를 세기

while True:
	if count1 + count7 == 7: #1이랑 7의 개수가 합쳐서 7개여야 하므로  # count1과 count7의 범위롤 각자 정하지 않아도 된다.
		break #멈춰!! ->여기서 밖의 프린트로

	r = random.randint(0, 1) 

	if r == 0 and count7 <= 3: #7의 개수를 3개까지만 추가하니깐, r ==0 이면 7이라는거 굳이 안 써줘도 된다.
		a.append(7)
		count7 += 1  # count7이 4가 된다면 더 이상 안 올라가고
	elif r == 1 and count1 <= 4: #count1만 올라감
		a.append(1)
		count1 += 1
print(a)


    
