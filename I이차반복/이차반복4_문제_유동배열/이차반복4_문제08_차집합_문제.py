'''
	[문제]
		a와 b 두 리스트를 비교해서 서로 겹치지 않는 값을 
		temp에 저장하고 출력하시오.
	[정답]
		temp = [6, 4, 20, 3, 17, 13, 7]
'''
a = [16,  5, 11, 6, 19, 12, 18,  4, 20, 3]
b = [17, 11, 19, 5, 13, 18, 16, 12, 11, 7]
temp = []

##먼저 a의 다른 값만 넣는다 (check사용)
for i in range(10):
	
	check =False
	for j in range(10):
	#같으면
		if a[i] == b[j] :
	#사실이다
			check = True 
	#멈추기
			break
	#틀리면
	if check ==False :
	#추가한다
		#a[i] != b[j]
		temp.append(a[i])
		#temp.append(b[i])
print(temp)

for i in range(10):
	
	check =False
	for j in range(10):
	#같으면
		if a[j] == b[i] :  #차이점 : 첫 반복은 이젠 b로 한다
	#사실이다
			check = True 
	#멈추기
			break
	#틀리면
	if check ==False :
	#추가한다
		#a[i] != b[j]
		temp.append(b[i])
		#temp.append(b[i])
print(temp)



#서로 수가 같으면 0으로 만들고 0이 아니면 temp에 수를 넣는 방식 -> 11이 b에 두 번 나오고 a랑 중복이라서 이렇게 풀면 틀림
# for i in range (len(a)):
# 	for j in range(len(b)):
# 		if a[i] == b[j] :
# 			a[i] = 0
# 			b[j] = 0
# print(a,b)

# for x in range(len(a)):
# 	if a[x] != 0 :
# 		temp.append(a[x])
# 	if b[x] != 0 :
# 		temp.append(b[x])
# print(temp)

