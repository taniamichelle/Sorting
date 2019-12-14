# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # print('arr', arr)
    # loop through n-1 elements: 
    for i in range(0, len(arr)): 
        cur_index = i 
        smallest_index = cur_index
        for j in range(i+1, len(arr)): 
            # TO-DO: find next smallest element. (hint, can do in 3 loc) 
            if arr[j] < arr[smallest_index]:0
                smallest_index = j
        # TO-DO: swap
        print('arr[j]', arr[j], 'min', arr[smallest_index])
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]        
        print('new arr[j]', arr[j])
        print('new arr', arr)

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # traverse through and compare all array elements in first iteration
    # set the range for comparison (1st round: i, 2nd: i-1, 3rd: i-2, etc)
    for i in range(len(arr)-1, 0, -1):
        print('len(arr): ', len(arr))
        # compare within set range of i
        for j in range(i):
            print('j: ', j, 'i: ', i)
            # compare element(i) with its right side neighbor
            if arr[j] > arr[j+1]:
                # swap (smallest to the left) if element found (n)is greater than the next element(n + 1)
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
    print('arr1: ', bubble_sort(arr1))

# How SWAPping works using temp(orary) variable: 
# a = 10
# b = 5
# temp = a #temp stores value of a temporarily. temp is later assigned to b
# a = b
# b = temp
# print('a: ', a) #prints 5
# print('b: ', b) #prints 10

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr



arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
selection_sort(arr1)


#INSERTION SORT pseudocode:
# for i: 1 to length(A) -1
#   j=i
#   while j>0 and A[j-1]>A[j]
#       swap A[j] and A[j-1]
#       j = j-1