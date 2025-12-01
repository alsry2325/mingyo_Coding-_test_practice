n = int(input())
word = [input() for _ in range(n)]

# Please write your code here.

# print(word)
words = sorted(word)
words ='\n'.join(words)
print(words)