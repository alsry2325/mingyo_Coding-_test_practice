arr = [
    list(map(int, input().split()))
    for _ in range(4)     #4줄이라 네번 입력 한걸 배열에 넣기
]

for i in range(4):  # 4줄이라 4번 실행
    ans = 0   # 그줄마다 합친 값을 구해야 해서  선언
    for j in range(4):   # 그줄에 갯수 선언
        ans += arr[i][j]  # 한줄 값이 들어올때마다  값을 더하기
    print(ans)  #결과 실행