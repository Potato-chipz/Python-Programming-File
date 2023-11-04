from letters import *
def highest_freq(file):
    '''
    parameter
    _________
        local variable HIGHEST, represneting the frequency of a letter, set to float 0.0
        Initializes a local variable key, set to an empty string

           for loop to find the highest frequncy letter from an input file 
                HIGHEST change if a larger frequcy appears
                KEY associates with the highes frequency
                
        Returns a tuple containing a most frequently appear letter and its frequncy 
    '''
    dictionary_a = letter_frequency(letter_count(file)) # all letters with each of their frequency
    HIGHEST = 0.0 
    KEY = ''

    for x,y in dictionary_a.items():
        if dictionary_a[x] > HIGHEST:
            HIGHEST = dictionary_a[x] # higest frequency
            KEY = x #find key that has the highest frequency 
    return (KEY,HIGHEST)

#ASSERT TEST for function highest_freq
if __name__ == "main":
    hf = highest_freq('Self_written_test.txt') #A fixed input 
    expected_hf = ('a', 0.14285714285714285)
    assert(hf == expected_hf) #Evaluates to True 
