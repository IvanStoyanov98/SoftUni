n, m = [int(x) for x in input().split()]
n_set = set()
m_set = set()

for x in range(n + m):
    new_num = int(input())
    if x < n:
        n_set.add(new_num)
    else:
        m_set.add(new_num)

print(*n_set.intersection(m_set), sep="\n")
