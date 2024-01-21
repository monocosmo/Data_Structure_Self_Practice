def quick_sort(arr, start, end):
  if start >= end:
    return
  
  l = start
  r = end
  p = arr[l]

  while l < r:
    while l < r and arr[r] >= p:
      # from right to left, find arr[x] smaller then p
      r -= 1
    # switch the position of arr[x] with p
    arr[l] = arr[r]
    while l < r and arr[l] <= p:
      # from left to right, find arr[x] larger then p
      l += 1
    # switch the position of arr[x] with p
    arr[r] = arr[l]
    # now l == r and the left part are nums smaller and right part are nums larger, p should be put here
    arr[l] = p

  # recursion
  quick_sort(arr, start, l - 1)
  quick_sort(arr, r + 1, end)

arr = [9,8,5,4,2,3,1,7,6]
quick_sort(arr, 0, 8)
print(arr)