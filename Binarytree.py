import sys

class Node:
    def __init__(self,value, left, right, parent):
        self.value = value
        self.l = left
        self.r = right
        self.p = parent
  
    def getChildren(self):
        children = []
        children.append(self.l)
        children.append(self.r)
        return children         
class Tree:
    def __init__(self, rootkey):
        self.root = Node(rootkey, None, None, None)
        #create a new tree while setting root
            
    def checkTree(self, value, parentValue, root):
        #Recursive function that searches through tree to find
        #if parentValue exists
        
        if root == None:
            #if there is no root in tree
            return False
        if root.value == parentValue:
            return root
        else:
            #add child in add()
            
           for child in root.getChildren():
                add_temp = self.checkTree(value, parentValue, child)
                if add_temp:
                    return add_temp
        
        
    #your code goes here
    def add(self,value,parentValue):
        parentValueNode = self.checkTree(value,parentValue,self.root)
        if parentValueNode == None:
            print "Parent not found."
        #step 1
        elif parentValueNode.l == None:
            newNode = Node(value, None, None, parentValueNode)
            parentValueNode.l = newNode
        elif parentValueNode.r == None:    
            newNode = Node(value, None, None, parentValueNode)
            parentValueNode.r = newNode
            
    
      #if parent already has left and right children, don't add node 
        else:
            print "Parent has two children, node not added."


    def findNodeDelete(self, value, root):
        if root == None:
            return False
        if value == root.value:
            if root.l == None and root.r == None:
                #print("Deleting Node", root.intkey)
                #update parent
                if root.p.l.value == value:
                    root.p.l = None
                elif root.p.r.value == value:
                    root.p.r = None
                root = None
                return True
            else:
                print "Node not deleted, has children"
                return False
        else:
            for child in root.getChildren():
                delete_node = self.findNodeDelete(value, child)
                if delete_node:
                    return delete_node
            
        
        
    def delete(self, value):
        if self.root == None:
            self.root = MyNode(value, None, None, None)
        if value == self.root.value:
            if self.root.l == None and self.root.r == None:
                #print("Deleting Root")
                self.root = None
                return True
            else:
                print "Node not deleted, has children"
                return False
        else:
            for child in self.root.getChildren():
                delete_node = self.findNodeDelete(value, child)
                if delete_node:
                    return delete_node
                    
        print "Node not found." 
        return False
        
    def printTree(self):
        if self.root != None:
            print self.root.value
            for child in self.root.getChildren():
                self.printBranch(child)
        else: 
            return
            
    
    def printBranch(self, root):
        if root == None:
            return
        else:
            print root.value
            for child in root.getChildren():
                self.printBranch(child)