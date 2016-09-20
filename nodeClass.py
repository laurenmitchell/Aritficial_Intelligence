class Node:
  def __init__(self,value, left, right, parent):
     self.value = value
     self.leftChild = left
     self.rightChild = right
     self.parent = parent
  
  def getChildren(self):
     children = []
     children.append(self.leftChild)
     children.append(self.rightChild)
     return children
  
     