'''
	[문제]
		chul와 min는 가위바위보를 6회 하였다. 
		가위(0) , 바위(1) , 보(2) 를 뜻한다. 
		아래 배열은 각각 가위바위보를 낸 기록을 저장한 것이다. 
		
		chul와 min는 계단 50번째부터 게임을 시작하였다. 
		min는 게임을 모두 끝마치고 어디 있는지 구하시오.
		[규칙]
			이기면 5칸 올라간다.
			비기면 1칸 올라간다.
			지면 3칸 내려간다. 
	[정답]
		48
'''

chul = [0,1,2,2,1,0]
min = [2,1,1,2,0,1]

chul_loca = 50
min_loca = 50

for i in range (len(chul)) :
	if chul[i] == min[i] :
		chul_loca += 1
		min_loca += 1
		print("tie")
	#chul win
	elif chul[i] == 0 and min[i] == 2:
		chul_loca += 5
		min_loca -= 3
		print("chulsoo wins")

	elif chul[i] == 1 and min[i] == 0 :		
		chul_loca += 5
		min_loca -= 3
		print("chulsoo wins")

	elif chul[i] == 2 and min[i] == 1 :		
		chul_loca += 5
		min_loca -= 3
		print("chulsoo wins")

	
	else :
		chul_loca -= 3
		min_loca += 5
		print("minsoo wins")
i += 1


print("minsoo",min_loca)
