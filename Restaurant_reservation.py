import random
class Time:
    """A class that represents time in the format HH:MM"""
    def __init__(self, hour, minute):
        self.hour = int(hour)
        self.minute = int(minute)

    def __lt__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self < other, and False otherwise"""
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        else:
            return False
    
    def __eq__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self == other, and False otherwise"""
        if self.hour ==  other.hour and self.minute == other.minute:
            return True
        else:
            return False

    def __repr__(self):
        """Return the string representation of the time"""
        return f"{self.hour:02d}:{self.minute:02d}"

class Entry:
    """A class that represents a customer in the waitlist"""
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __lt__(self, other):
        """Compare two customers based on their time, if equal then compare based on the customer name"""
        if self.time == other.time:
            return self.name < other.name
        return self.time < other.time

    def __repr__(self):
        'repr method to return the waitlist'
        return f'Waitlist({self.name}, {self.time})'

class Heap:
    def __init__(self):
        self._L = []

    def __len__(self): return len(self._L)

    def _i_parent(self, idx):
        "returns index of parent of idx"
        return (idx-1) // 2 if (idx-1) // 2 >= 0 else None
    
    def _i_left(self, idx):
        "left child"
        il = idx*2+1
        return il if il<len(self) else None
    
    def _i_right(self, idx):
        "right child"
        ir = idx*2+2
        return ir if ir<len(self) else None

    def insert(self, item, priority):
        "adds item w/ given priority to heap"
        # append entry to list
        # upheap until balanced

        new_e = Entry(item, priority)
        self._L.append(new_e)
        self._upheap(len(self)-1)
    
    def _upheap(self, idx):
        "upheaps item at idx"
        # find parent index
        i_p = self._i_parent(idx)

        # while parent exists and parent is bigger: swap
        while i_p is not None and self._L[i_p] > self._L[idx]:
            # swap them
            self._L[i_p], self._L[idx] = self._L[idx], self._L[i_p]
            # update vars for next loop
            idx = i_p
            i_p = self._i_parent(idx)
        
    def peek(self):
        "returns (but does not remove) item with minimum priority"
        return self._L[0].name
    
    def remove_min(self):
        "removes and returns item with minimum priority"
        min_item = self._L[0]
        #edge case, only one entry in heap 
        if len(self) == 1:
            self._L.pop()
            return min_item 

        self._L[0] = self._L.pop() #swap
        self._downheap(idx = 0)

        return min_item
        
    def _find_min_child(self, idx):
        "returns idx of minimum child if it exists, otherwise None"
        il = self._i_left(idx)
        ir = self._i_right(idx)

        # handles 0 and 1 child cases 
        if ir is None: 
            return il 
        else: 
            return il if self._L[il] < self._L[ir] else ir 
        
    def _downheap(self, idx):
        "downheaps item at idx"
        # sawp w/ minimum child until (i) end of tree or (ii) both children are bigger 
        i_min = self._find_min_child(idx)

        while (i_min is not None) and (self._L[i_min] < self._L[idx]):
            self._L[i_min], self._L[idx] = self._L[idx], self._L[i_min]
            idx = i_min 
            i_min = self._find_min_child(idx)
    def heapsort(self):
        '''help sorting the heap in ascending order'''
        #create a heap for sorted data 
        sorted_data = []

        # add the minimum item of self._entries into new ordered heap
        while len(self._L) > 0:
            sorted_data.append(self.remove_min())
        
        # return a sorted heap 
        return sorted_data
    
class Waitlist:
    def __init__(self):
        'this method initializes an empty priority queue'
        self._entries = Heap()

    def _helper_time(self,time):
        'a helper function to make sure that an input time is valid. Hour must be within 0-24 and min within 0-60. Must include : and in military time'
        x = time[0:2]
        y = time[3:5]
        if int(x) in range(25) and int(y) in range(60):
            return True 
        else:
            return False     
    
    def add_customer(self, item, priority):
        'this method allows the user to add a customer to the priority queue. Customers with an earlier time reservation take priority'
        #if the input is not length of 5, then invalid
        if len(priority) != 5:
            return 'Invalid time input!'
        
        #check if : is in time input
        if ":" not in priority:
            return 'Invalid time input!'
        
        if self._helper_time(priority):
            self._entries.insert(item, priority)
        
        else:
            return False
        
        

    def peek(self):
        'this method "peeks" and returns a tuple of the first customer in the queue. In the form of (customer, priority)'
        if self._entries._L == []:
            return 'There are no people in the waitlist'
        
        return self._entries.peek()
        
    def seat_customer(self):
        'The program should extract the customer with the highest priority  (i.e., the earliest reservation time) from the priority queue. Return a tuple of the extracted item (customer, time)'
        return self._entries.remove_min()


    def print_reservation_list(self):
        'Prints all customers in order of their priority (reservation time). Maintains the heap property'
        #sort self._entries using heapsort 
        sorted_entries = self._entries.heapsort()

        #print the sorted entries 
        for i in sorted_entries:
            print(f'{i.name}, {i.time}')
    
    def change_reservation(self, name, new_priority):
        'Change the reservation time (priority) for the customer with the given name'
        index = 0
        
        for i in self._entries._L:
           if i.name == name:
                i.time = new_priority
                self._entries._upheap(index)
                self._entries._downheap(index)
            
           else:
               index +=1
        
        
    #Add other methods you may need

if __name__ == '__main__':
    time = '25:70'
    x = time[0:2]
    y = time[3:5]
    print(x)
    print(y)

