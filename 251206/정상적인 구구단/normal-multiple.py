n = int(input())

for i in range(1,n+1) :
    for j in range(1,n+1):
        if j < n:
            print(f"{i} * {j} = {i*j}",end =", ")  #j가 n보다 작을때는 ,콘마를 붙여라 
        else:
            print(f"{i} * {j} = {i*j}",end ="")
    print()
