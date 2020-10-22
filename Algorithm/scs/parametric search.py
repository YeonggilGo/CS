"""
parametric search는 어떤 알고리즘으로 해를 바로 구해내는 것이 아니고, 임의의 값을 던지고 맞는지 확인해가며 해를 구하는 방법이다.
길이가 각각 다른 K개의 리본을 가지고 있다. 공예작품을 만들기 위해 가지고 있는 리본을 잘라서 길이가 동일한 N개의 리본재료를 만들려고 한다. 리본재료의 최대 길이를 구하시오
( 1 <= K <= 10,000; 1 <= N <= 1,000,000; K <= N )
- 손실되는 길이는 없음
- 만들 수 없는 경우는 없다
- 이미 자른 리본은 붙일 수 없다
- 자를 때는 정수 cm 단위로 자른다
"""

MAX_RIBBON = 100

K = 0
N = 0
sizeRibbonTape = [None for _ in range(MAX_RIBBON)]


def search(low, high):
    max = -1

    while low <= high:
        mid = low + (high - low) // 2

        numRibbonTape = 0
        for i in range(K):
            numRibbonTape += sizeRibbonTape[i] // mid

        if numRibbonTape >= N:
            low = mid + 1
            if max < mid:
                max = mid
        else:
            high = mid - 1

    return max


def main():
    global K, N

    T = int(input())

    for test_case in range(1, T + 1):
        low, high = 1, 0
        K = int(input())
        N = int(input())

        for i in range(K):
            sizeRibbonTape[i] = int(input())
            if high < sizeRibbonTape[i]:
                high = sizeRibbonTape[i]

        max = search(low, high)

        print("#%d %d" % (test_case, max))


if __name__ == "__main__":
    main()
