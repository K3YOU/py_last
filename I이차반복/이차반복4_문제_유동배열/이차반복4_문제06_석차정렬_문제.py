'''
	[문제]
		석차를 출력하시오.
	[정답]
		2 3 4 1 
'''

numList = [1001, 1002, 1003, 1004]
scoreList = [87, 42,  11, 98]

for i in range(len(scoreList)):
	count = 0

	for j in range(len(scoreList)):

		if scoreList[j] >= scoreList[i] :   #i하나에 j여러개 돌아가면서 비교하기 -> 그럼 j가 더 클 경우가 있겠네
			count += 1
	print(count) #i의 등수 출력하기