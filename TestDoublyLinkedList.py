from DoublyLinkedList import DoublyLinkedList as DLL
import unittest

# Basic tests are provided for you, but you need to implement the last 3 unittests
class testDLL(unittest.TestCase):
    def test_addfirst_removefirst(self):
        'adds items to front, then removes from front'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_first()

    def test_addlast_removelast(self):
        'adds items to end, then removes from end'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.new_method(dll, n, i)

            with self.assertRaises(RuntimeError):
                dll.remove_last()

    def new_method(self, dll, n, i):
        self.assertEqual(dll.remove_last(), n-1-i)

    def test_add_remove_mix(self):
        'various add/remove patterns'
        dll = DLL()
        n = 100

        # addfirst/removelast
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), i)

        # addlast/removefirst
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), i)

        # mix of first/last
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                if i%2: dll.add_last(i) # odd numbers - add last
                else: dll.add_first(i)  # even numbers - add first

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                if i%2: self.assertEqual(dll.remove_last(), n-i) # odd numbers: remove last
                else: self.assertEqual(dll.remove_first(), n-2-i) # even numbers: remove first

    # TODO: Add docstrings to and implement the unittests below
    def test_contains(self):
        '''
        parameter
        ---------
            create an empty double linked list LL

            for each item in range 5 
                add each item into LL
            
            for each item in range 5 
                assert each item has been added to LL

            for each item in range 5 
                remove each item from LL
                assert that the item is no longer in LL
        '''
        LL = DLL()

        for i in range(5):
            LL.add_last(i)
        
        for i in range(5):
            self.assertTrue(i in LL) # evaluates to TRUE
        
        for i in range(5):
            LL.remove_first()
            self.assertFalse(i in LL) # evaluates to TRUE

    def test_neighbors(self):
        '''
        create an empty double linked list ll
        add items 2-->3-->4 into ll

        create anotehr empty double linked list ll_1, which contains only 1 item represeting one node
        add item 0 to ll_1

        assert a middle node with item 3 will return a neighbor pair (2,4) --> asserts to TRUE 
        assert a head node with item 2 will return a neighbor pair (None,3) --> asserts to TRUE
        assert a tail node with item 4 will return a neighbor pair (3,None) --> asserts to TRUE
        assert ll_1, which has only one node represented by item 0, will return a neighbor pair (None,None) --> asserts to True
         
        '''
        ll = DLL()
        ll.add_last(2)
        ll.add_last(3)
        ll.add_last(4)

        ll_1 = DLL() # a double linked list where there's only 1 node 
        ll_1.add_last(0) 

        self.assertEqual(ll.neighbors(3),(2,4)) # evaluates to TRUE
        self.assertEqual(ll.neighbors(2),(None,3)) # evaluates to TRUE
        self.assertEqual(ll.neighbors(4),(3,None)) # evaluates to TRUE
        self.assertEqual(ll_1.neighbors(0),(None,None)) # no previous or next node; evaluates to TRUE

    def test_remove_item(self):
        '''
        parameter
        ---------
            create an empty doubled linked list LL 
            
            for each item in range 0-4
                add 0-->1-->2-->3-->4 to LL 
            
            remove the head node represented by item 0 
            assert the new head node is represented by item 1 --> assert to TRUE
            assert node with item 0 is no longer in LL

            remove the tail node represented by item 4
            assert the new tail node is represented by item 3 --> assert to True 
            assert node with item 4 is no longer in LL

            remove the middle node represented by item 2
            assert node 1's attribute _next points to node 3
            assert node 3's attribute _prev points to node 1
            assert node with item 2 is no longer in LL   
        '''
        LL = DLL() # empty double linked list

        # LL = node 0 <--> node 1 <--> node 2 <--> node 3 <--> node 4 
        for i in range(5): 
            LL.add_last(i)
        
        LL.remove_node(0) #remove the first node 
                          # DLL.remove_node(LL, 0)
        self.assertEqual(LL._head.item,1)
        self.assertFalse(0 in LL) #evaluates to TRUE 

        LL.remove_node(4) #remove the last ndoe 
        self.assertEqual(LL._tail.item,3)
        self.assertFalse(4 in LL) #evaluates to TRUE 

        LL.remove_node(2) #remove the middle node 
        assert(LL._nodes[1]._next == LL._nodes[3]) # Evaluates to TRUE
        assert(LL._nodes[3]._prev == LL._nodes[1]) #evaluates to TRUE
        self.assertFalse(4 in LL) #evaluates to TRUE 
        

unittest.main()
