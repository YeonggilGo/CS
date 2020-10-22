"""
위상 정렬(topological sorting)은 유향 그래프의 정점(vertex)을 간선의 방향을 거스르지 않도록 나열하는 것을 의미한다.

위와 같은 그래프에서 숫자가 있는 원은 정점(Vertex)라고 하고, 정점과 정점을 잇는 연결선을 간선(Edge)이라고 한다. N(<=25)개의 정점과 M(<=25)개의 간선이 주어졌을 때, 도착점 D 까지의 위상정렬을 구하시오.

Input	Output
3 // 테스트 개수
8 7 // 정점의 수, 간선의 수
1 // 목적지
2 1 // 2번 정점에서 1번 정점으로의 간선
3 1
4 2
6 3
8 3
5 4
7 5
5 6
1
3 1
2 1
3 2
4 2
4 3
5 4
7 7
1
2 1
4 1
6 2
3 2
2 4
5 4
7 5
#1 7 5 4 2 8 6 3 1
#2 5 4 3 2 1
#3 7 5 6 3 2 4 1

"""

def minKey(key, mstSet):
    min = 2147483647
    for v in range(0, V):
        if (mstSet[v] == 0) and (key[v] < min):
            min = key[v]
            min_index = v
    return min_index


def printMST(parent):
    weightSum = 0
    for i in range(1, V):
        weightSum += graph[i][parent[i]]
    print(weightSum)


def primMST():
    parent = [0] * 100
    key = [2147483647] * 100
    mstSet = [0] * 100
    key[0] = 0
    parent[0] = -1
    for count in range(0, V - 1):
        u = minKey(key, mstSet)
        mstSet[u] = 1
        for v in range(0, V):
            if graph[u][v] and (mstSet[v] == 0) and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]
    printMST(parent)


def main():
    global graph, V
    T, V = map(int, input().split())
    for test_case in range(1, T + 1):
        graph = [[int(x) for x in input().split()] for y in range(V)]
        print("#%d" % test_case, end=' ')
        primMST()


if __name__ == "__main__":
    main()