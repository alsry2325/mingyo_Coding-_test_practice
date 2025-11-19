A, B, C = map(int, input().split())


if (A >= B and B >= C) or (C >= B and B >= A):
    print(B)
elif (B >= A and A >= C) or (C >= A and A >= B):
    print(A)
else:
    print(C)