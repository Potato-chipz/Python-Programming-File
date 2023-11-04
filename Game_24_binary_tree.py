import itertools
class BETNode:
    """Node for binary expression tree"""

    # Don't modify the provided code below - start working at add_left()

    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A':1, '1':1, '2':2, '3':3, '4':4,
                     '5':5, '6':6, '7':7, '8':8, '9':9,
                     '10':10, 'J':11, 'Q':12, 'K':13}

    def __init__(self, value = None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # These are proficed for you - do not modify. They let you hash BETs (so they can be stored in sets)
    # and compare them (so you can write unittests more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None: return False
        return self.value == other.value and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))
    
    # START HERE
    def add_left(self,node):
        '''add a left child to teh current node'''
        self.left = node 

    def add_right(self,node):
        '''add a right child to the current node'''
        self.right = node

    ### Needs to be FIXED###
    def evaluate(self):
        '''recursively evaluated the subtree rooted at this BETNode'''
        # if value is digit/char, gets interger representation for string 
        if self.value in BETNode.CARD_VAL_DICT.keys():
            return int(BETNode.CARD_VAL_DICT[self.value])
            
        #Operator node, recursively evaluate left and right subtrees 
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()

        #divison by 0 
        if right_val == 0 and self.value == '/':
             return f'Error: No divison by zero'

        #normal operatiosn without exceptions 
        if self.value == '+':
            return left_val + right_val
        elif self.value == '-':
            return left_val - right_val
        elif self.value == '*':
            return left_val * right_val
        elif self.value == '/':
                return left_val / right_val
              
    def __repr__(self):
        '''display the repr expression stored in the BET using infix notation '''
        if self.value in BETNode.OPERATORS:
            #Operator node, recursively represent left and right subtrees
            left_repr = repr(self.left)
            right_repr = repr(self.right)
            return f'({left_repr}{self.value}{right_repr})' #i.e. (2-3) or (4*5)
        else:
            #leaf node, no children, return its value as a string 
            return str(self.value)


def create_trees_helper(L):
    '''Helper function for create_trees, create trees of different permutations'''
    stack = list()
    for i in L:
        stack.append(BETNode(i))
        if i in BETNode.OPERATORS:
            my_node = stack.pop() # pop operator and store as x value 
            right = stack.pop()
            left = stack.pop()
            my_node.add_right(right)
            my_node.add_left(left)
            stack.append(my_node)

    return stack.pop()

def create_trees(cards):
    """
    Return a set of every valid tree for a given collection of 4 cards with only 3 operators.
    There are five valid shapes. For each shape, generate every possible permutation of operators.
    
    Args:
        cards (list): A list of 4 cards (values or operators)
        
    Returns:
        set: A set of every valid tree
    """

    # Create a set to store all valid trees 
    valid_trees = set() 

    ###Iterate through all the permuattions of cards, operators, and tree shapes### 
    # Generate all unique permutatios of the 4 cards
    for C in itertools.permutations(cards):
        # Generate all uniqye 3-operator combinations 
        for X in itertools.product(BETNode.OPERATORS,repeat = 3):
            # Define the 5 valid tree shapes
            # CCXCXCX
            L = [C[0],C[1],X[0],C[2],X[1],C[3],X[2]]
            valid_trees.add(create_trees_helper(L))
            # CCCXXCX
            L = [C[0],C[1],C[2],X[0],X[1],C[3],X[2]]
            valid_trees.add(create_trees_helper(L))
            # CCXCCXX
            L = [C[0],C[1],X[0],C[2],C[3],X[1],X[2]]
            valid_trees.add(create_trees_helper(L))
            # CCCXCXX
            L = [C[0],C[1],C[2],X[0],C[3],X[1],X[2]]
            valid_trees.add(create_trees_helper(L))
            # CCCCXXX
            L = [C[0],C[1],C[2],C[3],X[0],X[1],X[2]]
            valid_trees.add(create_trees_helper(L))
    return valid_trees


def find_solutions(cards):
    '''
    Calls create_trees(cards) to get all valid trees for a passed in 4-card hand.
    Then evaluates each tree and returns a set of all the ways to get 24. 
    Store the string representation of each card in set 
        Returns a set of string representations of cards that form valid solutions
    '''

    # Evaluate each tree and store the string representation of valid solution that equals 24
    solutions = set()
    # for each tree in valid_trees
    for tree in cards:
        result = tree.evaluate()
        if result == 24:
            solutions.add(tree)
    
    #return a set of trees in string representation
    return solutions
