'''
	[문제]
		a리스트의 숫자를 하나씩 출력한다.
		단, 이미 출력이 되어 중복되는 숫자는 출력하지 마시오.
	[정답]
		1 2 3 4 100		                                                               ===> "답지.최종정리"
'''
a = [1,1,2,2,3,3,4,100,3]

#앞에만 검사해서 중복이 있으면 나오게 하는거.

for i in range(len(a)):
	check = False
	for j in range(i):# 1 , 2, 3 => 0 , 01 , 012
		if (  a[i] == a[j]):  # 다른 인덱스 넘버지만 같은 수일 때를 표현한 것
			check = True
			break

	if check == False :
		print(a[i],end = " ")
#for를 쓰더라도 check를 쓰는게 중요하다