'''
	[문제] 
		a리스트 안에 1 또는 7을 랜덤으로 7개 추가후 출력하시오. 
		단, 7의 개수는 3개만 추가하고, 1의 개수는 4개만 추가한다.
		위에서 만든복권을 판정한다. 
  		7이 연속으로 3개면 "당첨"을 출력한다.
		아니면 "꽝" 을 출력한다.
		
	[예]
		[ 1, 7, 7, 1, 1, 7, 1]  "꽝"
		[ 1, 1, 1, 7, 7, 7, 1]  "당첨"
'''
import random

a= []

count1 = 0
count7 = 0

#배열안에 요소를 집어 넣는다.
for i in range (1000):
	if count1 + count7 == 7 :
		break
	
	r = random.randint(1,2)

	if r == 1 and count1 <= 3:
		a.append(1)
		count1 += 1
		#count7 = 0
	if r == 2 and count7 <= 4:
		a.append(7)
		count7 += 1
		
print(a)

#넣어진 요소들을 하나씩 7이 연속인지 아닌지 검증한다.
count = 0 
check = False

for i in range(len(a)) :
	if a[i] == 7 :
		count += 1
		
		if count == 3:
			check =True
	else :
		count = 0

#count = 3이면 당첨 아님 실패
if count == 3:
	print("당첨")
else:
	print("실패")
