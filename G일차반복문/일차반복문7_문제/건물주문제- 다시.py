"""
[문제]
	1씩증가하는 무한반복을  하다가 4 가 안들어가는 숫자를 만날때 카운트 + 1
	그카운트가 50이되면 종료 

"""
run = 1
i = 1 #무한증가
count = 0
num = 50

while run == 1 :
	x = i // 10
	y = i % 10

	if x != 4 and y != 4:
		print(i, end = " ")
		count += 1
		print(count)
		if count == 50 :
			run = 0
	i += 1

