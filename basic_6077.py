import random

rand = random.randrange(1, 100)
print('random값: ', rand)

total = 0

# 1부터 rand값까지의 짝수합 구하기
# for문 버전
'''
for i in range(1, rand+1):
    if i%2 == 0:
        total += i
'''

# while문 버전
i = 1
while i < rand+1:
    if i%2 == 0:
        total += i
    i += 1  # i 증가식 추가하지 않으면 while문 빠져나오지 못함

print(total)

