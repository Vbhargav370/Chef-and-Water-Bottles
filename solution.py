t = int(input())
for _ in range(t):
    n,x,k = map(int, input().split())
    maximum = k//x
    if maximum >= n:
        print(n)
    else:
        print(maximum)
    
    
