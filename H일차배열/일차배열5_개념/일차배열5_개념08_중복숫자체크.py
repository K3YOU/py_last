'''
   [문제]
      a리스트에 랜덤(1~4) 숫자 4개를 저장한다. 
      단, 중복없는 숫자로 저장한다.
   
   [예시]
      [1,4,2,3]
'''
import random

a = [0, 0, 0, 0]
check = [False, False, False, False] #랜덤을 방지하기위한 T/F 

count = 0
while True: #Flase라고 적으면 나중에는 [0,0,0,0]만 나옴 a의 원래 값들로 채워져서 굳이 할 필요 없음 BUT true라고 적어주고 빠져나올 수 있게 브레이크를 써줘야한다.
   r = random.randint(0, 3) #밑에서 +1을 해줘야 하므로 범위를 하나씩 작게 
   print("r",r,"a",a,check[r])
   
   #1,4,2,3

   if check[r] == False: #False인 것에만 들어가서
      a[count] = r + 1 #첫 count부터 r을 저장하는데 +1한 r의 값을 넣기
      check[r] = True # a중 한 배열이 채워졌으니 트루로 바꾸기 #True가 적히면 r이 같은 값이 나오면 이미 그 자리는 끝난다는 걸 의미
      count += 1 #카운트 값은 커지기

   if count == 4:
      break

print(a)


#요약
#중복을 방지하기위한 check라는 열을 따로 만들고 그 안에는 F로 채우기
#r 값의 범위를 하니씩 작게하고 실제 a안에 들어가는 값은 r+1
#한 번 값이 정해지면 True로 바꿔주기
