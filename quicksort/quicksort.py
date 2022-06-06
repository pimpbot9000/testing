arr = [1,3,42,5,6,4,5,6,6,7,6,5,6,6,7,3,23,23,23,4,5,1]

def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp

def partition(arr, i, j):
    ii = i
    jj = j
    pivot = arr[jj]
    print("pivot,", pivot)
    while i < j:
        while arr[i] < arr[jj] and i < j:
            i += 1
            print("iii", i)
        while arr[j] >= pivot and i < j:
            j -= 1
        swap(arr, i, j)

    swap(arr, j, jj)

    output = (ii, i - 1), (i + 1, jj)
    print(output)
    return output

def quicksort(arr, i, j):
    print(arr)
    (i, ii), (j, jj) = partition(arr, i, j)
    if i < ii:
        quicksort(arr, i, ii)
    if j < jj:
        quicksort(arr, j, jj)

quicksort(arr, 0, len(arr) - 1)
#partition(arr, 0, len(arr) - 1)
print(arr)
