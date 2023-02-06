t = {}
for _ in range(int(input())):
    w = input().lower()

    s = tuple(sorted(w))
    if s not in t:
        t[s] = [w]
    elif w not in t[s]:
        t[s].append(w)

for val in t.values():
    if len(val) != 1:
        print(*val)
