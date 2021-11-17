# Question 1
# Selection sort  O(N2)

def selectionSort( itemsList ):
    n = len( itemsList )
    for i in range( n - 1 ):
        minValueIndex = i

        for j in range( i + 1, n ):
            if itemsList[j] < itemsList[minValueIndex] :
                minValueIndex = j

        if minValueIndex != i :
            temp = itemsList[i]
            itemsList[i] = itemsList[minValueIndex]
            itemsList[minValueIndex] = temp

    return itemsList


el = [13, 36, 9, 25, 40, 83, 73]

print(selectionSort(el))

# Question 2
# Bubble sort  O(N2)


def bubblesort(descseq):
    n = len(descseq)
    for i in range(n - 1):
        flag = 0
        for j in range(n - 1):
            if descseq[j] > descseq[j + 1]:
                tmp = descseq[j]
                descseq[j] = descseq[j + 1]
                descseq[j + 1] = tmp
                flag = 1
        if flag == 0:
            break
    return descseq

el = [21, 12, 9, 37, 6]

result = bubblesort(el)

print(result)

# Question 3
# Insertion sort

def insertionSort(alist):
   for i in range(1, len(alist)):
        current = alist[i]
   while i > 0 and alist[i-1] > current:
                alist[i] = alist[i-1]
                i = i-1
                alist[i] = current

   return alist

print(insertionSort([5, 8, 10, 19, 20, 24, 46]))

# Question 4
# Merge sort  O(N * log n)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


def merge_arrays(left_array, right_array):
    merged_array = []
    i = j = 0
    while i < len(left_array) or j < len(right_array):
        if i == len(left_array):
            merged_array.append(right_array[j])
            j += 1
            continue
        if j == len(right_array):
            merged_array.append(left_array[i])
            i += 1
            continue

        if left_array[i] >= right_array[j]:
            merged_array.append(left_array[i])
            i += 1
        else:
            merged_array.append(right_array[j])
            j += 1

    return merged_array


test_list = [1, 8, 10, 17, 26, 21, 32, 4]
print(test_list)
print(merge_sort(test_list))