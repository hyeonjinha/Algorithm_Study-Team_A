import sys

input = sys.stdin.readline

num = int(input())

m = num // 5
cnt = 10000
for i in range(m,-1,-1):
    now = num - 5*i
    if now % 3 != 0:
        continue
    now_3 = now // 3
    total = i + now_3
    if total <= cnt:
        cnt = total
if cnt == 10000:
    print(-1)
else:    
    print(cnt)
    
    