'''
	[문제]
		랜덤(2~10)의 숫자를 저장하고 
		랜덤 개수만큼 반복하면서 반복적으로 숫자를 저장한다.
		반복 숫자란? 1 2 3 1 2 3 1 2 3 을 반복해서 저장하는 것이다.
	[예1] 
		r = 8
		arr = [1,2,3,1,2,3,1,2]
  
	[예2] 
		r = 4
		arr = [1,2,3,1]
'''

arr = []

import random
r = random.randint(2,10)
print("r",r)


count = 0
i = 1
run = 1
while run == 1:
	if count < r :
		if i == 4:
			i = 1 
 
		arr.append(i)

		#print(arr,end= " ")
		i += 1

	if count == r:
		run = 0
	count += 1	
	
print("arr",arr)	

print("==============================")

arr1=[]
count1 = 1
print("r",r)

for i in range(r) :
	if count1 == 4:
		count1 = 1

	arr1.append(count1)
	count1 += 1
print(arr1)
	