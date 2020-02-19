# TO-DO: complete the helper function below to merge 2 sorted arrays

import math

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    # TO-DO
    a = 0                                   # index of arrA
    b = 0                                   # index of arrB

    for i in range(elements):

                                            # ran out of elements in either array:
        if a == len(arrA):                  # if arrA has no more elements to compare
            merged_arr[i:] = arrB[b:]       # set rest of merged_array to rest of arrB
            break
        if b == len(arrB):                  # if arrA has no more elements to compare
            merged_arr[i:] = arrA[a:]       # set rest of merged_array to rest of arrA
            break
                                            # comparisons for each currently selected index in each array:
        if arrA[a] <= arrB[b]:              # if arrA current val is smaller,
            merged_arr[i] = arrA[a]
            a += 1                          # progress to next index of current array!
        else:
            merged_arr[i] = arrB[b]         # if arrB current val is smaller,
            b += 1                          # progress to next index of current array!

    return merged_arr

# print(merge([2, 3, 4, 6, 8, 8], [3, 7, 9]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    length = len(arr)                       # grabs length of whole array

    if length == 1 or length == 0:          # if array is empty or only has 1 value
        return arr                          # nothing more needs to be done

    breakIndex = math.floor(length/2)       # in case of odd number

    leftArray = arr[:breakIndex]            # separates left at breakIndex - 1
    rightArray = arr[breakIndex:]           # separates right at breakIndex

    leftArray = merge_sort(leftArray)       # recurse left
    rightArray = merge_sort(rightArray)     # recurse right

    return merge(leftArray, rightArray)     # once done, combine two arrays into one sorted array

# print(merge_sort([2, 3, 4, 6, 8, 8, 3, 7, 9]))














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
