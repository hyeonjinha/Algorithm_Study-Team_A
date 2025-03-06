# 앞에 존재하는 사람이 걸린 시간이 중복하여서 계산됨
# 시간에 따른 오름차순으로 정렬하여 더하면 해결할 것으로 보임
import sys

input = sys.stdin.readline

num = int(input())
lt = list(map(int,input().split()))

sort_lt = sorted(lt,key = lambda x : x)

time_list = [0 for i in range(num)]
for i in range(num):
    if i == 0:
        time_list[i] = sort_lt[i]
    else:
        time_list[i] = time_list[i-1] + sort_lt[i]
#메모리제이션을 이용하여 한 사람당 걸린 시간을 계산
print(sum(time_list))
