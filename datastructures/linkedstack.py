#implémentation de la classe stack utilisant les listes chainées:

class Node():
 def __init__(self,data=0):
  self.data=data
  self.next=None

class LinkedStack():
 def __init__(self,top=None):
  self.top=top
 
 def is_empty(self):
  return self.top==None
 
 
 def show(self):
  if self.is_empty():
   print("Stack empty, nothing to show")
  else:
   current=self.top
   while current:
    print("(",current.data,")",end=" ")
    current=current.next
   print()
   
 
  #in a linked list, we add and delete from the top
 def pop(self):
   if self.is_empty():
    print("Stack empty, nothing to pop")
   else:
    self.top=self.top.next
 def push(self,item):
  if self.is_empty():
   self.top=item
  else:
   item.next=self.top
   self.top=item
 def peek(self):
  if self.is_empty():
   print("Stack empty, nothing to ")
  else:
   return self.top.data

node=Node(2)
node1=Node(1)
S=LinkedStack()
S.push(node)
S.push(node1)
S.show()
S.pop()
S.show()
print(S.peek())
                                        

    