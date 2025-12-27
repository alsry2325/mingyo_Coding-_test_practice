n = int(input())
cnt = 0

for i  in range(n):
    for j in range(n):
        if i % 2 == 0:    #짝수 줄일때는 1234
            print(j + 1,end="")  
        else:    #그렇지 않고 홀수줄일때는 
            print(n - j,end="") #전체에서 순으로 0,1,2,3 빼기 
    print()