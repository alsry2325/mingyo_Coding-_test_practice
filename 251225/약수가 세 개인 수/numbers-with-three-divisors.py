start, end = map(int, input().split())

# Please write your code here.
 

total = 0  # 3인 약수의 갯수
for i in range(start,end+1):  # 3에서 7까지 반복
    cnt = 0  #약수의 갯수들 
    for d in range(1,i+1):  #1부터 n까지
        if i % d == 0:  #n을 나누었을때  0으로 떨어지는 수만
            cnt+=1          #=1
    if cnt == 3:  #약수가 세개라면 
        total +=1  # 세개인 약수 하나씩 더함
print(total)
