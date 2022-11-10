'''
[문제]
	랜덤으로 1 또는 7을 10번 출력한다. 
	7이 연속으로 3번 이상이면 "당첨" 아니면 "꽝"을 출력하시오.
[예시]
	1 1 1 7 7 7 1 1 7 7 
	당첨

	7 1 1 1 1 7 1 1 7 1 
	꽝
'''
#있어야 할 변수 : 출력할 동안 돌아가는 변수, 카운트세는 변수, 당첨/꽝 나타내는 변수


##내 풀이
import random

count = 0 

result = False

i = 0 
while i < 10 :
	r = random.randint(1,2)

	if r == 2 :
		r = 7
		#print(r, end = " ") #여기서 프린트 쓰면 안되는 이유 : 계속 7만 나옴! 다른 숫자도 나올 수 있게 프린트를 if문이랑 같이 써줘야한다. 	
		count += 1 #카운트는 7의 개수를 세는 것이므로 들여써도 된다.
	print(r, end= " ") 
	
	if r == 1 :
		count = 0 #연속해서 7이 나와야하므로 카운트
	
	if count >= 3:    
		result = True

	i += 1

if result == True:
	print("당첨")
if result == False :
	print("꽝")



#선생님 풀이
import random

count = 0 #중복을 세는 카운트를 넣기

result = False #꽝이면 false/ 당첨이면 true

# 1 1 1 7 7 7 1 1 7 7 
i = 0   #열번 반복할 변수를 정한다.
while i < 10: #10번 출력
	r = random.randint(1, 2)
	if r == 2: #2이면 7로 나오기
		r = 7
	print(r, end=" ") #출력하기

	if r == 7: #위에서 2->7로 바꿈
		count += 1 #중복카운트 시작
	if r != 7:
		count = 0
	
	if count >= 3:
		result = True

	i += 1

if result == True:
	print("당첨")
if result == False:
	print("꽝")
