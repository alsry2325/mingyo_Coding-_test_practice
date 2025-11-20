num1 = int(input())

num2 = list(map(int, input().split()))


for i in range(num1):
    print(num2[i]**2 ,end=' ')