import unittest
from binary_search import BinarySearchTree

class BSTTestCase(unittest.TestCase):
    def test_bestTest(self):
        bst=BinarySearchTree()

        #Test 'add' and 'size'
        bst.add(10,"A value")
        self.assertEqual(bst.size(),1)
        bst.add(5,"A value")
        self.assertEqual(bst.size(),2)
        bst.add(30,"A value")
        self.assertEqual(bst.size(),3)

        #Test 'inorder_walk'
        self.assertListEqual(bst.inorder_walk(),[5,10,30])

        bst.add(15,"value")
        self.assertListEqual(bst.inorder_walk(),[5,10,15,30])

        #Test 'preorder_walk'
        self.assertListEqual(bst.preorder_walk(),[10,5,30,15])

        #Test 'postorder_walk'
        self.assertListEqual(bst.postorder_walk(),[5,15,30,10])

        #test 'smallest'
        self.assertEqual(bst.smallest(),5)

        #test 'largest'
        self.assertEqual(bst.largest(),30)

        #test 'search'
        #the output itself gives the test. since the value is not returned, this test case cannot be applied
        #also delete implements search

        #test 'delete'
        bst.delete(5)
        self.assertListEqual(bst.inorder_walk(),[10,15,30])


if __name__=="__main__":
    unittest.main()
