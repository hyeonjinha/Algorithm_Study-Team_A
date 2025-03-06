import sys
input = sys.stdin.readline

def fi(n,lt):
    if lt[n] != [-1,-1]:
        return lt[n]
    
    fi0 = fi(n-1,lt)
    fi1 = fi(n-2,lt)
    lt[n] = [fi0[0] + fi1[0],fi0[1]+fi1[1]]
    
    return lt[n]

num = int(input())
for _ in range(num):
    tem = int(input())
    lt = [[-1,-1] for _ in range(tem+2)]
    lt[0] = [1,0]
    lt[1] = [0,1]
    result = fi(tem,lt)
    print(result[0],result[1])
    
    

