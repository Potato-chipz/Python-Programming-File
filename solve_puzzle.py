def solve_puzzle(L:list, index = 0, track = None ): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable""" 
    # 1) Base case: have you found a valid solution?
    if track == None: 
        track = set()
    
    if len(L) == 0: 
        return False 

    # 2) Find all valid next-steps
    # 3) Recursively explore next-steps, returning True if any valid solution is found
    elif index == (len(L)-1): 
        return True 
    elif index in track:
        return False 
    else: 
        #update track 
        track.add(index)

        move = L[index]

        left_move = (index - move) % len(L)
        right_move = (index + move) % len(L)

        found_left = solve_puzzle(L,left_move,track)
        found_right = solve_puzzle(L,right_move,track)

        return found_left or found_right

if __name__ == '__main__':
    list_test = [3,6,4,1,3,4,2,0]
    list_test_2 = [3, 4, 1, 2, 0]

    print(solve_puzzle(list_test))
    print(solve_puzzle(list_test_2))

  