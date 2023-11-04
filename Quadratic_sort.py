# TODO: implement the 4 functions (as always, include docstrings & comments)

# return the index of the 0 in such a list in O(log(n)) using binary search
def find_zero(L): 
    ''' 
    parameter(list)
    ---------------
        left end point is 0 
        right end point len(list) -1 

        while left end pt is less than or equal to the right end pt
            using binary search, create and set a median value to (left+right)//2
            if median value is 0 
                return index of median value 
            else if median value is greater than 0 
                reassign the right end pt to median index - 1
            else if median value is less than 0 
                reassign the left end pt to median index + 1
            
            return None if 0 doesn not exsits in given list    
    '''
    left = 0 #left bound 
    right = len(L)-1 #right bound 

    while left <= right: #length of the list > 1
        median = (left + right)//2 # floor division to find median
        if L[median] == 0: 
            return median
        elif L[median] > 0:
            right = median - 1
        elif L[median] < 0: 
            left = median + 1

    return None #if 0 is not in the list L     
    
def bubble(L, left, right): 
    """
    Sorts the sub-list L[left:right] using the bubble sort algorithm in O(n^2) time complexity
    
    parameter(L,left,right)
    -----------------------
        for nth assortion in range(left end pt, right end pt - 1)
            create a boolean variable best_case = True, assume that L has been sorted 
            for each index in range (left, right-1)
                if former number is greater than the later number 
                    sawp so in order --> smaller #, bigger #
                    set best_case to False, can't exist the program early because more sorting may be needed
                if L is compeletly sorted 
                    break the outer for loop and exists program early
                    O(n) in the best case 
    """
    # L has an increasing order, find the smallest number --> move towards to the right to find the biggest number
    for n in range(left,right-1):
        best_case = True #assume list L is already sorted 
        for i in range(left,right-1):
            if L[i] > L[i+1]: #if the former number is greater than the later number 
                L[i],L[i+1] = L[i+1],L[i]
                best_case = False
        if best_case: # O(n) in the best case
            break 
 

def selection(L, left, right):
    '''
    parameter(L,lef,right)
    ----------------------
        for index i in range(left pt, right pt - 1)
            create and set the minimum index (min_index) to i
            for index j in range (i + 1, right pt)
                if index j value < index min_index value 
                    reassign the min_index to index j 
            sawp so gradually in order: smallest # --> 2nd smallest --> 3rd smallest ... 3rd biggest --> 2nd biggest --> biggest  #      
    '''
    for i in range(left, right - 1):
        min_index = i
        for j in range(i + 1, right):
            if L[j] < L[min_index]:
                min_index = j #update minimum index 
        L[i], L[min_index] = L[min_index], L[i] #swap the smaller number to the left, bigger to left

def insertion(L, left, right):
    '''
    parameter(L,left,right)
    -----------------------
        for index i in range(left pt + 1, right pt)
            create and set a comparison value (compare_v) to L[i] value
            create and set a index j value to i -1 
            while index j is >= left pt and L[j] value > compare_v
                the bigger value, L[j] moves to the right in list L by 1 index
                index j deducted by 1, loop back to relocate (compare_v), the current minimum value
           value at the j+1 position does not change/gets sorted (if value(s) before compare_v is/are smaller than compare_v)
    ''' 
    for i in range(left+1, right):
        compare_v = L[i] 
        j = i - 1
        while j >= left and L[j] > compare_v: # index j is in the bound and if L[j] value is greater than L[i] value
            L[j+1] = L[j] # value L[j] moves to the right in list L by 1 index
            j -= 1 # loop back to relocate compare_v, the current minimum value
        L[j+1] = compare_v # the value at the j+1 position does not change/gets sorted 

def sort_halfsorted(L, sort):
    '''Efficiently sorts a list comprising a series of negative items, a single 0, and a series of positive items
    
        Input
        -----
            * L:list
                a half sorted list, e.g. [-2, -1, -3, 0, 4, 3, 7, 9, 14]
                                         <---neg--->     <----pos----->

            * sort: func(L:list, left:int, right:int)
                a function that sorts the sublist L[left:right] in-place
                note that we use python convention here: L[left:right] includes left but not right

        Output
        ------
            * None
                this algorithm sorts `L` in-place, so it does not need a return statement

        Examples
        --------
            >>> L = [-1, -2, -3, 0, 3, 2, 1]
            >>> sort_halfsorted(L, bubble)
            >>> print(L)
            [-3, -2, -1, 0, 1, 2, 3]
    '''

    idx_zero = find_zero(L)     # find the 0 index 
    sort(L, 0, idx_zero)        # sort left half
    sort(L, idx_zero+1, len(L)) # sort right half