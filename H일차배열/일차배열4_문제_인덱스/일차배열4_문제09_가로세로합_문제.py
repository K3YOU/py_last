'''
	[문제]	
		아래 a 리스트는 한 줄 리스트이지만 
		아래와 같이 사각형으로 놓였다고 했을 때,  
		[1] a 리스트의 가로 합은 garo 리스트에 저장하시오.
		[2] a 리스트의 세로 합은 sero 리스트에 저장하시오.
	[정답]
		garo = [10, 26, 42]
		sero = [15, 18, 21, 24]
'''	

a = [1, 2, 3, 4,
     5, 6, 7, 8,
     9, 10,11,12]

'''
a = ['1', 2, 3, 4, '5', 6, 7, 8, '9', 10,11,12]
가로 = 1~4/5~8/9~12 각각의 합
'''

garo = [0, 0, 0] #이미 값이 0으로 채워져있으니 값을 바꿔주기
sero = [0, 0, 0, 0]

#가로
count = 0
j = 1
sum =0
for i in range(len(a)):
	a[i] = j 
	sum += j 
	j += 1 
	count += 1 

	if count == 4 :
		print(sum,end= " ")
		sum = 0
		count = 0

print()
print()


'''
세로
세 개씩 끊어서
'''
# 세로인덱스: <0><1><2><3>
'''
a = [1, 2, 3, 4,
     5, 6, 7, 8,
     9, 10,11,12]
'''

seroIndex = 0
for i in range(len(a)):
	sero[seroIndex] += a[i] # sero[0] = a[0],sero[1]=a[1],sero[2]=a[2],sero[3]=a[3] ,sero[0]=a[0]+a[4]
	seroIndex += 1 # 1 , 2, 3,4
	if i % 4 == 3: # i = 3
		seroIndex = 0 # 0
print("sero =", sero)	


#세로인덱스에 맞춰서 그 값을 더하라
#세로인덱스를 조절하기
#세로인덱스가 무한으로 못 늘어나게 i 값으로 조절하기


