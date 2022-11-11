'''
[문제]
	철수는 오징어게임에 참가하였다.
	첫 번째 게임은 "무궁화꽃이 피었습니다" 이다.
	규칙은 아래와 같다.	
	[규칙]	
		[1] 전체 거리는 0 ~ 25까지 거리가 있다.
		[2] 철수는 현재 0의 자리에 있다.
		[3] 철수는 매 턴 1 ~ 4의 랜덤숫자를 뽑는다. 숫자만큼 이동한다. 
		[4]	이동 거리를 누적하며, 합이 25 이상이 되면 승리이며 종료한다.
		[5] 인형은 매턴 3 ~ 5의 랜덤숫자를 뽑는다. 
		[6] 인형보다 큰 숫자가 나오면 움직인 것으로 간주되어 패배하며 종료한다.
		[7] 10턴 안에 도착 못 하면 시간초과로 패배하며 종료한다.
		[8] 철수의 이동 경로를 전부 출력하시오.
'''

import random
#전체거리는 25까지
chul = 0
doll = 0
count = 0

run = 1
while run == 1:
	r = random.randint(1,4)
	r1 = random.randint(3,5)
	print("random number :",r,"(chulsoo)",r1,"(doll)")

	count += 1
	if  chul < 25 and 10  == count :
		print("time over:lose")
		run = 0

	chul += r
	doll += r1
	print("이동경로: ", chul,doll)
	

	if r > r1 :
		print("chulsoo lose : bigger num")
		run = 0

	
	if chul >= 25 :
		print("chulsoo wins")
		run = 0

	
