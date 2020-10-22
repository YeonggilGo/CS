"""
Plane sweeping은 여러 개의 직사각형이 주어졌을 때, 총 넓이를 구하는 알고리즘이다.
테스트케이스 수 T와 지도의 수 N(1 ≤ N ≤ 10,000)이 주어진다. 다음 N개의 줄에는 각 지도의 정보가 주어진다. 지도의 정보는 네 정수 x1, y1, x2, y2 (0 ≤ x1 < x2 ≤ 30,000, 0 ≤ y1 < y2 ≤ 30,000)으로 이루어져 있다. (x1, y1)와 (x2, y2)은 직사각형의 왼쪽 아래 좌표와 오른쪽 위 좌표이다. 모든 지도는 직사각형이고, 변은 항상 x축 또는 y축에 평행하다. 첫째 줄에 지도를 모두 합쳤을 때, 그 면적을 출력한다. (직사각형을 모두 합쳤을 때 면적)
"""

class Rec:
    def __init__(self, x, y1, y2, end):
        self.x = x
        self.y1 = y1
        self.y2 = y2
        self.end = end


def update(x, left, right, nodeLeft, nodeRight, val):
    global tree
    if left > nodeRight or right < nodeLeft:
        return
    if left <= nodeLeft and right >= nodeRight:
        cnt[x] += val
    else:
        mid = (nodeLeft + nodeRight) >> 1
        update(x * 2, left, right, nodeLeft, mid, val)
        update(x * 2 + 1, left, right, mid + 1, nodeRight, val)

    tree[x] = 0
    if cnt[x] > 0:
        tree[x] = nodeRight - nodeLeft + 1
    if cnt[x] == 0 and nodeLeft < nodeRight:
        tree[x] = tree[x * 2] + tree[x * 2 + 1]


def main():
    global tree, cnt
    T = int(input())

    for test_case in range(1, T + 1):

        N = int(input())

        v = [0] * N * 2

        idx = 0
        for _ in range(N):
            x1, y1, x2, y2 = map(int, input().split())
            v[idx] = Rec(x1, y1, y2, 1)
            idx = idx + 1
            v[idx] = Rec(x2, y1, y2, -1)
            idx = idx + 1

        v = sorted(v, key=lambda rec: rec.x)

        tree = [0] * 65538
        cnt = [0] * 65538
        px = v[0].x
        ans = 0
        for i in range(0, idx):
            ans += (v[i].x - px) * tree[1]
            update(1, v[i].y1, v[i].y2 - 1, 0, 32768, v[i].end)

            px = v[i].x

        print("#%d %d" % (test_case, ans))


if __name__ == "__main__":
    main()