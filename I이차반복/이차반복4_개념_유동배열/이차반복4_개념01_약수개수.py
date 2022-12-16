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

a = [43,55,65,11]
count = []

for i in range(len(a)):
	val = 0
	for j in range(a[i]):   #a[i]인 이유 : 43의 약수의 개수를 구해야하므로
		if a[i] % (j+1) == 0 :  #J+1인 이유 : 43까지인데 j는 42까지라서 
			print(j+1,end= " ")
			val += 1
	count.append(val)        # 여기에 있어야하는 이유 : 43의 개수는 43의 턴이 끝나면 들어가야하니깐
	print()
print(count)



















# a = [43,55,65,11]
# count = []

# for i in range(len(a)):

# 	val = 0
# 	for j in range(a[i]):
# 		if a[i] % (j + 1) == 0:
# 			print(j + 1, end=" ")
# 			val += 1
# 	print()

# 	count.append(val)

# print("count",count)
