# Question 1
# Even First

def even_odd(arr):
    next_even = 0
    next_odd = len(arr) - 1

    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1
    return arr


print(even_odd([1, 2, 3, 4, 5, 6]))


def even_odd(arr):
    u = 0
    for i in range(len(arr)):
        if arr[u] % 2 != 0:
            temp = arr[u]
            arr.remove(arr[u])
            arr.append(temp)
        else:
            u += 1
    return arr


print(even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Question 2
# Increment a number

def plus_one(a: list[int]) -> List[int]:
    a[-1] += 1
    for i in reversed(range(1, len(a))):
        if a[i] !=10:
            break
        a[i] = 0
        a[i - 1] += 1
    else:
        if a[0] == 10:
           a[0] = 1
           a.append(0)
    return a
