'''
컴퓨터 시스템에 그래프는 연결되어 있는 객체간의 관계를 표현할 수 있는 자료구조다.
방향성이 없는 그래프의 V개의 정점과 E개의 간선 정보가 주어진다.
첫째 줄에는 V와 E의 갯수, 정점의 정보를 묻는 쿼리의 갯수가 주어지고 둘째 줄부터 간선의 정보(연결된 정점의 번호쌍)가 주어진다.
그 다음 줄에는 정점의 인접정점들이 무엇인지 묻는 쿼리가 정점번호로 주어진다.
정점의 번호는 0~V-1까지 이며, 간선정보는 오름차순으로 나열되어 주어진다. 또한 중복 간선은 존재하지 않는다.
입력으로 주어지는 쿼리의 정점에 인접한 정점들을 각 줄에 출력하라.
(2<=V<=100, 1<=E<=1000)
'''
num_vertices = 0
adjListArr = list()


def createGraph(n):
    global adjListArr
    global num_verticess
    adjListArr = list()
    for i in range(n):
        adjListArr.append(list())
    num_vertices = n


def addEdge(src, dest):
    global adjListArr
    adjListArr[src].append(dest)
    adjListArr[dest].append(src)


def displayGraph(i):
    global adjListArr
    adjList = list(adjListArr[i])
    for i in adjList:
        print(i, end=' ')
    print()


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        V, E, Q = map(int, input().split())
        createGraph(V)

        for i in range(E):
            sv, ev = map(int, input().split())
            addEdge(sv, ev)

        print("#%d" % test_case)

        for i in range(Q):
            sv = int(input())
            displayGraph(sv)


if __name__ == "__main__":
    main()