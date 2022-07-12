

class binaryNode():
 def __init__(self,data=0):
  self.data=data
  self.left=None
  self.right=None
 
 def insert(self,value):
  #since this is a normal binary tree, we add in the first empty spot, left to right
  #which means that I will have to traverse the tree in order.
   #1- if self.left i none, I just insert in its left, else if the right is empty,
   #i insert in the right, else i recurse to left, then to right
   if self.left is None:
      self.left=binaryNode(value)
   elif self.right is None:
      self.right=binaryNode(value)
   elif self.left is not None:
      self.left.insert(value)
   else:
      self.right.insert(value)
    
    
    
    
    
    
    
    
    
    
 def in_display(self):
  if self:
     if self.left:
      self.left.in_display()
     
     print(self.data,end=" ")
     if self.right:
      self.right.in_display()
   

 def pre_display(self):
  if self.left:
   print(self.left.data)
   self.left.pre_display()
  if self.right:
   print(self.right.data)
   self.right.pre_display()
  

   
a=binaryNode(5)
a.insert(6)
a.insert(7)
a.insert(8)
a.insert(9)
a.insert(10)
a.in_display()
# a.pre_display()
 

 
 