# Question 1
# Even first
#O(n)

def even_odd(arr):
    next_even = 0
    next_odd = len(arr) - 1
    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1

test_list = [13, 6, 15, 20, 25, 9, 12, 18]
print(test_list)
even_odd(test_list)
print(test_list)


# Question 2
# Increment a number
# O(n)

def plus_one(arr):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        print(i)
        print(arr)
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1

    print(arr)
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr


test_list_1 = [1, 2, 7]
test_list_2 = [1, 2, 8]
test_list_3 = [9, 9, 9]

print(test_list_1)
print(plus_one(test_list_1))

print(test_list_2)
print(plus_one(test_list_2))

print(test_list_3)
print(plus_one(test_list_3))