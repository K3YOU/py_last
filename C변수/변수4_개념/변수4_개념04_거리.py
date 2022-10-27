'''
	[ 거리문제 ]		
		[1] 철수는 자전거를 타고 2시간에 65040 미터를 간다. 
			1시간에는 몇미터를 가는가?
			1시간 =65040/2
			30분에는 몇미터를 가는가?
			30분 = 1시간/2
			10분에는 몇미터를 가는가?
			10분 = 30분/3
			1분에는 몇미터를 가는가?
			1분 = 10분 / 10
			1초에는 몇미터를 가는가? 
			1초 = 1분 / 60
			17초에는 몇미터를 가는가?
			17초 = 1초 * 17

			2시간(2 x 3600초) : 65040미터 = 1초 : n미터
			7200초 : 65040미터 = 1초 : n미터
			7200 x n = 65040 x 1
			7200n = 65040
			7200n / 7200 = 65040 / 7200
			n = 9.03333...

		[2]
			철수는 자전거를 타고 65040미터를 가는데 2시간이걸린다. 			
			철수는 10000미터를 몇초에 가는가?
			철수는 1000 미터를 몇초에 가는가?
			철수는 1미터를 몇초에 가는가?

			65040미터 : 7200초 = 10000미터 : n초
			65040 x n = 7200 x 10000
			65040n = 7200 x 10000
			n = 7200 x 10000 / 65040
'''
'''
	65040 : 2*60*60 = 10000 : n
	2*60* 60 * 10000 = 65040 * n
	n = 2*60*60* 10000/65040
'''

'''
print("[문제1]")
print("2시간 : ", 65040)
print("1시간 : ", 65040 / 2)
print("30분 : " , 65040 / 2 / 2)
print("10분 : " , 65040 / 2 / 2 / 3)
print("1분 : " , 65040 / 2 / 2 / 3 / 10)
print("1초 : " , round(65040 / 2 / 2 / 3 / 10 / 60 , 2))
print("17초 : " , round(65040 / 2 / 2 / 3 / 10 / 60 * 17 , 2))

print("[문제2]")
print("10000미터 : " , round(7200 * 10000 / 65040 , 2)) # 초로 바꿔준다.
print("1000미터 : " , round(7200 * 1000 / 65040 , 2))
print("1미터 : " , round(7200 * 1 / 65040 * 1 , 2))


'''
'''
한시간 = 65040 /2
삼십분 = 한시간 /2
십분 = 삼십분/3
일분 = 십분/10
일초 = 일분/60
십칠초 = 일초 * 17

print(한시간,삼십분,십분,일분,round(일초,2),round(십칠초,2))
'''

