def heapify(arr, root, last_leaf):
  # first find out the max child between left and right leaves
  # left_leave = root * 2 + 1
  # right_leave = left_leaf + 1
  # then compare root vs max child
  child = root * 2 + 1
  while True:
    if child > last_leaf:
      break
    if child + 1 <= last_leaf and arr[child] < arr[child + 1]:
      # if right_leaf > left_leaf, max child is the right leaf
      child += 1
    if arr[root] < arr[child]:
      arr[root], arr[child] = arr[child], arr[root]
      # maybe the swith make the sub tree unqualified, so need to repeat heapify on the subtree
      root = child
    else:
      # the subtree is qualified
      break

def heap_sort(arr):
  n = len(arr)
  # last leaf idex is n - 1
  # so last parent (subroot) = n // 2 - 1
  # from last parent to the root, build the max heap tree
  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, i, n - 1)
  # switch root (the max of the arr) vs last leaf and build the max heap tree again (last_leaf -= 1)
  for i in range(n - 1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    heapify(arr, 0, i - 1)

arr = [9,7,8,6,4,5,3,1,2,0]
heap_sort(arr)
print(arr)