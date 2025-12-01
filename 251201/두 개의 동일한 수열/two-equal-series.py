n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

A.sort()
B.sort()

# new_B = ''.join(B) 조인함수는 스트링타입만 들어갈수있다 인트형은 애러 따라서 
#int(''.join(map(str, int_list))) 숫자형으로 비교하고싶다면 인트형으로 감싸면된다
new_A =''.join(map(str, A))
new_B =''.join(map(str, B))
# print(new_B)
if new_A == new_B:
    print("Yes")
else:
    print("No")
