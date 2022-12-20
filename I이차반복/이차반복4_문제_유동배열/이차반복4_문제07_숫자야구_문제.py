'''
	[문제]		
		[1] com리스트에 0~9사이의 랜덤 숫자 3개를 저장하되 중복 값이 없어야 한다.
		[2] me리스트에 0~9사이의 랜덤 숫자 3개를 저장하되 중복 값이 없어야 한다.
		[3] com과 me 를 비교해서 숫자가 같고 자리도 같으면 strike + 1  
		[4] com과 me 를 비교해서 숫자가 같고 자리가 틀리면 ball + 1
		[5] 사용자에게 strike와 ball 개수를 출력해 보여준다.
		
		계속 반복하면서 strike가 3이 되면 종료한다.
'''




import random
com = [1, 2, 4]
me = [0, 0 ,9]


comindex = 0
#make me list

a = [1]

for i in range(7):
	a[i]
	# a[0]a[1]a[2]a[3]a[4]a[5]


while True:
	check = False
	r = random.randint(0,5)
	

	for j in range(comindex):
		if r== com[j]:
			check = True
	if check==False :
		com[comindex] = r
		comindex += 1
			
	if comindex == 3:
		break

print("com",com)

while(True) :
	index = 0
	me = [0, 0 ,0]

	#make me list
	for i in range(100):
		
		check = False
		r = random.randint(0,5)

		for j in range(len(me)):
			if r== me[j]:
				check = True
		if check==False :
			me[index] = r
			index += 1
				
		if index == 3:
			break

	print("me",me)

	#strike and ball counts
	strike = 0
	ball = 0
	for i in range (len(com)):
		for j in range(len(com)):
			if i == j and com[i] == me[j] :
				strike += 1
			if i != j and com[i] == me[j] :
				ball += 1
	print(strike, ball)

	if strike == 3:
		break





			





















'''
// 빈 배열인 경우 count로 할 수 있다.

	for(i=0;i<4;){
		var r = parseInt(Math.random()*4)+1 
		var count = 0 
		arr[i] = r // 넣고
		for(j=0;j<i;j++){ //i까지 돌리기
			if(arr[j] != r){
			count ++ // 아니면 늘어나기
			}
			
		}
		if(count == i){
			i++
		}
	}
	console.log("arr", arr)



'''