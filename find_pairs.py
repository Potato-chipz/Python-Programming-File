import time

def find_pairs_naive(lst = [],target = 0):
    '''
    parameter(list default to empty, target default to int 10)
    ----------------------------------------------------------
        create my_set --> an empty set

        first for loop --> 1st number
            second for loop --> 2nd number 
                if a pair adds up to the target value 
                    if the flipped version hasn't been added to my_set yet
                        add the number pair as a tuple to my_set
        return my_set 
    '''
    my_set = set() #empty set
    
    for i in lst:                                  # n x
        for ii in lst:                             # n x
            if i + ii == target and i != ii:       # 2
                if not((ii,i) in my_set):          # 1
                    my_set.add((i,ii))             # 1                                             
    return my_set                                  # 1
                                                   # ---------
                                                   # n*(n*(2+1+1)) + 1 = n*4n+1 = 4n^2 + 1 = O(n^2) 
                                                   # The big O analysis shows that the algorithm can be repsented by a Quadratic function, so the computer takes in n^2 amount of operations per time unit   

def find_pairs_optimized(lst = [], target = 0):
    '''
    parameter(list default to empty, target default to int 10)
    ----------------------------------------------------------
        create an empty set named 'pairs' 
        change list 'lst' to set 'newlst'

        for each number in lst
            if the other number needed to get the target is in set 'newlst'
                if the number pair is unique (no duplicate of the reversed version)
                    if the number pair is not composed of two same integers 
                        add the number pair as a tuple to the set 'pairs'

    '''
    pairs = set() #empty set for pairs 
    newlst = set(lst) #turn the given list to set 
    
    for num in lst:                                                           # n x
        #if the two numbers needed are both in the given list                              
        if (target-num) in newlst:                                            # 1
            #prevent duplicates of pairs         
            if(target-num,num) not in pairs:                                  # 1
                #prevent pairs that have identical values such as (2,2)
                if target-num != num:                                         # 1
                    pairs.add((num,target-num))                               # 1
    return pairs                                                              # 1
                                                                              # -----------
                                                                              # n*(1+1+1+1) + 1 = 4n + 1 = O(n)
                                                                              # The big O analysis shows that the algorithm can be repsented by a Linear function, so the computer takes in n amount of operations per time unit. Because the optimized function turns the input list to a set, hence the runtime is faster than that of the naive function.   


def measure_min_time(fn, *args, n_trials = 10):
    '''
    parameter(function,arguments,number of trails)
    ---------
        default the minimum time to infinity

        for each trail 
            create a variable 'start' to record the starting time 

            unpack arguments 
            create a varibale 'end' to record the ending time

            if the end-start time is less than the previously stored minimum time 
                update the minimum time with the smallest number 
       
        return the minimum time
    '''

    minimum_time = float('inf')

    for i in range(n_trials):
        start = time.time()

        fn(*args) # unpack arguments of a function
        end = time.time()

        if end-start < minimum_time:
            minimum_time = end-start #update the minimum time with the smallest number

    return  minimum_time

#code to print the tables
if __name__ in '__main__':
    print('='*40)
    print(f"{'n':<10}{'naive':<10}{'optimized':<10}")
    print('-'*40)

    for n in[10,50,100,150,100,200,300,500]:
        L = [i for i in range(n)] #trials
        naive = 1000*measure_min_time(find_pairs_naive,L,7) #time for naive
        optimized = 1000*measure_min_time(find_pairs_optimized,L,7) #time for optimized

        print(f"{n:<10}{naive:<10.4f}{optimized:<10.4f}")

#table footer
print('-'*40)

