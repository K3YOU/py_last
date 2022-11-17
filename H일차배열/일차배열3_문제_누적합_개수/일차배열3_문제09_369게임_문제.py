'''
    [문제]
        [1] 1~50까지 반복한다.
        [2] 3이나 6이나 9가 없는 수 중 짝수만 a리스트에 추가하시오.
    [정답]
        a = [2, 4, 8, 10, 12, 14, 18, 20, 22, 24, 28, 40, 42, 44, 48, 50]
'''

a = []


for i in range (50) :
    i += 1   #이거는 특수한 경우! 위의 for문의 i에서 알아서 꺼내온 뒤 그 다음에 더한다는 뜻

    # i => 1, 50
    #십의 자리에 3,6,9가 있는 경우
    ten = i // 10
    #일의 자리에 3,6,9가 있는 경우    
    one = i % 10

    if i % 2 == 0 :
        if ten != 3 and ten != 6 and ten != 9 and one != 3 and one !=6 and one != 9 :  #다 and로 묶어야함
            a.append(i)
    
print(a)

#둘의 차이점은 무엇인가?
a= []
for i in range (50) :
    # i => 0, 49
    #십의 자리에 3,6,9가 있는 경우
    ten = i // 10
    #일의 자리에 3,6,9가 있는 경우    
    one = i % 10

    if i % 2 == 0 :
        if ten != 3 and ten != 6 and ten != 9 and one != 3 and one !=6 and one != 9 :  #다 and로 묶어야함
            a.append(i)
    
    i += 1  #동작안함, 이미 for문 안에서 다 알아서 돌아가기 때문에
print(a)


#for랑 while의 차이점
##for는 개수가 이미 정확하게 지정되어 있는 경우, for i in range 에서 i는 알아서 돌아감. ()안에 숫자만 하나 크게 적어주면 된다.
##while은 개수가 변동이 될 때 i +=1 이런식으로 적어줘야 돌아감
