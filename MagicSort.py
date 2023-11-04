from math import log2
import math 
import random

def linear_scan(L):
    '''
    Check 3 Edge Cases:
    1)if the input list is already sorted
    2)if the total number of misplaced items is less than 5 
    3)if the input list is in reverse order 

    if the total number of misplaced is greater than 5, call the insertion sort algorithm on given list  
    '''
    is_sorted = True
    count_misplaced = 0
    is_reversed = True

    for i in range (len(L)-1):
        if L[i] > L[i+1]:
            count_misplaced += 1
        else:
            is_reversed = False
    # edge case 1: if the list is already sorted
    if count_misplaced == 0: 
        return 'is_sorted'
    # edge case 2: if the list is reversely sorted, called the function reverse_list
    if is_reversed:
        return 'is_reversed'
    # edge case 3: insertion sort if there's at most 5 items out of place
    elif count_misplaced <= 5 and count_misplaced > 0:
        return 'insertion_sort'
    else:
        quicksort(L)
        return 'quicksort'
    
    
def reverse_list(L):
    '''
    Sort the given reversed list in corret, accending order
    '''
    #reverse a list in linear time
    L = L[::-1]
    return L

def insertionsort(L, left, right):
    '''
    Pick an hypothetical minmum, compare with other items in the given list L 
    If the other item is greater than the current minimum, then swap positions of the two items
    Set the next value as the hypothetical minimum, and compare with all the items follwing that hypothetical minimum  
    '''
    if right is None:
        right = len(L)
    
    for each_item in range(left+1, right):
        a = L[each_item] #items to compare w/ hypothetical min 
        b = each_item -1 #hypothetical min 

        while (b >= left) and (a < L[b]):
            L[b+1] = L[b] #swap if the previous > after 
            b -= 1 # continuing finding the idx for that mib L[b]
        L[b+1] = a #no swap 
    return L

def quicksort(L, left = 0, right = None, method_used = set(), recursive_depth=0):
    '''
    Use divde-conquer algrithm with a pivot point (the last item in the sublist) to sort a given list.
    By comparing with the pivot, the function divides the remaining items into 2 sublists, according to whether they are greater or less than the pivot. 
    Because the algorithm is doing in-place sorting, no combining needed in the end. 
    When the sublists of these divide-and-conquer algorithms drop to 16 or fewer items, sort those sublists using insertion sort instead.
    If the recursive depth reaches twice the best-case maximum-depth, fall back to mergesort to sort the list.
    '''
    
    recursive_depth += 1
    max_depth = log2(len(L)) + 1  

    #Base case
    if right is None: 
        right = len(L) 

    if right - left <= 16: 
        method_used.add("insertion_sort")
        insertionsort(L,left,right)
        return L
        
    elif recursive_depth >= max_depth:
        method_used.add("mergesort")
        mergeSort(L)
        return mergeSort(L,left,right)


    else:
        method_used.add('quicksort')
        #Divide
        pivot = partition(L, left, right, recursive_depth)

        #Conquer
        quicksort(L, left, pivot, method_used,recursive_depth)
        recursive_depth -= 1
        quicksort(L, pivot+1, right, method_used, recursive_depth)
        recursive_depth -= 1

    return L

def partition(L, i, j, recursive_depth):
    '''
    A helper function for quicksort.
    Pivot is the last item in the sublist.
    Separate rest of the items (except the pivot) into 2 sublists, depending on whether they are greater/less than the pivot. 
    i is the idex of element used to compare with the pivot, j is the index of pivot.
    Swap pivot and i if value at index i > pivot. 
    '''
    pivot = j - 1
    j = pivot - 1
    #Pivot all items between left and right
    while i < j :
        while L[i] < L[pivot]:
            # Find leftmost item < pivot
            i += 1
        while i < j and L[j] >= L[pivot]:
            # Find rightmost item > pivot
            j -= 1
        if i < j:
            # Swap them
            L[i], L[j] = L[j], L[i]
    #Swap pivot and i
    if L[i] >= L[pivot]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    return i

def mergeSort(L, left = 0, right = None):
    '''
    A sorting algorithm that works by dividing an array into smaller sublists
        Sorting each sublists.
        Then merging the sorted sublists back together to form the final sorted array.
    When the sublists drops to 16 or fewer items, sort those sublists using insertion sort instead.

    '''
    #Base Case
    if right is None:
        right = len(L)

    if len(L) <= 16:
        insertionsort(L,left,right)
        return L
    if len(L) < 2:
        return L
    
    #Divide
    mid = len(L)//2
    left = L[:mid]
    right = L[mid:]
    
    #Conquer
    mergeSort(left)
    mergeSort(right)
    
    #Combine 
    # print(left,right,L)
    merge(left,right,L)
    return L

def merge(left,right,L):
    '''
    It's a helper function for the mergesort function. 
    i,j are the idex value of sublists A, B
    if A[i] > B[i], then add B[i] to the general big list L
    if B[i] > A[i], then ass A[i] to the general big list L
    add the rest of the items in either sublist A or sublist B to the general big list L
    '''
    i , j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L[i+j] = left[i]
            i += 1
        else:
            L[i+j] = right[j]
            j += 1
    L[i+j:]  = left[i:] + right[j:]

def magic_sort(L,left = 0,right = None):
    '''
    Operate all the other sorting algorithms to find the best sorting method(s) on a given list L 
    Call the linear_scan first to test if the given function suits any of 3 Edge Cases.
        In the second edge case, if insertion sort is needed, call the insertion sort.  
    If not, then call quicksort on the given list L. 
    Track all the sorting method used in a set called method_used. 
    '''
    # Implementation of MagicSort 
    result = linear_scan(L)
    if result == 'is_sorted':
        method_used = {'is_sorted'}
        return method_used
    
    elif result == 'is_reversed':
        method_used = {'is_reversed'}
        return method_used
    
    elif result == 'insertion_sort':
        insertionsort(L,left,right)
        method_used = {'insertion_sort'}
        return method_used

    elif result == 'quicksort':
        method_used = {'quicksort'}
        quicksort(L,0, None, method_used)
        return method_used

if __name__ == "__main__":
    
    '''
    L1 = [1,2,3,4,5]
    print(magic_sort(L1))

    L2 = [-1,-2,-3,-4]
    print(magic_sort(L2))

    L3 = [1,2,3,6,5,-1,9,8,0,-7]
    print(magic_sort(L3))
    
    randomlist = []
    for i in range(0,3000):
        a = random.randint(1,20000)
        randomlist.append(a)
    
    print(magic_sort(randomlist))

    L5 = []
    print(magic_sort(L5))
    '''
    L6 = [12, 3,6,1,-8,0,9,54]
    print(magic_sort(L6))


