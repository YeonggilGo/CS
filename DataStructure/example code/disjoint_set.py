def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x: return x
    else: return find_set(p[x])

def union(x, y):
    # x의 대표자, y의 대표자를 찾음
    p[find_set(y)] = find_set(x)

N = 6
p = [0] * (N+1)
for i in range(1, N+1):
    make_set(i)

# print(p)
union(1, 3)
union(2, 3)
union(5, 6)
print(p)
print(find_set(6))