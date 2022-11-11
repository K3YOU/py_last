철수위치 = 50

count = 0
turn = True
while 철수위치 > 0:

    # 왼발
    철수위치 = 철수위치 - 2 ## 48
    if turn == True:
        print("(좌)",철수위치, end=" ")
        count += 1 ## 1

        if count % 5 == 0: ##48은 아니니깐 뛰어넘고
            print()
            count = 0
            turn = not turn
            print("turn : ",turn) #true -> flase
    # 오른발
    철수위치 = 철수위치 - 2 ##48-2=46
    if turn == False: ##46 : turn is still true so that skip
        print("(우)",철수위치, end=" ")
        count += 1 ##2

        if count % 5 == 0: #여기 있어야 오-46 이더라도 바뀌지 않는다
            print()
            count = 0
            turn = not turn
            print("turn :",turn)