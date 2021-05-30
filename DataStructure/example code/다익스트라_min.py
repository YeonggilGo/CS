# 다익스트라 + 인접리스트
'''
서울(0), 천안(1), 원주(2), 논산(3), 대전(4),
대구(5), 강릉(6), 광주(7), 부산(8), 포항(9)
'''
'''
10 14
0 1 12
0 2 15
1 3 4
1 4 10
2 5 7
2 6 21
3 4 3
3 7 13
4 5 10
5 8 9
5 9 19
6 9 25
7 8 15
8 9 5
'''
'''
[0, 12, 15, 16, 19, 22, 36, 29, 31, 36]
'''
import heapq

def dijkstra(start):
    # 출발점 선택
    dist[start] = 0

    # 모든 도시 선택될 때까지
    for i in range(V):
        # 최소값 찾기
        min = INF
        u = -1
        for v in range(V):
            if not visited[v] and dist[v] < min:
                min = dist[i]
                u = i

        visited[u] = 1

        # 정점 u에 인접한 정점중에 방문 안 한 정점 가중치 업데이트
        for v in range(V):
            if adj[u][v] and not visited[v]:
                if dist[v] > dist[u] + adj[u][v] :
                    dist[v] = dist[u] + adj[u][v]

# 입력
V, E = map(int, input().split())    # 정점수, 간선수
adj = [[0] * V for i in range(V)]   # 인접행렬
INF = float('inf')
dist = [INF] * V                    # 가중치
visited = [0] * V                   # 방문처리

for i in range(E):
    s, e, d = map(int, input().split())
    adj[e][s] = adj[s][e] = d

dijkstra(0)
print(dist)







