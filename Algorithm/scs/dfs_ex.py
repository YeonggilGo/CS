def depthFirstSearch(v, depth):
    global maxEdge

    if v == end:
        if maxEdge < 0 or depth < maxEdge:
            maxEdge = depth
        return

    visit[v] = True

    for i in range(1, vertex + 1):
        if MAP[v][i] == 1 and visit[i] is False:
            depthFirstSearch(i, depth + 1)
            visit[i] = False


def main():
    global vertex, end, visit, MAP, maxEdge

    T = int(input())

    for test_case in range(1, T + 1):
        vertex, edge, start, end = map(int, input().split())
        MAP = [[0] * (vertex + 1) for _ in range(vertex + 1)]
        visit = [False] * (vertex + 1)
        for _ in range(edge):
            v1, v2 = map(int, input().split())
            MAP[v1][v2] = 1
        maxEdge = -1
        depthFirstSearch(start, 0)
        print("#%d %d" % (test_case, maxEdge))


if __name__ == "__main__":
    main()