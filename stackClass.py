class Stack:
    def __init__(self):
        self.items = []
    def push(self,numItem):
        #adding numItem to end of the array 
        self.items.append(numItem)
    def pop(self):
        #popping off the item in the array 
        if(len(self.items) > 0):
           return self.items.pop()
        else:   
            return "Stack empty."
  
    def checkSize(self): 
        #checking number of items in the array
        return len(self.items)
      
					 