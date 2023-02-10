'''
	[문제]
		a리스트의 각 값의 약수를 전부 출력하고 
		각 약수의 개수를 count리스트에 추가하시오.

	[예시]
		1 43 
		1 5 11 55 
		1 5 13 65 
		1 11 		
		count = [2, 4, 4, 2]
	
	[정답]
		count = [2, 4, 4, 2]
'''
# 푸는 법
# i 반복에서는 a리스트의 값을 하나씩 꺼내고 (약수의 개수를 세는 변수가 필요할 것)
# j 반복에서는 꺼낸 값을 길이로 정하고 그 중 약수를 찾아가기 


a = [43,55,65,11]

count = []


# 2/10
for i in range(len(a)):
	val = 0
	for j in range(a[i]) : #a[i]인 이유 => 약수가 몇개인지 나열하는 곳이므로 총 길이는 a[i]여야 한다
		if(a[i]%(j+1)== 0):
			val += 1
		#count.append(val) : 여기 있으면 위에서 더해질때마다 출력되는 것임	
	count.append(val) #여기 있어야하는 이유 : list a의 i번째 요소의 약수의 개수이므로 i번째일때만 해당 약수의 개수를 더해줘야한다.
print(count)
				












# for i in range(len(a)):
# 	val = 0
# 	for j in range(a[i]):   #a[i]인 이유 : 43의 약수의 개수를 구해야하므로
# 		if a[i] % (j+1) == 0 :  #J+1인 이유 : 43까지인데 j는 42까지라서 
# 			print(j+1,end= " ")
# 			val += 1
# 	count.append(val)        # 여기에 있어야하는 이유 : 43의 개수는 43의 턴이 끝나면 들어가야하니깐
# 	print()
# print(count)


















