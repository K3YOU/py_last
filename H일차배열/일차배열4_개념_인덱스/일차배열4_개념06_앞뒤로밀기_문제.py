'''
	[문제1]
		a리스트의 값들을 한 칸씩 앞으로 당기고 출력하시오.
	[정답1]
		a = [10,20,30,40,50,0]
		
  
	[문제2]
		b리스트의 값들을 한 칸씩 뒤로 밀고 출력하시오.
	[정답2]
		b =  [0,10,20,30,40,50]
'''

# [문제1]
a = [0, 10, 20, 30, 40, 50]
print(a)

for i in range(len(a)-1): #len(a)=6 #= for i in range(5)
	a[i]=a[i+1] #a[0]=a[1]~a[4]=a[5] 까지임/ a[5]=a[6] 절대 이렇게 안 나감 range안의 그 수는 미포함이니깐
	#print(i,a[i]) 
#print()
a[len(a)-1]=0	#a[5]
#print(len(a)-1,a[len(a)-1])
print(a)
	
#마지막 값을 밖으로 빼서 따로 지정해두기	

print()

# [문제2]
b =  [10, 20, 30, 40, 50, 0]
b1 =  [0,10,20,30,40,50]
print("b",b)
print("b1",b1)

index = len(b)-1
for i in range(len(b)):

	# 그냥 다섯번 반복한 것 돌아간게 아님 식에 i가 있어야 돌아감 => b[len(b)-1] = b[len(b)-1-1]
	b[index]= b[index-1]
	index -= 1
b[0]= 0

print(b)	



