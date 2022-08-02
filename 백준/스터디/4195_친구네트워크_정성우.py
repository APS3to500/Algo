def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
        # 대표값끼리 카운트값을 연산한다.
        count[b] += count[a]
        return count[parent[b]]
    elif a < b:
        parent[b] = a
        count[a] += count[b]
        return count[parent[a]]
        # 대표값이 같으면 이미 친구 네트워크에 속하므로 연산을 하면 안됨
    else:
        return count[a]


for _ in range(int(input())):
    f = int(input())
    # count배열의 인덱스를 정해주기 위해 딕셔너리 사용 : 이름을 인덱스에 매칭
    name = dict()

    idx = 1  # 인덱스를 0부터하면 맨 처음 이름이 또 나올 시 아래 if문이 true처리 되므로 1부터 시작
    count = [1] * (f * 2 + 1)  # 가능한 인덱스의 수는 2*f+1이다.
    parent = [i for i in range(f * 2 + 1)]
    for _ in range(f):
        a, b = input().split()
        if not name.get(a):
            name[a] = idx
            idx += 1
        if not name.get(b):
            name[b] = idx
            idx += 1
        print(union(name[a], name[b]))
