#A는 재배열하되 B는 재배열 불가
#S는 A와B에 index에 해당하는 값을 곱한 값
#즉, S가 최솟값이 되기 위해선 A의 배열에서 가장 큰 값은 B에서 가장 작은 값으로 설정되어야 함

import sys

input = sys.stdin.readline

n = int(input())
lt_A = list(map(int,input().split()))
lt_B = list(map(int,input().split()))

sort_A = sorted(lt_A,key = lambda x : x,reverse = True)
sort_B = sorted(lt_B,key = lambda x : x)

answer = 0

for i in range(n):
    answer += sort_A[i] * sort_B[i]
    
print(answer)

#tem = [[0,0] for _ in range(n)]
#for i in range(n):
#    tem[i][0] = sort_A[i]
#    tem[i][1] = sort_B[i]
