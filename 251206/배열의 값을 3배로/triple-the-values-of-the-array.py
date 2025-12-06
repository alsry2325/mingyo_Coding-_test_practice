row_data = [list(map(int,input().split())) for _ in range(3)]

row_datas = [
    [test * 3 for test in row]
    for row in row_data
]

for row in row_datas:
    print(*row)