#Q 1
# Below the arithmetical mean   O(n)

def below_ar_mean(arr):
    ar_mean = sum(arr) / len(arr)
    print(f'Ar. mean: {ar_mean}')
    final_list = []
    for num in arr:
        if num < ar_mean:
            final_list.append(num)
    return final_list

list_to_test = [1, 3, 5, 6, 4, 10, 2, 3]
print(list_to_test)
print(below_ar_mean(list_to_test))



# Q 2
# Two lowest elements   O(n log n)

def find_two_lowest_elements(arr):
    arr.sort()
    print(arr)
    return arr[:2]

list_to_test = [198, 3, 4, 9, 10, 9, 2]
print(list_to_test)
print(find_two_lowest_elements(list_to_test))
