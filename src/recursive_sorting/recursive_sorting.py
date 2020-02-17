# TO-DO: complete the helper function below to merge 2 sorted arrays

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    # TO-DO
    a = 0
    b = 0
    for i in range(0, elements-1):

        # ran out of elements in either array:
        if a == len(arrA):                  # if arrA has no more elements to compare
            merged_arr[i:] = arrB[b:]       # set rest of merged_array to rest of arrB
        elif b == len(arrB):                # if arrA has no more elements to compare
            merged_arr[i:] = arrA[a:]       # set rest of merged_array to rest of arrA

        # comparisons:
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr

print(merge([4, 6, 8], [2, 7, 9]))














































# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
