
# 리스트 컴프리헨션을 이용하여 2차원 리스트 
row = 3
cols = 3

matrix1 = [
    list(map(int,input().split()))
    for _ in range(row)
]
input()
matrix2 = [
     list(map(int,input().split()))
    for _ in range(row)
]
# for _ in range(row):
#     row_list = list(map(int,input().split()))
#     matrix1.append(row_list)
# input()
# for _ in range(row):
#     row_list = list(map(int,input().split()))
#     matrix2.append(row_list)

for i in range(row):
    for j in range(cols):
        results = matrix1[i][j] * matrix2[i][j]
        print(results,end=" ")
    print()

