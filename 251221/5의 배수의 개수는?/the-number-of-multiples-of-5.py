# arr = [
#     list(map(int, input().split()))
#     for _ in range(4)     #4줄이라 네번 입력 한걸 배열에 넣기
# ]

# print(arr)

arr = []
count= 0
for _ in range(4):
    n = list(map(int, input().split()))
    arr.append(n)
for i in arr:
    for num in i:
        if num % 5 == 0:
            count+=1
print(count)
