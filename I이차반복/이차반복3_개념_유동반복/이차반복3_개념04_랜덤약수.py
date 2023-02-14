'''
    [문제]
        10~100 사이의 랜덤 숫자를 다섯 개 저장한다. 
        각 숫자의 약수를 전부 출력한다. 
    
    [예시]    
        52 : 1 2 4 13 26 52 
        81 : 1 3 9 27 81 
        28 : 1 2 4 7 14 28
        11 : 1 11
        52 : 1 2 4 13 26 52
'''
import random


#2/14
#랜덤 숫자 5섯 개 저장한다
total=[]
for i in range(5):
    r = random.randint(10,100)
    total.append(r)
print(total,end= " ")
print()

#약수 출력
for i in range(len(total)):
    share = 1
    for j in range(total[i]):
        if total[i] % share == 0 :
            print(share,end= " ")
        # print()
        share += 1
        if share == total :
            break
    print()


















# a=[67, 70, 39, 73, 77]
# # for i in range(5):
# #     r = random.randint(10,100)
# #     a.append(r)
# print(a) #[67, 70, 39, 73, 77]

# for i in range(len(a)): #a를 진행한다
#     share = 1  #share를 여기에 두는게 중요하다
    
#     for j in range(a[i]) : #a[i]까지 진행한다
#         if a[i] % share == 0 :
#             print(a[i],":", share,end= " ")
#             print()

#         share += 1
#         if share == a[i]:
#             break
#     print()



# for i in range(5):
#     r = random.randint(10, 100)
#     print(r, end=" : ")

#     for j in range(r):
#         if r % (j + 1) == 0:
#             print(j + 1, end=" ")
#     print()
