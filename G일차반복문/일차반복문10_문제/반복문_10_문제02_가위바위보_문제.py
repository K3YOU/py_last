'''
	[문제]
		철수와 민수는 계단에서 가위바위보를 한다. 	 	
		철수와 민수는 각각 0 ~ 2 의 랜덤 값을 저장한다.
		0 : 가위 , 1 : 바위 , 2 : 보를 뜻한다.	 
		철수와 민수는 50번째 계단의 위치에서 시작한다.
		룰은 다음과 같다.	
		이기면 3칸 올라가기, 비기면 2칸 올라가기, 지면 1칸 내려가기.	 	
		둘 중 아무나 100 이상 도착하거나 
		둘 사이의 간격이 10 이상이면 게임은 종료된다. 
		게임이 종료될 때까지 두 사람의 이동 경로를 출력하시오.
'''
import random


chul_loca = 50
min_loca = 50
run =1
#철수랑 민수가 랜덤 값을 하나 뽑는다
while run == 1:
	print(chul_loca,min_loca)
	chul_r = random.randint(0,2)
	min_r = random.randint(0,2)
	print("random numbers : ", chul_r,min_r)

		## 철수와 민수의 값 차이를 비교한다
		#tie
	if chul_r == min_r :
			print("tie")
			chul_loca += 2
			min_loca += 2

	if chul_r == 0 and min_r == 2:
			print(chul_r,min_r)
			chul_r += 3
			min_r -=1

	if chul_r == 1 and min_r == 0 :
			print(chul_r,min_r)
			min_r -= 1
			chul_r +=3

	if chul_r == 2 and min_r == 1:
			print(chul_r,min_r)
			chul_r += 3
			min_r -=1

	if chul_r == 2 and min_r == 0:
			print(chul_r,min_r)
			chul_r -= 1
			min_r +=3

	if chul_r == 0 and min_r == 1 :
			print(chul_r,min_r)
			chul_r -= 1
			min_r +=3

	if chul_r == 1 and min_r == 2:
			print(chul_r,min_r)
			chul_r -= 1
			min_r +=3
		
	if chul_loca >= 100 :
			print("chulsoo wins")
			run = 0
	if min_loca >= 100 :
			print("minsoo wins")
			run = 0
	if abs(chul_loca- min_loca) >= 10 :
		if chul_loca > min_loca :
				print("chulsoo wins")
		else :
				print("minsoo wins")
				run = 0 		

###min_r 민수의 값을 누적한다
#### 100 이상 이거나 간격이 10 이상이면 게임을 종료한다

