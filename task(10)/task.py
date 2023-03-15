s = input()
n = len(s)
d = {}
for i, c in enumerate(s):
    d[c] = d.get(c, 0) + (n-i)*(i+1)
for k, v in sorted(d.items()):
    print(f'{k}: {v}')