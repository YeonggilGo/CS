"""
데이크스트라 알고리즘은 어떤 변도 음수 가중치를 갖지 않는 유향 그래프에서 주어진 출발점과 도착점 사이의 최단 경로 문제를 푸는 알고리즘이다.
방향이 있는 그래프에서 꼭지점들을 연결하는 비용이 할당 되었을 때 임의의 꼭지점에서 다른 꼭지점으로 가는 경로들 중에서 비용이 가장 적게 드는 경로, 즉 두 정점 사이의 최단 경로를 찾아라.
입력 값 첫번째 라인에는 전체 테스트 케이스의 개수가 입력된다.
두번째 라인에는 정점의 개수, 그리고 시작 정점, 도착 정점이 입력된다. 이때, 정점의 최대 개수는 100이다.
세번째 라인에는 정점을 잇는 간선 개수(m)가 입력된다.
네번째 라인부터는 연결 된 정점 값 2개와 간선에 할당 된 비용이 m번 들어온다. 이때 간선 방향은 첫번째 입력된 정점에서 두번째 입력된 정점으로 가는 방향이다.
"""

N = 100
INF = 100000
MAP = [[0] * (N + 1) for _ in range(N + 1)]
visit = [False] * (N + 1)
dist = [0] * (N + 1)


def dijkstra():
    global dist, visit, MAP
    v = 0
    dist[start] = 0

    for i in range(1, vertex + 1):
        min = INF
        for j in range(1, vertex + 1):
            if visit[j] == False and min > dist[j]:
                min = dist[j]
                v = j

        visit[v] = True

        for j in range(1, vertex + 1):
            if dist[j] > dist[v] + MAP[v][j]:
                dist[j] = dist[v] + MAP[v][j]


def main():
    global MAP, dist, visit, vertex, start

    T = int(input())

    for test_case in range(1, T + 1):
        vertex, start, end = map(int, input().split())
        edge = int(input())

        for i in range(1, vertex + 1):
            for j in range(1, vertex + 1):
                if i != j:
                    MAP[i][j] = INF

        for i in range(1, edge + 1):
            FROM, TO, value = map(int, input().split())
            MAP[FROM][TO] = value

        for i in range(1, vertex + 1):
            dist[i] = INF
            visit[i] = False

        dijkstra()
        print("#%d %d" % (test_case, dist[end]))


if __name__ == "__main__":
    main()