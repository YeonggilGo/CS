class Queue:
    class Point:
        def __init__(self, y, x, c):
            self.y = y
            self.x = x
            self.c = c

    def __init__(self, capacity):
        self.queue = [0] * capacity
        self.head = self.rear = 0

    def isEmpty(self):
        return self.head <= self.rear

    def enQueue(self, y, x, c):
        self.queue[self.head] = self.Point(y, x, c)
        self.head = self.head + 1

    def deQueue(self):
        if self.isEmpty():
            return None
        self.rear = self.rear + 1
        return self.queue[self.rear - 1]


def breadthFirstSearch():
    queue = Queue(row * column)
    queue.enQueue(0, 0, 0)
    MAP[0][0] = 0

    while queue.isEmpty() == False:
        p = queue.deQueue()

        if p.y == row - 1 and p.x == column - 1:
            return p.c

        if p.y + 1 < row and MAP[p.y + 1][p.x]:
            queue.enQueue(p.y + 1, p.x, p.c + 1)
            MAP[p.y + 1][p.x] = 0
        if p.x + 1 < column and MAP[p.y][p.x + 1]:
            queue.enQueue(p.y, p.x + 1, p.c + 1)
            MAP[p.y][p.x + 1] = 0
        if p.y - 1 >= 0 and MAP[p.y - 1][p.x] != 0:
            queue.enQueue(p.y - 1, p.x, p.c + 1)
            MAP[p.y - 1][p.x] = 0
        if p.x - 1 > 0 and MAP[p.y][p.x - 1] != 0:
            queue.enQueue(p.y, p.x - 1, p.c + 1)
            MAP[p.y][p.x - 1] = 0

    return -1


def main():
    global MAP, row, column
    T = int(input())

    for test_case in range(1, T + 1):
        row, column = map(int, input().split())
        MAP = [[int(num) for num in input().split()] for _ in range(row)]
        print("#%d %d" % (test_case, breadthFirstSearch()))


if __name__ == "__main__":
    main()