'''
	[문제] 
		numberList 는 학생들의 번호를 저장한 리스트이다.
		scoreList 는 학생들의 점수를 저장한 리스트이다.
 		실수로 학생들의 점수가 한 칸씩 밀렸다. 
		학생들의 점수를 한 칸씩 앞으로 당기고 
		맨 앞의 점수는 맨 뒤에 저장하시오.
	
	[정답]	
		[ 1001, 1002, 1003, 1004, 1005 ]
		[ 11, 45, 98, 23, 87 ]
'''

numberList = [1001, 1002, 1003, 1004, 1005]
scoreList =  [87, 11, 45, 98, 23]  #한 칸씩 앞으로 당겨라 #맨 앞의 점수는 제일 뒤로

temp = scoreList[0]
for i in range(len(scoreList) -1):
	scoreList[i] = scoreList[i+1]
print(scoreList)

scoreList[len(scoreList) - 1] = temp
print(scoreList)


	
temp = scoreList[0] #맨 앞 점수는 맨 뒤로 보내야하므로 이 값을 임시적으로 저장한다.
for i in range(len(scoreList) - 1): #-1을 해주는 이유 : 맨 앞 점수는 이미 임시적으로 저장해두었고 나중에 추가적으로 넣을 것이므로 순환에서 하나를 뺀다.
	scoreList[i] = scoreList[i + 1] #1번 값은 2번 값이 된다. 
print(scoreList)

scoreList[len(scoreList) - 1] = temp #마지막 배열에는 맨 앞 점수가 들어간다.
print(scoreList)



 