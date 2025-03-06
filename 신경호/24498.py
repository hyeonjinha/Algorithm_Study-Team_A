#선택할 수 있는 idx는 1 ~ n-2
#왼쪽에서 부터 시작하여 0을 만들면서 진행
#오른쪽이 0이되면 max값

import sys
input = sys.stdin.readline

n = int(input())
lt = list(map(int,input().split()))
answer = max(lt)

for i in range(1,n-1):
    plus = lt[i] + min(lt[i-1],lt[i+1])
    answer = max(answer,plus)
print(answer)