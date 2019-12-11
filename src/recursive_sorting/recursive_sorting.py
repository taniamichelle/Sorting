# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    print('array A: ', arrA, 'array B: ', arrB)
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = []
    # print(merged_arr)
    # # TO-DO
    while len(arrA) != 0 and len(arrB) != 0:
        # print('arrA: ', arrA, 'arrB: ', arrB)
        if arrA[0] >= arrB[0]:
            merged_arr.append(arrB[0]) # can combine these 2 lines: merged_arr.append( arrB.pop(0) )
            arrB.pop(0) 
        elif arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.pop(0) 
        # print('merged: ', merged_arr)
    if len(arrA) != 0:
        merged_arr.extend(arrA)
    elif len(arrB) != 0:
        merged_arr.extend(arrB)
    
    # print('merged_array:', merged_arr, 'arrB: ', arrB, 'arrA: ', arrA)

    return merged_arr
    # print('merged array: ', merged_arr)

arra = [0, 1, 4, 9]
arrb = [0, 1, 2, 3, 4]
# print(merge(arra, arrb))

# TO-DO: implement the Merge Sort function below USING RECURSION
# RECURSIVE MERGE SORT PSEUDOCODE TO HALVE ARRAYS:
# mergesort(array a)
#     if(n == 1)  # base case
#         return a

# left = a[0] ... a[n/2]  # Left side of mid-point
# right = a[n/2 +1] ... a[n]  # Right side of mid-point

# right = mergesort(right)
# left = mergesort(left)

# return merge(left, right)

def merge_sort( arr ):  # arr has length of 4
    # TO-DO
    if len(arr) <= 1:  # base case
        print('arr: ', arr)
        return arr

    middle = len(arr) // 2  # middle point is at arr[2]
    left = arr[:middle]
    right = arr[middle:]
    
    # recursion
    l = merge_sort(left)
    r = merge_sort(right)

    # merge the left and right arrays
    result = merge(l, r)
    print('result: ', result)
    return result

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
merge_sort(arr1)


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



# RECURSIVE MERGE SORT PSEUDOCODE TO RECOMBINE ARRAYS:
# merge(array a, array b)
#     array c

#     while(a and b have elements)
#         if(a[0]>b[0])
#             add b[0] to the end of c
#             remove b[0] from b
#         else
#             add a[0] to the end of c
#             remove a[0] from a
    
#     # at this point either a or b is empty

#     while(a has elements)
#         add a[0] to the end of c
#         remove a[0] from a
    
#     while(b has elements)
#         add b[0] to the end of c
#         remove b[0] from b

#     return c 

# def merge( arrA, arrB ):
#     print('array A: ', arrA, 'array B: ', arrB)
#     elements = len( arrA ) + len( arrB )
#     merged_arr = [0] * elements
    # print(merged_arr)
    # # TO-DO
    # for i in range(len(merged_arr)):
    #   if arrA >= 1:
    #     if len(arrA[0]) > len(arrB[0]):
    #         merged_arr[i] = arrA[i]

