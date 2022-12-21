'''
	[문제]
		[1] a리스트에 1~10까지의 랜덤 숫자 3개를 저장 후 출력하시오.
		[2] 단, 숫자 3개는 서로 중복되면 안 된다. 
		[3] 숫자 3개의 합은 반드시 20이어야 한다. 
	[예시]
		[3, 10, 7] o 
		[5, 10, 5] x 
'''
import random

a = [0,0,0]   

while(True):   #여기가 제일 중요한 부분 : 합이 20이 아니면 처음부터 다시한다
	i = 0
	sum = 0

	while i <3:
		
		
		r = random.randint(1,10)
		
		check = False
		for j in range(i):
			#같으면
			if a[j] == r:
			#사실이다
				check = True
			#브레이크
				break
			#거짓이면
		if check == False:
			#다르다 (추가한다)
			a[i] = r
			
			sum += a[i]
			print(sum)
			i += 1

	if sum == 20:
		break

print(a)
		 
