'''
	[문제]
		학교에서 집까지 갈 때 시속 15km로 자전거를 타고 가면, 
		시속 6km로 걸어가는 것보다 18분 일찍 도착한다고 한다.
		학교에서 집까지의 거리를 구하시오.
	[정답]
		3
'''

자전거_분속 = 15 / 60.0
도보_분속 = 6 / 60.0

시간 = 0

run = 1
while run == 1:
	if 자전거_분속 * 시간 == 도보_분속 * (시간 + 18):
		print("시간",시간)
		거리 = 자전거_분속 * 시간
		print("거리",거리)
		run = 0
	#print("!!")
	시간 += 1

거리 = 자전거_분속 * 시간
print("거리", 거리)


#거리 숫자가 다르게 나오는 이유
'''
run = 0이라고 해서 끝인게 아니라 run = 0이 나오기 전의 숫자가 시간에 한 
'''



