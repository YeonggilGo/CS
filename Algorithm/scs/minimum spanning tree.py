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