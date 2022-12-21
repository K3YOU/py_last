'''
	[문제]
		a리스트에서 혼자있는 숫자만 출력하시오.
	[정답]
		20 50
'''

a = [10,20,30,40,40,10,30,10,50]

#while로 푼 버전

i = 0
while i < len(a):
	
	j = 0  #j = i이면 뒤에 놓인 10같은 경우는 앞에는 검사 안 하니깐 결국 혼자있는 수로 취급받게 된다.
	check = False
	while j < len(a):
		##중복찾기
		if i != j and a[i]== a[j]:   #서로 다른 자리의 숫만 가능하고 '내 자신은 안된다'는 의미
			check = True
			break
		j += 1
	if check == False :
		print(a[i],end= " ")

	i += 1 