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

while True: # total까지 해서 20이 아니면 처음부터 다시!
	i = 0
	while i < 3:
		r = random.randint(1, 10)
		print("r:",r)
		check = False
		j = 0
		while j < i:
			if r == a[j]:
				check = True
				break
			j += 1

		if check == False:
			a[i] = r
			i += 1

	total = 0
	for i in range(3):
		total += a[i]
		print("total:",total)

	if total == 20:
		break

print(a)
