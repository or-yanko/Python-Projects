from itertools import (chain, repeat, starmap)
from operator import (add)
from unicodedata import name

class Structer:
  def __init__(self, id, name):
      self.id = id
      self.name = name


class BinaryTreeNode:
  def __init__(self, id, name='None'):
    self.data = Structer(id,name)
    self.leftChild = None
    self.rightChild=None
     
def insert(root,newID, newName):
    #if binary search tree is empty, make a new node and declare it as root
    if root is None:
        root=BinaryTreeNode(newID, newName)
        return root
    #binary search tree is not empty, so we will insert it into the tree
    #if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newID<root.data.id:
        root.leftChild=insert(root.leftChild,newID, newName)
    else:
        #if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild=insert(root.rightChild,newID, newName)
    return root
 
def height(root):
    #if root is None return 0
        if root==None:
            return 0
        #find height of left subtree
        hleft=height(root.leftChild)
        #find the height of right subtree
        hright=height(root.rightChild)  
        #find max of hleft and hright, add 1 to it and return the value
        if hleft>hright:
            return hleft+1
        else:
            return hright+1
    

def printTree(node, level=0):
    if node != None:
        printTree(node.leftChild, level + 1)
        print(' ' * 6 * level + '->' , node.data.id, node.data.name)
        printTree(node.rightChild, level + 1)



root= insert(None,15, 'pap')
insert(root,25, 'ggg')
insert(root,6, 'dudi')
insert(root,14, 'mos')
insert(root,20, 'avi')
insert(root,60, 'dor')
insert(root, 13, 'amy')

printTree(root)