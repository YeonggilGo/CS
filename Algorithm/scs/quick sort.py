arr = []
num = 0


def quick_sort(first, last):
    if first < last:
        pivot = first
        i = first
        j = last

        while i < j:
            while arr[i] <= arr[pivot] and i < last:
                i += 1
            while arr[j] > arr[pivot]:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[pivot], arr[j] = arr[j], arr[pivot]

        quick_sort(first, j - 1)
        quick_sort(j + 1, last)


def main():
    global arr, num
    T = int(input())

    for test_case in range(1, T + 1):
        num = int(input())
        arr = [int(x) for x in input().split()]

        quick_sort(0, num - 1)
        print("#%d" % test_case, end=' ')
        for j in range(0, num):
            print(arr[j], end=' ')
        print()


if __name__ == "__main__":
    main()