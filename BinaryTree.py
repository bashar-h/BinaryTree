import math

class Node:
    def __init__ (self,value):
        self.value=value
        self.right=None
        self.left=None
    
    def _insert(self,index,limit,lst):
        level=int(math.log(index+1,2))
        left=2*index+1
        right=left+1
        if not lst[left] == None:
            self.left=Node(lst[left])
        if not lst[right] == None:
            self.right=Node(lst[right])
        if index<=limit:
            self.left._insert(left,limit,lst)
            self.right._insert(right,limit,lst)
 
class BinaryTree:
    def __init__ (self,root=None):
        self.root=Node(root)

    def preorder (self,start,traversal):
        if start:
            traversal+=str(start.value)+"-"
            traversal=self.preorder(start.left,traversal)
            traversal=self.preorder(start.right,traversal)
        return (traversal)
        
    def inorder (self,start,traversal):
        if start:
            traversal=self.inorder(start.left,traversal)
            traversal+=str(start.value)+"-"
            traversal=self.inorder(start.right,traversal)
        return (traversal)
        
    def postorder (self,start,traversal):
        if start:
            traversal=self.postorder(start.left,traversal)
            traversal=self.postorder(start.right,traversal)
            traversal+=str(start.value)+"-"
        return (traversal)
        
    def listToTree(self,lst):
        self.root=Node(lst[0])
        limit=math.log(len(lst),2)-2
        self.root._insert(0,limit,lst)
        

test=[3,9,20,None,None,15,7]
tree=BinaryTree()
tree.listToTree(test)
                

print("Inorder:",tree.inorder(tree.root,"")[:-1])
print("Preorder:",tree.preorder(tree.root,"")[:-1])
print("Postorder:",tree.postorder(tree.root,"")[:-1])
