'''
	[문제]
		철수의 위치는 y = 0 , x = 0 이다.
		랜덤 숫자(1~4) 를 5번 뽑는다. 
		랜덤 숫자는 방향을 뜻한다. 
		1은 북쪽 2는 동쪽 3은 남쪽 4는 서쪽을 뜻한다.
  
		방향만큼 1씩 이동하며, 
		5번 이동 후 철수의 위치를 출력하시오.
  
		[예시] 랜덤으로 1 4 3 2 1 이 나왔다고 했을 때
		1은 북이므로 y += 1
		4는 서이므로 x -= 1
		3은 남이므로 y -= 1
		2는 동이므로 x += 1
		1은 북이므로 y += 1
'''
import random

x = 0 #east and west
y = 0 # north and south
#sum_x = 0 # sum for x
#sum_y = 0 #sum for y

i = 5 #chance for random 
run = 1
sum_x= 0
sum_y = 0
while run == 1 :
	if i == 0 :
		run = 0
	else: #5 #4
		
		r = random.randint(1,4)
		print("r :",r,end= " ") #2 #1
		if r == 1:
			print("north")#north
			y = 1	
		if r == 2:
			print("east") #east
			x =1	
		if r == 3:
			print("south")
			y = -1	
		if r == 4:
			print("west")	
			x = -1	
		
		sum_x += x 
		sum_y += y
	i -= 1 #4 #3
print("x :",x,"y :",y)
print("sum_x :",sum_x,"sum_y :",sum_y)

