[TOC]

# Sort

| 알고리즘  | 평균 시간 | 최악 시간 |    기법     |              비고              |
| :-------: | :-------: | :-------: | :---------: | :----------------------------: |
|  Bubble   |  O(n^2)   |  O(n^2)   | 비교와 교환 |          코딩이 쉽다.          |
| Counting  |  O(n+k)   |  O(n+k)   |   비교환    |        n이 작아야 가능         |
| Selection |  O(n^2)   |  O(n^2)   | 비교와 교환 |    회수가 위 두개보다 적음     |
|   Quick   | O(nlogn)  |  O(n^2)   |  분할 정복  |      평균적으로 가장 빠름      |
| Insertion |  O(n^2)   |  O(n^2)   | 비교와 교환 |       n이 작으면 효율적        |
|   Merge   | O(nlogn)  | O(nlogn)  |  분할 정복  | 연결 리스트의 경우 가장 효율적 |



### Bubble Sort

> 배열을 2중 순회하며 크기 비교를 통해 정렬
>
> 코딩이 가장 손쉽다.
>
> O(n^2)

```python
def bubble_sort(data):
  for i in range(len(data)):
    swap = False
    for j in range(i+1, len(data)):
      if data[i] > data[j+1]:
        data[i], data[j] = data[j], data[i]
        swap = True
    if not swap:
      break
```

```python
def bubble_sort(arr):
    end = len(arr) - 1
    while end > 0:
        last_swap = 0
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last_swap = i
        end = last_swap
```



### Counting Sort

> 각 항목이 몇 개씩 있는지 세어 선형시간에 정렬. 정수만 가능. max : k값을 알아야함
>
> n이 비교적 작을 때만 가능하다.
>
> O(n+k)

```python
def counting_sort(A, k):
    # A : 입력 배열
    # C : 카운트 배열
    C = [0] * (k+1)

    for i in range(len(A)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i - 1]

    res = [0] * len(A)
    for i in range(len(res) - 1, -1, -1):
        res[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    return res
```

> 

```python
def my_counting_sort(A, k):
    # A : 입력 배열
    # C : 카운트 배열
    C = [0] * (k + 1)

    for i in range(len(A)):
        C[A[i]] += 1

    res = []
    for i in range(len(C)):
        if C[i]:
            res.extend(([i]*C[i]))
    return res
```



### Selection Sort

> 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
>
> selection algorithm을 전체 자료에 적용
>
> O(n^2)

```python
def selection_sort(list):
    for i in range(len(list) - 1):
        min = i
        for j in range(i + 1, len(list)):
            if list[min] > list[j]:
                min = j
        list[i], list[min] = list[min], list[i]
```



### Quick Sort

> 정렬의 꽃
>
> pivot을 정해서, 기준점보다 작은 데이터는 왼쪽, 큰데이터는 오른쪽으로 모은다.

```python
def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)
```



### Insertion Sort

> 2번째 index부터 시작
>
> 해당 index앞에 있는 데이터부터 비교하여 값이 작으면 뒤인덱스로 복사

```python
def insertion_sort(list):
	  for end in range(1, len(list)):
      	i = end
        while i > 0 and list[i - 1] > list[i]:
          	list[i - 1], list[i] = list[i], list[i - 1]
            i -= 1
```



### Merge Sort

> 리스트를 반으로 잘라 재귀적으로 분할 정복을 이용해 정렬

```python
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr
```

```python
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))
```

