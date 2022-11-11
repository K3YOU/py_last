'''
	[문제]
		계단이 50 계단이 있다. 철수는 제일 위 계단에 서 있다. 
		철수는 한 번에 두 계단씩 내려간다. 
		철수가 왼발로 디딘 계단을 출력하시오.
		아래 조건을 참고하시오.
		[1] 철수는 한 번에 두 계단씩 내려간다.
		[2] 철수는 왼발부터 내려간다. #그 다음 발은 오른발이다! 
		[3] 5번 출력할 때마다 다른 발을 출력하시오.
		
		(좌) 48 (좌) 44 (좌) 40 (좌) 36 (좌) 32 
		(우) 30 (우) 26 (우) 22 (우) 18 (우) 14
		(좌) 12 (좌) 8 (좌) 4 (좌) 0
'''
#왼발로 2칸씩 4번 내려가는게 아니라 왼오왼오 이렇게 번갈아 가면서 두칸씩 내려가는게 내가 틀린 포인트

location = 50
turn = False 
count = 0

while location >= 0 :
	location = location -2 # 48 ## 44 = 46-2
	#left
	if turn == False : #48-false-left  ## 44-false-left
		print("left",location,end= " ") #print : 48 ## 44
		count += 1 #count : 1 ## 2
		if count == 5 :
			count = 0
			turn = not turn
	#right #출력이 못 되게 여기서 두개를 빼줘야한다! 
	location= location -2 # 46 # 42=44-2
	if turn == True : #but 46 is still in false not over 5 yet
		print("right",location,end= " ")
		count += 1
		if count == 5 :
			count = 0
			turn = not turn
		



