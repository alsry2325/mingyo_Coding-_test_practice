n, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
# print(n,k)
# print(nums)
nums_result  = sorted(nums)
print(nums_result[k-1])
     
