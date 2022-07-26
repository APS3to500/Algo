s = input()
t = input()

while len(t) - len(s) > 0:
    if t[-1] == 'A':
        t = t[:len(t) - 1]
    else:
        t = t[:len(t) - 1][::-1]

if s == t:
    print(1)
else:
    print(0)
