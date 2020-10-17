
def heapPush(value):
    global heapCount
    heapCount += 1              # 마지막 노드번호 증가
    heap[heapCount] = value     # 마지막 노드에 값 저장
    current = heapCount         # 마지막 노드가 현재 노드
    parent = current // 2       # 부모 노드 계산

    # 루트가 아니고, 부모 노드의 값이 자식노드 값 보다 더 크면 -> swap
    while parent and heap[parent] > heap[current]:
        heap[parent], heap[current] = heap[current], heap[parent]
        current = parent
        parent = current // 2

def heapPop():
    global heapCount
    retValue = heap[1]          # 리턴 값(루트노드)
    heap[1] = heap[heapCount]   # 마지막을 루트노드로 이동
    heap[heapCount] = 0         # 마지막 노드 지움
    heapCount -= 1              # 카운터 감소
    parent = 1
    child = 2 * parent

    if child + 1 <= heapCount:              # 오른쪽 자식이 존재하면
        if heap[child] > heap[child+1]:     # 왼쪽, 오른쪽 중 작은 값을 child에 저장
            child = child + 1

    # 자식노드가 힙카운트보다 작고 부모노드가 자식노드보다 크면 -> swap
    while child <= heapCount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = 2 * parent
        if child + 1 <= heapCount:              # 오른쪽 자식이 존재하면
            if heap[child] > heap[child + 1]:   # 왼쪽, 오른쪽 중 작은 값을 child에 저장
                child = child + 1

    return retValue


# 최소힙
heapCount = 0                   # 노드가 하나도 없는 상태(heap의 원소의 개수)
temp = [7, 2, 5, 3, 4, 6]       # 입력 정점
N = len(temp)
heap = [0 for _ in range(N+1)]  # 이진 힙 구현을 위한 리스트 생성(크게 잡아야 함)


for i in range(N) : # 힙에 저장
    heapPush(temp[i])

for i in range(N) : # 출력 확인
    print(heapPop(), end = " ")
print()

