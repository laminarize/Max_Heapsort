def sink(lst, idx, size):
    largest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < size and lst[left] < lst[largest]:  # < Makes Max Heap
        largest = left
    if right < size and lst[right] < lst[largest]:  # < Makes Max Heap
        largest = right

    if largest != idx:
        lst[idx], lst[largest] = lst[largest], lst[idx]
        sink(lst, largest, size)

def heap_sort(lst):
    n = len(lst)
    # Build the max heap
    for i in range(n // 2 - 1, -1, -1):
        sink(lst, i, n)  # Use modified sink

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        sink(lst, 0, i)  # Use modified sink
    return lst

my_list = [5, 1, 8, 3, 2]
sorted_list = heap_sort(my_list)

print(sorted_list)
