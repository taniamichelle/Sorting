# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    print(merged_arr)
    # TO-DO
    while len(arrA) or len(arrB) != 0:
        if arrA[0] > arrB[0]:
            merged_arr.append[arrB[0]]
            arrB[0].remove 
        else:
            merged_arr.append[arrA[0]]
            arrA[0].remove 

        while len(arrA) != 0:
            merged_arr.append[arrA[0]]
            arrA[0].remove
        while len(arrB) != 0:
            merged_arr.append[arrB[0]]
            arrB[0].remove 
    
    return merged_arr
    print('merged array: ', merged_arr)

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

# RECURSIVE MERGE SORT PSEUDOCODE TO HALVE ARRAYS:
# mergesort(array a)
#     if(n == 1)
#         return a

# arrayOne = a[0] ... a[n/2]
# arrayTwo = a[n/2 +1] ... a[n]

# arrayOne = mergesort(arrayOne)
# arrayTwo = mergesort(arrayTwo)

# return merge(arrayOne, arrayTwo)

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