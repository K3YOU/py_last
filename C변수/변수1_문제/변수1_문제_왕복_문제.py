'''
	[문제]
		 철수는 운동을 위해 집에서 직진으로 1800m를 걸어간 후, 
		 집으로 돌아가기 위해 뒤돌아서 300m를 걸어갔다. 
		 철수는 힘들어서 잠시 쉬었다.
		 철수는 다시 일어나서 집으로 200m를  걸어갔을 때쯤,
		 아까 쉬었던 자리에 가방을 두고 온 것을 깨달았다.
		 철수는 다시 돌아가서 가방을 가지고 집으로 돌아왔다.
		 오늘 철수가 걸은 길이는 총 몇m 인지 구하시오.
		 
	[정답] 
		4000
'''

거리1= 1800
거리2 = 300
거리3= 200

총거리= 거리1+거리2+거리3 + 거리3+(거리1-거리2)

print(총거리)