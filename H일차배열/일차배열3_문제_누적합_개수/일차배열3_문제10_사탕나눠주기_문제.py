'''
	[문제]
		아래 candy 리스트는 각 병에 들어있는 사탕의 양이다. 
		한 사람당 한 병에서 25개씩 나눠주려 한다. 
		나눠줄 수 있는 사람 수를 count 배열에 저장하시오.
		나눠주고 남은 사탕은 remainder 배열에 순차적으로 저장하시오.
	[정답]
		candy	 	[80, 53, 36, 22]  각 병에 들어있는 사탕의 양
		count		[3, 2, 1, 0]  나눠줄 수 있는 사람의 수
		remainder 	[5, 3, 11, 22] 나눠주고 남은 사탕
'''

candy = [80,53,36,22]
count = []
remainder = []

i = 0 #for의 i랑 다른 i
c=0
r=0
#candy[i] // 25 = 3 = count[i]
#candy[i] % 25 = 5 = remainder[i]

for i in range(len(candy)) : #여기에서 i는 0부터 시작하니깐 candy라는 배열의 요소 수보다 하나 작게 돌아감 = 결국에는 요수의 수는 다 맞음
	c = candy[i] // 25 
	r = candy[i] % 25
	count.append(c)
	remainder.append(r)


print("candy",candy)
print("count",count)
print("remainder",remainder)
	




