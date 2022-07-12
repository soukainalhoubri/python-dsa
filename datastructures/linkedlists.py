#node object
class Node(object):
    
 def __init__(self,data=0):
  self.data=data
  self.next=None
 def afficher(self):
   print("Node :",self.data," next Node :",self.next)
   
#linked list
class LinkedList():
 def __init__(self,head=None):
  self.head=head
  
#add a node at the end:

 def add_last(self,node):
  current=self.head
  while(current.next!=None):
   current=current.next
  current.next=node


#add a node at the beginning:
 def add_start(self,node):
  node.next=self.head
  self.head=node
  
#printing the list elements:
 def afficher(self):
  current=self.head
  while(current!=None):
   current.afficher()
   current=current.next
   
#inserting a node at a certain index :
 def insert_index(self,node,index):
  if index==0 or self.head==None:
   print("adding at the beginning")
   self.add_start(node)
  else:
   i=1
   current=self.head
   while(current.next!=None and i!=index):
    current=current.next
    i+=1
   if(current.next==None):
    print("end reached, adding a the end")
    self.add_last(node)
    
   else:
    node.next=current.next
    current.next=node
    
#deleting the first element :
 def del_first(self):
  if self.head==None:
   print("List is empty, no items to delete")
  else:
   current=self.head
   self.head=self.head.next
   del current
   
#deleting the last élément :
 def del_last(self):
  if self.head==None:
   print("List is empty, no items to delete")
  else:
   current=self.head
   while(current.next.next!=None):
    current=current.next
   current.next=None
   
#deleting the element depending on index:

 def del_index(self,index):
  if self.head==None:
   print("List is empty, no items to delete")
  elif index==0:
   print("deleting the first element")
   self.del_first()
  else:
   i=1
   current=self.head
   while(current.next!=None and i!=index):
    current=current.next
    i+=1
   if current.next==None:
    print("end reached, deleting the last element")
    self.del_last()
   else:
    current.next=current.next.next
    
#deleting value:
 def del_val(self,val):
  if self.head==None:
   print("List is empty, no items to delete")
  elif val==self.head.data:
   self.del_first()
  else:
   current=self.head
   previous=current
   while(current!=None and current.data!=val):
    previous=current
    current=current.next
   if current==None:
    print("value not found in list")
   elif current.data==val:
    previous.next=current.next
    
#reversing the linked list:

 def reverse_list(self):
  if self.head==None or self.head.next==None:
   return
  else:
   current=self.head
   previous=None
   currentmov=current
   while(current.next!=None):
    currentmov=current
    current.next=previous
    previous=current
    current=currentmov.next
   self.head=previous
    
   
    
   

   
   
  
    
node= Node(5)
node1=Node(7)
node2=Node(4)
node3=Node(6)
node4=Node(8)
# node.afficher()

# print("step 1: creating the list")
liste=LinkedList(node)
# liste.afficher()
# print("adding at the end 7 & 8")
liste.add_last(node1)
liste.add_last(node4)
# liste.afficher()
# print("adding 4 at the beginning")
liste.add_start(node2)
# liste.afficher()
# print("adding 6 at index 2")
liste.insert_index(node3,2)
# liste.afficher()


# print("deleting the first element : 4")
# liste.del_first()
# print("deeting the element at index 0")
# liste.del_last()
# liste.del_index(4)
# liste.del_val(10)
liste.afficher()

  
 
        
    
    
        
        