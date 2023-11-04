import maze

class Game():
    '''Holds the game solving logic. Initialize with a fully initialized maze'''

    def __init__(self, maze):
        self._maze = maze

    # Creating simple methods (like the next two) to abstract core parts 
    #   of your algorithm helps increase the readability of your code.
    #   You will find these two useful in your solution.

    def _is_move_available(self, row, col, path):
        '''If (row, col) is already in the solved path then it is not available'''
        return (row, col) not in path

    def _is_puzzle_solved(self, row, col):
        '''Is the given row,col the finish square?'''
        return self._maze.get_finish() == (row, col)


    ########################################################
    # TODO - Main recursive method. Add your algorithm here.

    def try_move(self,row,col,score,path):
        '''
        parameter(self,row,col,score,path)
        ----------------------------------
            if (check 3 conditions):
            a) next move is not wall 
            b) self._is_move_avaliable(row,col,path)
            c) next move is a move in maze
                if maze is solved:
                    return (score,path)
                else
                    call the recusive method find_route to continue to find possible route
            else:
                return (-1, path)
        '''
        #checking the 3 conditions
        if self._is_move_available(row,col,path) and self._maze.is_move_in_maze(row,col) and not self._maze.is_wall(row,col):
            
            value = self._maze.make_move(row,col,path) #get the value at a specific path
            
            #if the puzzle is solved/else continue updating score and path
            if self._is_puzzle_solved(row,col):
                return(score + value,path)
            else:
                return self.find_route(row,col,score + value,path)
        #if the next path is invalid
        else:
            return(-1,path)
        
    def find_route(self, currow, curcol, curscore, curpath):
        '''
        parameter(self,currow,curcol,curscore,curpath)
        ------------------------------------------------
            check if the current position is the starting position:
                update teh score based on the move made from starting position 
        
            Initialize variables for storing the best score and path

            Try to move in each of the four directions (up, down, right, left)
                Update the best score and path if a better score is found
        
            Return the best score and path, or (-1, []) if the finish position cannot be reached

        '''
        #check if the current position is the starting point 
        if self._maze.get_start() == (currow,curcol):
             curscore = self._maze.make_move(currow,curcol,curpath)
        
        #intialize the best_score anf best_path
        best_score = -1
        best_path = []

        # Try to move in each of the four directions (up, down, right, left)
        for i in range(4):
            if i == 0:
                    score, path = self.try_move(currow + 1, curcol, curscore, list(curpath))
            elif i == 1:
                    score, path = self.try_move(currow - 1, curcol, curscore, list(curpath)) 
            elif i == 2:
                    score, path = self.try_move(currow, curcol + 1, curscore, list(curpath))
            else:
                    score, path = self.try_move(currow, curcol - 1, curscore, list(curpath))
            if score > best_score:
                    best_score = score
                    best_path = path

        #return the best score and path
        if best_score > -1:
            return(best_score, best_path)
        else:
            return(-1, [])


# This block of code will be useful in debugging your algorithm. But you still need
#  to create unittests to thoroughly testing your code.
if __name__ == '__main__':
    # Here is how you create the maze. Pass the row,col size of the grid.
    grid = maze.Maze(3, 6)
    # You have TWO options for initializing the Value and Walls squares.
    # (1) init_random() and add_random_walls()
    #     * Useful when developing your algorithm without having to create 
    #         different grids
    #     * But not easy to use in testcases because you cannot preditably
    #         know what the winning score and path will be each run
    # (2) _set_maze()
    #     * You have to create the grid manually, but very useful in testing
    #       (Please see the test_game.py file for an example of _set_maze())
    grid.init_random(0,9) # Initialze to a random board
    grid.add_random_walls(0.2)   # Make a certian percentage of the maze contain walls

    # AFTER you have used one of the two above methods of initializing 
    #   the Values and Walls, you must set the Start Finish locations. 
    start = (0,2)
    finish = (1,1)
    grid.set_start_finish(start, finish)

    # Printing the starting grid for reference will help you in debugging.
    print(grid)           # Print the maze for visual starting reference

    # Now instatiate your Game algorithm class
    game = Game(grid)     # Pass in the fully initialize maze grid

    # Now initiate your recursize solution to solve the game!
    # Start from the start row, col... zero score and empty winning path
    score, path = game.find_route(start[0], start[1], 0, list())
    print(f"The winning score is {score} with a path of {path}")

