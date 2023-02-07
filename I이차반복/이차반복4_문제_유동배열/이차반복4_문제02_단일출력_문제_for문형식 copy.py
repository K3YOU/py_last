'''
	[문제]
		a리스트의 숫자를 하나씩 출력한다.
		단, 이미 출력이 되어 중복되는 숫자는 출력하지 마시오.
	[정답]
		1 2 3 4 100		                                                               ===> "답지.최종정리"
'''
a = [1,1,2,2,3,3,4,100,3]

for i in range(len(a)):
	check = False
	for j in range(i) :
		print("i",a[i],end= " ")

		print("j",a[j])
		if (a[i]== a[j]) :
			check = True
			break

	if check == False :
		print("a[i]", a[i]) 
		print()
	