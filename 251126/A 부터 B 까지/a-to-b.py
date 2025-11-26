A,B = map(int,input().split())
while True:
    # A와 B가 들어오면서 A에는 2 가 담기고
    print(A,end=" ")
    if A %2 == 1:      # 2가 홀수일때 곱하고
        A *= 2
    elif A %2 == 0:  # 2가 짝수일때 3을 더해라 
        A += 3

    if A > B:
        break
    
    