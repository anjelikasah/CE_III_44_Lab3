from binary_search import BinarySearchTree

bst=BinarySearchTree()

bst.add(10,"A value")
bst.add(20,"B value")
bst.add(5,"A value")
bst.add(12, "D value")
bst.add(30,"E value")
bst.add(2,"G value")
bst.add(35,"F value")

print("The inorder traversal of the tree is")
print(bst.inorder_walk())
print("The preorder traversal of the tree is")
print(bst.preorder_walk())
print("The postorder traversal of the tree is")
print(bst.postorder_walk())

print(bst.smallest(),"is the smallest")
print(bst.largest(),"is the largest")

x = int(input("enter the no. u want to search? "))
bst.search(x)

del_value=int(input("enter the key u want to delte."))
bst.delete(del_value)
print("after deletion the search tree becomes.. ",bst.inorder_walk())



