def del_max(lst, heap):
  '''
  Input: a list (lst) where the element in position 0 is the largest element of array.
  Output: the array without the largest element (lst) and the sorted array (heap)
  '''
    heap.append(lst.pop(0))
    return lst, heap

def sink(lst, idx):
  '''
  sink function verifies that the parent node is actually a parent node by comparing it to its children (left & right).
  If it is not a parent node (parent > child) then it swaps the 2 and traverses down the array continuing verification.
  If it is verified to be a parent it returns the list (lst) with max parent in position 0.

  Input: Unheaped heap (lst)
  Output: Heap with largest element at position 0
  '''

    # Children index - updated every call
    left = 2 * idx + 1
    right = 2 * idx + 2

    # Check if index is still in bounds of array (prevents index error)
    if left < len(lst):
        print(f'left: {lst[left]}')

        # Check if index is still in bounds of array (prevents index error)
        if right < len(lst):
            print(f'right: {lst[right]}')
            print(f'index: {lst[idx]}')

            # If left or right child is larger than parent
            if lst[left] > lst[idx] or lst[right] > lst[idx]:

                # If right child is larger than left child - swap parent and right child
                # If swap occurs update the idx variable to step through heap.
                if lst[right] > lst[left]:
                    print('swapped right')
                    lst[right], lst[idx] = lst[idx], lst[right]
                    idx = right

                # If left child is larger than right child - swap parent and left child
                # If swap occurs update the idx variable to step through heap.
                if lst[left] > lst[right]:
                    print('swapped left')
                    lst[left], lst[idx] = lst[idx], lst[left]
                    idx = left

        # If right index is out of bounds - still need to check left
        else:
            if lst[left] > lst[idx]:
                print('swapped lleft')
                lst[left], lst[idx] = lst[idx], lst[left]
                idx = left
              
    # Return list that now has the largest element at position 0 (max heap)
    return lst   

def heap_sort(lst, heap=[]):

    # Base case of recursive call to end algorithm
    if len(lst) == 0:
        return []

    # Step through all current parent nodes starting at floor of len(lst)//2 - 1 and send to sink - working backwards through array with every iteration.
    for idx in range(len(lst)//2 - 1, -1, -1):
        print(lst, lst[idx], idx)
        lst = sink(lst, idx)
        print(lst, lst[idx])

    # Send heapified array to del_max to pop max value 
    lst, heap = del_max(lst, heap)

    # Recursively call heapsort to heapify array after pop
    heap_sort(lst,heap)
    return heap

print(heap_sort([4, 2, 7, 9, 12, 1, 3, 0, 10, 11]))

### Output: [12, 11, 10, 9, 7, 4, 3, 2, 1, 0]
