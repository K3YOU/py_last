'''
    [리스트 값 추가]
        append() 함수를 사용해서 리스트에 값을 추가할 수 있다. 
'''

a = [10,20,30,40]
print("a : " , a)

a.append(50) #제일 뒤에 값이 추가된다는 뜻이다
print("a : " , a)

a.append(80)
print("a : " , a)
print("-------------------------------")

'''
    [빈 리스트]
        b = [] 와 같이 리스트 선언 시 값을 미리 저장하지 않으면 빈 리스트를 만든다.
    
    [문제]
        아래 b 리스트에 랜덤숫자(1~10)를 다섯 개 저장 후 출력하시오.
'''
import random
b = []
print("b : " , b)
for i in range(5):
    r = random.randint(1, 10)
    b.append(r)
print("b : " , b)

c=[]
print("c :",c)
for i in range(5): #여기서 랜덤숫자를 몇 개 뽑아야하는지 알려준다! 
    r = random.randint(1,10)
    c.append(r)
print("c :", c)