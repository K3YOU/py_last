'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
	[예시]
		1 2 3 4 5 6 7
		2 3 4 5 6 7
		3 4 5 6 7
		4 5 6 7
		5 6 7
		6 7
		7
'''

# 2/ 15

#필요한것 
# i :  가로 (ex. i = 7일 때)
# j : 숫자를 출력할 것 (ex. j 에서 1부터 7까지 출력한다)

for i in range(7): #i : 0 ~ 6  --> 실제 : 1~ 7
	num = i +1
	for j in range(7-i):
		print(num,end=" ")
		num += 1
	print()     #여기있는 이유 : j의 for문이 끝나고 줄을 띄어야 함
		