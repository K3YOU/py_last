'''
  [문제]
    0~4 사이의 랜덤 숫자를 저장해 a리스트에서 그 위치의 값이
    최대값인지 검사한다.
    만약 최대값이면 그 위치의 값을 0으로 바꾸고,
    전부 0이되면 종료한다. 

    과정을 전부 출력하시오.
  [예]
      랜덤 : 3
      [11, 87, 42, 0, 24]

      랜덤 : 0
      [11, 87, 42, 0, 24]   <- 최대값이 아니므로 그대로 유지

      랜덤 : 1
      [11, 0, 42, 100, 24]

      ...
      
  '''
import random

a = [11, 87, 42, 100, 24]

#2/16











#2/13


#   #랜덤숫자뽑기
count = 0
while True :
  r = random.randint(0,4)
  print("random num :", r)

  max = 0
  maxindex = 0

#   #랜덤값이 최대값이면 그 자리를 0으로 바꾸기
#   ##최대 값을 먼저 찾기
  for i in range(len(a)):
    if(max < a[i]) : #0으로 지정된 최대값과 최대인덱스를 특정 수들로 바꿔줘야함
      max = a[i]
      maxindex = i   #최대인덱스가 특정값일 경우, 그 값이 r일 경우 


#   ##0으로 바꿔주기   <-- 내가 헷갈리는 부분 : r은 배열 안의 숫자가 아닌 인덱스 넘버라서

  if maxindex == r:
    a[r]  = 0
    count += 1

  print(a)
  print() 

  if count == len(a):
    break



#   #랜덤숫자뽑기
# count = 0
# while (True):
#   r = random.randint(0,4)
#   print(r)

#   max = 0
#   maxindex = 0

#   #랜덤값이 최대값이면 그 자리를 0으로 바꾸기
#   ##최대 값을 먼저 찾기
#   for i in range(len(a)):
#     if max<a[i] :
#       max = a[i]
#       maxindex = i


#   ##0으로 바꿔주기

#   if r == maxindex :
#     a[r] = 0
#     count += 1

    
#   print(a)
#   print()

#   if count == len(a):
#     break



