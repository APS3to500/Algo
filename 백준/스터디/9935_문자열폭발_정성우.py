s = input()
bomb = list(input())

l = len(s)
n = len(bomb)

stack = []

for i in s:
    stack.append(i)
    while len(stack) >= n and stack[-n:] == bomb:
        for _ in range(n):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
