class BinarySearchTree:
    def __init__(self):
        self._size=0
        self._root=None

    class _BSTNode:
        def __init__(self,key,value):
            self.key=key
            self.value=value
            self.left=None
            self.right=None
            self.parent=None

    def add(self,key,value):
            z=self._BSTNode(key,value)
            y=None
            x=self._root
            while(x!=None):
                y=x
                if(key<x.key):
                    x=x.left
                else:
                    x=x.right
            z.parent=y
            if(y==None):
                self._root=z
            elif(z.key<y.key):
                y.left=z
            else:
                y.right=z
            self._size+=1

    def is_empty(self):
            return self._size==0
    def size(self):
            return self._size    
    def inorder_walk(self):
            nodes=[]
            self._inorder_walk(self._root,nodes)
            return nodes
    def _inorder_walk(self,subtree,nodes):
            if subtree:
                self._inorder_walk(subtree.left,nodes)
                nodes.append(subtree.key)
                self._inorder_walk(subtree.right,nodes)

    def preorder_walk(self):
        nodes=[]
        self._preorder_walk(self._root,nodes)
        return nodes
    def _preorder_walk(self,subtree,nodes):
        if subtree:
            nodes.append(subtree.key)
            self._preorder_walk(subtree.left,nodes)            
            self._preorder_walk(subtree.right,nodes)
    def postorder_walk(self):
        nodes=[]
        self._postorder_walk(self._root,nodes)
        return nodes
    def _postorder_walk(self,subtree,nodes):
        if subtree:
            self._postorder_walk(subtree.left,nodes)            
            self._postorder_walk(subtree.right,nodes)
            nodes.append(subtree.key)

    def search(self,key):
        if self._root !=None:
            return self._searchloop(self._root,key)
        
    def _searchloop(self,node,key):
            if node.key==key:
                print(key,'is in the tree')
            elif node.key<key:
                if node.right!=None:
                    self._searchloop(node.right,key)
                else:
                    print(key, 'is not in the tree')
            else:
                if node.left!=None:
                    self._searchloop(node.left,key)
                else:
                    print(key, 'is not in the tree')

    def smallest(self):
        if self._root !=None:
            return self._smallestloop(self._root)
    def _smallestloop(self,node):
        if node.left!=None:
            return self._smallestloop(node.left)
        return  node.key

    def largest(self):
        if self._root !=None:
            return self._largestloop(self._root)
    def _largestloop(self,node):
        if node.right!=None:
            return self._largestloop(node.right)
        return node.key

    def delete(self,key):
        if self._root !=None:
            return self._deleteloop(self._root,key)
    def _deleteloop(self,node,key):
        if node.key==key:
            if node.left==None and node.right==None:
                if node.parent.left==node:
                    node.parent.left=None
                else:
                    node.parent.right=None
            elif node.left==None:
                node.right.parent=node.parent
                if node.parent.left==node:
                    node.parent.left=node.right
                else:
                    node.parent.right=node.right
            elif node.right==None:
                node.left.parent=node.parent
                if node.parent.left==node:
                    node.parent.left=node.left
                else:
                    node.parent.right=node.left
            else:
                max_val =self._largestloop(node.left)
                node.key=max_val
                return self._deleteloop(node.left,max_val)
                    
        elif key<node.key:
            if node.left!=None:
                return self._deleteloop(node.left,key)
            else:
                print(key,'is not in the tree')
        else:
            if node.right!=None:
                return self._deleteloop(node.right,key)
            else:
                print(key,'is not in the tree')
                    
                    
                    
                
