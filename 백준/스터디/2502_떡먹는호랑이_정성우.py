dp = [0] * 31

dp[1] = 1

for i in range(2, 31):
    dp[i] = dp[i - 1] + dp[i - 2]

d, k = map(int, input().split())

cof_a = dp[d - 2]
cof_b = dp[d - 1]

flag = False
for a in range(1, 50000):
    for b in range(a, 100000):
        check = cof_a * a + cof_b * b
        if check == k:
            A, B = a, b
            flag = True
            break

        if check > k:
            break
    if flag:
        break

print(A)
print(B)
