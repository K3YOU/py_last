'''
	[문제]
		a리스트의 숫자를 하나씩 출력한다.
		단, 이미 출력이 되어 중복되는 숫자는 출력하지 마시오.
	[정답]
		1 2 3 4 100		
'''
a = [1,1,2,2,3,3,4,100,3]


for i in range(len(a)):
	check = False          #이걸 여기써야 반복되면서 중복되는 숫자들만 뽑아냄. 위에 쓰면 1 하나만 나옴(하나만 뽑을 때는 위에 쓰면 될 듯..?)

	for j in range(i):
		print("i :",i)

		if a[i] == a[j] :   #같을 때
			check = True    #사실이다
			break			#(그러므로) 멈춰라 ->if 탈출
	if check == False:      #거짓일 때는
		print("a[i]",a[i])         #(다르므로) 프린트해라















