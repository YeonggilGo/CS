'''
7 11
0 5 60
0 1 32
0 2 31
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x: return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1

def mst():
    cnt = 0     #간선갯수
    total = 0   #가중치의 합

    for i in range(E):                  # MST 구성을 위해 V개의 간선을 선택
        p1 = find_set(edge[i][0])       #두 노드의 대표원소 알아내기
        p2 = find_set(edge[i][1])
        if p1 != p2:                    # 사이클이 생성되지 않으면
            total += edge[i][2]         # MST에 포함되므로 가중치 추가
            cnt += 1                    # 간선 개수 증가
            union(p1, p2)
        if cnt == V-1  : break          # V-1 의 간선 선택
    return total                        # MST 완성 후 가중치 합 반환

V, E = map(int, input().split())
edge = [list(map(int, input().split())) for i in range(E)]  #시작, 끝, 가중치
edge.sort(key=lambda x : x[2])              # 간선을 가중치 기준으로 정렬
p = [0] * V
rank = [0] * V
for i in range(V):
    make_set(i)

print(mst())
