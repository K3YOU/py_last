'''
    [문제]
        랜덤숫자(1~100)를 각각 다섯개씩 a 와 b에 저장하고,
        a 와 b 의 각 자리의 합을 total에 추가하시오.
'''
import random
a = []
b = []
total = [] #각 자리의 합을 나타내는 변수도 빈 리스트로 저장한다.
print("a : " , a)
print("b : " , b)

for i in range(5):    #각각 다섯개씩
    a.append(random.randint(1, 100)) #빈리스트인 a,b에 추가해야하므로 append함수를 사용한다 #랜덤이므로 랜덤함수를 괄호 안에 넣는다  
    b.append(random.randint(1, 100))
print(a , " " , b)

for i in range(len(a)):
    c = a[i] + b[i] #각각의 배열들마다 저장해야 하므로 새로운 변수를 선언해야한다.
    total.append(c) #total함수도 빈 리스트이므로 리스트에 추가하는 함수인 append를 써야한다.

print("total : " , total)

