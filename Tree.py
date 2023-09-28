from treePrint import *
class Node:
    def __init__(self, val):
        self.val = val
        self.r = None
        self.l = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def add(self, val):
        if(self.size):
            curr = self.root
            prev = self.root
            while(curr != None):
                prev = curr
                if val > curr.val:
                    curr = curr.r
                else:
                    curr = curr.l
            if(val >= prev.val):
                prev.r = Node(val)
            else:
                prev.l = Node(val)
        else:
            self.root = Node(val)
        self.size = self.size + 1
    def __find(self, val) -> (Node | None, Node | None):
        if(self.size):
            curr = self.root
            prev = None
            while(curr and curr.val != val):
                prev = curr
                if(curr.val < val):
                    curr = curr.r
                else: curr = curr.l

            return (curr, prev)

    def __findChild(self, toDelete):
        if(toDelete.l and toDelete.r):
            curr = toDelete.l
            while(curr.r):
                curr = curr.r
            curr.r = toDelete.r
            return toDelete.l
        elif(toDelete.l):
            return toDelete.l
        elif(toDelete.r):
            return toDelete.r
        else:
            return None

    def delete(self,val):
        if(self.size):
            toDelete, parent = self.__find(val)
            if(toDelete and parent):
                if(toDelete.val > parent.val):
                    parent.r = self.__findChild(toDelete)
                else:
                    parent.l = self.__findChild(toDelete)
                self.size = self.size -1
            elif(toDelete):
                r = self.root.r
                self.root = self.root.l
                self.root.r = r
                self.size = self.size - 1
            else: print("value not found")









    #Depth First Search or DFS
    #Inorder Traversal # LEFT ROOT RIGHT
    def inorder(self):
        if(self.size):
            root = self.root
            self.__inorder_traverse(root)
            print()
    def __inorder_traverse(self,root):
        if(root):
            self.__inorder_traverse(root.l)
            print(root.val, end=" ")
            self.__inorder_traverse(root.r)
    def preorder(self):
        if(self.size):
            root = self.root
            self.__preorder_traverse(root)
            print()
    def __preorder_traverse(self, root):
        if(root):
            print(root.val, end = " ")
            self.__preorder_traverse(root.l)
            self.__preorder_traverse(root.r)
    #Postorder Traversal
    #Do left child, right child, then finall print
    def postorder(self):
        if(self.size):
            root = self.root
            self.__postorder_traverse(root)
            print()
    def __postorder_traverse(self, root):
        if(root):
            self.__postorder_traverse(root.l)
            self.__postorder_traverse(root.r)
            print(root.val, end = " ")



myTree = BinaryTree()

myTree.add(5)
myTree.add(3)
myTree.add(4)
myTree.add(1)
myTree.add(9)
myTree.add(7)
myTree.add(8)
myTree.add(6)
myTree.add(10)
myTree.delete(4)
myTree.delete(3)

print2D(myTree.root)
myTree.inorder()
myTree.preorder()
myTree.postorder()