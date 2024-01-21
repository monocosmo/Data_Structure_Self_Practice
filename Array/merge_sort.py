def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2
  l = arr[:mid]
  r = arr[mid:]
  return merge(merge_sort(l), merge_sort(r))

def merge(l, r):
  res = []
  i = 0
  j = 0
  while i < len(l) and j < len(r):
    if l[i] <= r[j]:
      res.append(l[i])
      i += 1
    else:
      res.append(r[j])
      j += 1
  res += l[i:]
  res += r[j:]
  return res

arr = [8,7,5,4,6,3,1,2]
print(merge_sort(arr))