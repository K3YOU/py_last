'''
		
	[문제] 
		numberList 는 학생들의 번호를 저장한 리스트이다.
		scoreList 는 학생들의 점수를 저장한 리스트이다.
 		랜덤으로 한 학생의 학번과 점수를 출력
   
	[예시1] 
		1001 , 87
  
	[예시2]
		1004 , 97
'''

numberList = [ 1001, 1002, 1003, 1004, 1005 ]
scoreList =  [ 87, 11, 45, 98, 23 ]

import random
r = random.randint(0,len(numberList)-1)

index = r
print(numberList[index],scoreList[index])