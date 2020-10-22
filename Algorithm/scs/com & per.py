"""
순열조합(permutation combination), 순열은 순서가 부여된 임의의 집합을 다른 순서로 뒤섞는 연산이며, 조합은 집합에서 일부 원소를 취해 부분 집합을 만드는 방법을 말한다.
주어진 문자열 str (길이 n)에 대해 아래 두 가지를 차례로 출력하시오.
1. str의 n개 character를 일렬로 배열하는 모든 경우를 출력하시오.
2. str의 n개 character 중 k개를 취하는 모든 경우를 출력하시오.
(제한사항: 주어진 string에 동일한 알파벳이 중복으로 포함되지 않음. String의 maximum size는 10. k <= n.)
"""

combinationStack = []


def printString(cArr):
    for i in cArr:
        print(i, end='')
    print()


def swap(cArr, x, y):
    cArr[x], cArr[y] = cArr[y], cArr[x]


def permutation(cArr, l, r):
    if l == r:
        printString(cArr)
    else:
        for i in range(l, r + 1, 1):
            swap(cArr, l, i)
            permutation(cArr, l + 1, r)
            swap(cArr, l, i)


def push(ch):
    combinationStack.append(ch)


def pop():
    combinationStack.pop()


def combination(cArr, length, offset, k):
    if k == 0:
        printString(combinationStack)
    else:
        for i in range(offset, length - k + 1, 1):
            push(cArr[i])
            combination(cArr, length, i + 1, k - 1)
            pop()


def main():
    global cArr, N, K
    T = int(input())

    for test_case in range(1, T + 1):
        cArr = list(input())

        N = int(input())
        K = int(input())

        print("#%d" % test_case)

        permutation(cArr[0:N], 0, N - 1)
        combination(cArr, N, 0, K)


if __name__ == "__main__":
    main()