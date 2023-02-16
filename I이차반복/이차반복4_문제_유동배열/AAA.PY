

import random


r = random.randint(1, 10)
"""
7
67
567
4567
34567
234567
1234567


"""
for i in range(7):
    num = 7 -i
    for j in range(i+1):
        print(num,end=" ")
        num += 1
    print()

a = [1,44,54,3]

print()

"""
1 44 54 3
44 54 3
54 3
3

"""
for i in range(len(a)): # 0~ len(a) -1 --> 1 ~ len(a)
   
    for j in range(len(a) -i) :
        print(a[j+i],end= " ")
        
    print()
    