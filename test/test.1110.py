"""
    [문제] 9와 0 이 없는 세상 

        숫자 1부터 1씩 증가하며 순서대로 20번 출력한다. 
        단 9와 0이 없다. 
    [예시]
        1 2 3 4 5 6 7 8 11 12 13 14 15 16 17 18 21 22 23 24
"""
print("--[문제1]--")

i = 1

while i <= 24 :

    십 = i // 10
    일 = i % 10 

    if 십 != 9 and 일 != 0 and 일 != 9 :
        print(i,end= " ")
    i += 1

print()
print("===============================")    
'''
count = 0
run = 1
i = 1
while run ==1:
    ten = i//10
    one = i % 10
    if i <= 20:
        if  one != 0 and one != 9 :
            count += 1
            print(count, end = " ")

        
    
    


    if count == 20:
        run = 0
            

    i += 1
'''

i = 1
c = 0
while c < 20:
    ten = i // 10  #몫
    one = i % 10   #나머지
    if i < 10: #1,2,3,4,,,,
        if one != 0 and one != 9:
            print(i , end=" ")
            c += 1
    if i >= 10: #11,12,13,14,
        if ten != 0 '''ten == 0 이면 십의 자리 수가 없는 경우라서 당연히 써줘야함''' and ten != 9 '''i는 무한히 커지므로 90대의 숫자는 제외한다'''and one != 0 '''10,20,30,,, 제외 이유''' and one != 9: '''일의 자리 9인 숫자들 제외''' 
            print(i , end=" ")
            c += 1
    i += 1