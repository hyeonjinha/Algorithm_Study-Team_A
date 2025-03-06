# 자신의 키 : index
# 자신 보다 키가 큰 사람의 수 : list의 값
# 리스트에서 가장 작은 키를 가진 사람부터 배치?
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
lt = list(map(int,input().split()))
answer = [-1 for _ in range(n)]
#키가 작은 순서부터 배치
for h in range(1,n+1):
    cnt = 0
    for i in range(n):
        if answer[i] == -1: # 이미 키가 작은 경우에는 cnt가 증가하지 않음
            if lt[h-1] == cnt:
                answer[i] = h
                break
            cnt +=1
        
print(*answer)


