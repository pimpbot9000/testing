a = [60, 4, 16,2,3,41,2,3, 2]

def merge(arr, index1, index2):
  (i, ii) = index1
  (j, jj) = index2

  tmp = [0] * (jj - i + 1)
  k = i
  
  for z in range(0, len(tmp)):
    tmp[z] = arr[z + k]
    
  i = 0; ii -= k; j -= k; jj -= k
  
  while i <= ii or j <= jj:
    if i > ii:
      arr[k] = tmp[j]
      j += 1
    elif j > jj:
      arr[k] = tmp[i]
      i += 1
    elif tmp[i] < tmp[j]:      
      arr[k] = tmp[i]
      i += 1
    elif tmp[j] <= tmp[i]:
      arr[k] = tmp[j]
      j += 1
    k += 1

def merge_sort(arr, l, r):
  if l < r:
    m = l+(r-l)//2
    merge_sort(arr, l, m)
    merge_sort(arr, m + 1, r)
    merge(arr, (l , m), (m + 1, r))
    
merge_sort(a, 0, len(a) - 1)
print(a)
