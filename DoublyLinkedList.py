# Do not modify this class
class Node:
    'Node object to be used in DoublyLinkedList'
    def __init__(self, item, _next=None, _prev=None):
        'initializes new node objects'
        self.item = item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        'String representation of Node'
        return f"Node({self.item})"


class DoublyLinkedList:
    def __init__(self, items=None):
        'Construct a new DLL object'
        self._head = None
        self._tail = None
        self._len = 0
        self._nodes = dict()    # dictionary of item:node pairs

        # initialize list w/ items if specified
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        'returns number of nodes in DLL'
        return self._len

    # TODO: Modify the 4 methods below to keep `self._nodes` up-to-date
    def add_first(self, item):
        'adds item to front of dll'
        # add new node as head
        self._head = Node(item, _next=self._head, _prev=None)
        self._len += 1
        
        # if that was the first node
        if len(self) == 1: self._tail = self._head

        # otherwise, redirect old heads ._tail pointer
        else: self._head._next._prev = self._head

        #push the order of other nodes by 1 
        'UPDATE dictionary self._nodes to add an item:node pair'
        self._nodes[item]= self._head
        

    def add_last(self, item):
        'adds item to end of dll'
        # add new node as head
        self._tail = Node(item, _next=None, _prev=self._tail)
        self._len += 1
        
        # if that was the first node
        if len(self) == 1: self._head = self._tail

        # otherwise, redirect old heads ._tail pointer
        else: self._tail._prev._next = self._tail

        'UPDATE dictionary self._nodes to add an item:node pair'
        self._nodes[item] = self._tail

    def remove_first(self):
        'removes and returns first item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._head.item

        # move up head pointer
        self._head = self._head._next
        self._len -= 1

        # was that the last node?
        if len(self) == 0: self._tail = None

        else: self._head._prev = None

        'UPDATE self._nodes to delete an item:node pair'
        del self._nodes[item]
        
        return item
        
    def remove_last(self):
        'removes and returns last item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._tail.item

        # move up tail pointer
        self._tail = self._tail._prev
        self._len -= 1

        # was that the last node?
        if len(self) == 0: self._head = None

        else: self._tail._next = None

        'UPDATE self._nodes to delete an item:node pair'
        del self._nodes[item]

        return item
        
    # TODO: Add a docstring and implement
    def __contains__(self, item):
        '''
        parameter(item)
        --------------------
            return T/F if item is in dict self._nodes
        '''
        return item in self._nodes

    # TODO: Add a docstring and implement
    def neighbors(self, item):
        '''
        parameter(item)
        ---------------
            if item not in dict self._nodes
                raise RuntimeError
            elif only one node in dict 
                return (None, None)
            elif item represents the head node
                return (None, next node's item)
            elif item reprsents the tail node 
                return (previous node's item, None)
            else 
                return(previous node's item, next node's item)
        '''
        if not (item in self._nodes):
            raise RuntimeError('Item not in the DLL!')
        elif len(self) == 1:
            return (None, None)
        elif item == self._head.item:
            return (None,self._head._next.item)
        elif item == self._tail.item:
            return (self._tail._prev.item,None)
        else:
            return (self._nodes[item]._prev.item, self._nodes[item]._next.item) #item represents a node surrounded front & back by 2 other nodes

    # TODO: Add a docstring and implement
    def remove_node(self, item):
        '''
        parameter(item)
        ---------------
            if item not in the DLL self._nodes
                raise RuntimeError 
            else if item represents the head node 
                call remove_first function
            else if item represents the tail node 
                call remove_last function
            else if removing a node in the middle 
                 linked the after node's _prev attribute to point to the previous node
                 linked the previous node's _next attribute to point to the after node 
                 delete the middle node with the given value 'item' in self._nodes
        '''
        if not(item in self._nodes): # if item is not in DLL
            raise RuntimeError("Item not in the DLL!")
        elif self._nodes[item] == self._head: #if item is the head 
            self.remove_first()
        elif self._nodes[item] == self._tail: #if item is the tail 
            self.remove_last()
        else: # if item represents the middle node 
            self._nodes[item]._next._prev = self._nodes[item]._prev # link the previous node's _prev to the next node's _prev 
            self._nodes[item]._prev._next = self._nodes[item]._next # linke the previous node's _next to the next node's _next 
            del self._nodes[item] # delete the item:node pair from the dictionary
        
        return item


    
    