'''
    [문제]
        a리스트에는 이미 1~3의 값이 저장되어 있다.
        이제 추가로 랜덤(1~10)을 10번 추가하려 한다.  (걍 10번 돌림, 중복이라도 그냥 넘어감)
        단, 중복숫자가 있으면 저장하지 않는다.
    [예시]
        [1, 2, 3, 10, 8, 9, 4]
'''
import random

a = [1,2,3]


i = 0
while i <10 :
   

    r = random.randint(1,10)

    check = False

    
    for j in range (len(a))  :
        if  a[j] == r:  #a[j]랑 같은게 아니라 r이랑 같아야함
            check =True
            break
     
    if check == False :
        a.append(r)

    i += 1

print(a)

