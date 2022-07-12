#implementing list stacks:


#for the implementation of a stack using an array, we add and delete at the end of the stack, for complexity puposes:
class Stack():#creating class
 def __init__(self):#class constructor
  self.stack=[]
    
 def show(self):#showing the stack items
  if self.is_Empty():
   print("empty stack, nothing to show")
  else:
   for i in self.stack:
    print("(",i,")",end=" ")
   print
   
   
 def pop(self):
  if len(self.stack)!=0:
   self.stack.pop()
  return
 def push(self,element):
  self.stack.append(element)
 def peek(self):
  if len(self.stack)==0:
   print("stack is empty!")
  else:
   return self.stack[0]
 def is_Empty(self):
  return len(self.stack)==0
 def is_full(self):
  return len(self.stack)!=0
  
  
  
S= Stack()
print(S.is_Empty())
print(S.is_full())
S.push(5)
# S.push(6)
S.show()
S.pop()
S.show()
print(S.is_Empty())
print(S.is_full())

print(S.peek())
