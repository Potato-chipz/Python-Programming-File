from hw3 import *
import unittest 

class TestHw3(unittest.TestCase):
    def test_find_pairs_naive(self):
        '''
        parameter
        ---------
            empty list 
            normal list with some numbers 
            list for duplicate test 

            expected result for empty list 
            expected result for traget equals 0 
            expected result for duplicate test, i.e. when target value is equal to the expected duplicate values in the input list
            expected result for a normal list, no indentical pairs should be produced

            assert an empty list should produce an empty set 
            assert target 0 should produce an empty set
            assert duplicate test should produce an empty set
            assert a normal list produces an correct set of pairs 

        
        '''

        test_list_empty = []
        test_list_normal = [6, 5, 2, 8, 9, 1]
        test_list_dup = [1, 2, 3, 4, 5] # list for duplicate test case

        
        exp_result_empty = find_pairs_naive(test_list_empty,7) # expected result for test case with an empty list
        exp_result_target_0 = find_pairs_naive(test_list_normal,0) # expected result for test case where target = 0 
        exp_result_dup = find_pairs_naive(test_list_dup,10) # expected result for test case with expected duplicate values as the target
        exp_result_normal = find_pairs_naive(test_list_normal,7) # expected result for test case with an normal list; no identical number pairs, such as Pair(3,3), should be produced 
        


        self.assertEqual(str(exp_result_empty),'set()') # test case with an empty list, evaluates to True
        self.assertEqual(str(exp_result_target_0), 'set()') # test case with target = 0, evaluates to True
        self.assertEqual(str(exp_result_dup),'set()') #test case with expected duplicate values as the target, evaluates to True
        self.assertEqual(str(exp_result_normal),'{(6, 1), (5, 2)}') # test case with an normal list; no identical number pairs (i.e. Pair(3,3)) are produced, evalutes to True
    
    def test_find_pairs_optimized(self):
        '''
        parameter
        ---------
            empty list 
            normal list with some numbers 
            list for duplicate test 

            expected result for empty list 
            expected result for traget equals 0 
            expected result for duplicate test, i.e. when target value is equal to the expected duplicate values in the input list
            expected result for a normal list, no indentical pairs should be produced

            assert an empty list should produce an empty set 
            assert target 0 should produce an empty set
            assert duplicate test should produce an empty set
            assert a normal list produces a correct set of pairs 

        
        '''
        test_list_empty = []
        test_list_normal = [6,5,2,8,9,1]
        test_list_dup = [1, 2, 3, 4, 5] # list for duplicate test case

        
        exp_result_empty = find_pairs_naive(test_list_empty,7) # expected result for test case with an empty list
        exp_result_target_0 = find_pairs_naive(test_list_normal,0) # expected result for test case where target = 0 
        exp_result_dup = find_pairs_naive(test_list_dup,10) # expected result for test case with expected duplicate values as the target
        exp_result_normal = find_pairs_naive(test_list_normal,7) # expected result for test case with an normal list; no identical number pairs, such as Pair(3,3), should be produced 
        


        self.assertEqual(str(exp_result_empty),'set()') # test case with an empty list, evaluates to True
        self.assertEqual(str(exp_result_target_0), 'set()') # test case with target = 0, evaluates to True
        self.assertEqual(str(exp_result_dup),'set()') #test case with expected duplicate values as the target, evaluates to True
        self.assertEqual(str(exp_result_normal),'{(6, 1), (5, 2)}') # test case with an normal list; no identical number pairs (i.e. Pair(3,3)) are produced, evalutes to True


unittest.main()