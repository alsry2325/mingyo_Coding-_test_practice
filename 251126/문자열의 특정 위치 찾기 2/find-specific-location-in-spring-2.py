a = input()
string  = ["apple","banana","grape","blueberry","orange"]
cnt = 0
for i in range(5):
            #첫번째 loop a == apple[p] 또는 a == apple[l] 같으면 카운터 1
    if a == string[i][2] or a ==  string[i][3]:
        cnt += 1
        print(string[i])
print(cnt)