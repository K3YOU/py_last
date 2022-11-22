'''
	[문제]
		공간이 10개인 a리스트가 있다. 
		랜덤(0~9)로 시작 인덱스를 저장한다.
		랜덤(1~10)로 개수를 저장한다.
		시작 인덱스부터 개수만큼 거꾸로 숫자를 채워나간다.
		채우는 숫자는 1부터 1씩 증가한다.
		
	[예시]
		ranIndex = 3 
		ranCount = 7		
  		a = [4,3,2,1,0,0,0,7,6,5]  
  			- 인덱스 3부터 7개를 채운다. 
	

'''
import random

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

ranindex = random.randint(0, 9)
print("ranindex =", ranindex)

rancount = random.randint(1, 10)
print("rancount =", rancount)

value = 1
for i in range(rancount):  #0이 들어가있으니깐 안 넣는다 그래서 범위를 rancount로 함
    a[ranindex] = value
    ranindex -= 1
    value += 1 

    if ranindex < 0:
        ranindex = len(a) - 1
print(a)