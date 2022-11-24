'''
	[문제]
		다음은 학생 번화와 점수의 한 세트이다.
		일등의 번호와 점수, 꼴등의 번호와 점수를 출력하시오.
	[정답]
		일등 = 1004 98
		꼴등 = 1002 11
'''


numberList = [1001, 1002, 1003, 1004, 1005]
scoreList = [87, 11, 45, 98, 23]
 

minscore = 100
minindex = 0

maxscore = 0
maxindexm =0


for i in range(len(numberList)):
	if scoreList[i] <minscore :
		minscore =scoreList[i]
		#scoreList[i]의 점수가 numberlist[i]의 학생번호로 이어져야 한다
		minindex = i	
	if scoreList[i] > maxscore :
		maxscore = scoreList[i]
		maxindex = i
print("꼴등",numberList[minindex],minscore)
print("일등",numberList[maxindex],maxscore)











