#선택할 수 있는 idx는 1 ~ n-2
#idx를 순회하며 양쪽에 있는 수 중 작은 값을 더함

import sys
input = sys.stdin.readline

n = int(input())
lt = list(map(int,input().split()))
answer = max(lt)

for i in range(1,n-1):
    plus = lt[i] + min(lt[i-1],lt[i+1])
    answer = max(answer,plus)
print(answer)