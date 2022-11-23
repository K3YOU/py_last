'''
   [문제]
      a 리스트에 있는 값들을 b에 저장하려고 한다. 
      a 리스트의 값을 뒤에서부터 두 개씩 저장하시오.
   [정답]
      b = [7,7,3,3,1,1]
'''


a = [1 ,3, 7]
b = [0, 0, 0, 0, 0, 0]

aindex = 0 #인덱스는 0부터 시작하는거니깐
bindex = len(b) -1
for i in range(len(a)):
   b[bindex] = a[aindex]
   b[bindex - 1] = a[aindex]
   bindex -= 2 #중복을 방지
   aindex += 1 #0,1,2
print(b)  




   





