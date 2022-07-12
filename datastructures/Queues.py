# import requests
# import mysql.connector
# import pandas as pd

#array implementation:
#array implementation:
#array implementation:

class Queue():
    #constructor
    def __init__(self,queue=[]):
        self.queue=queue
    
    #adding an element to the queue:
    
    def enqueue(self,item):
        self.queue.append(item)
    
    #delete the first element
    
    def dequeue(self):
        if self.queue:
            for i in range(len(self.queue)-1):
                self.queue[i]=self.queue[i+1]
            del self.queue[-1]
        else:
            print ("Queue empty, nothing to dequeue!")
    
    #check if queue is empty:
    def is_empty(self):
        return self.queue==[]
    
    #returning the hed of the queue without removing it:
    def peek(self):
        if self.queue:
            return self.queue[-1]
        else:
            print ("Queue Empty!")
    
    #displaying the queue:
    
    def display(self):
        if self.queue:
            for i in range(len(self.queue)-1,-1,-1):
                print("(",self.queue[i],")",end=" ")
            print()
        else:
            print ("Queue Empty!")
            
#Linked list implementation:
#Linked list implementation:
#Linked list implementation:
#Linked list implementation:

#class node:
class Node():
    def __init__(self,data=0):
        self.data=data
        self.next=None
    
class ListQueue():
    def __init__(self,top=None):
        self.top=top
    
    def is_empty(self):
        return self.top==None
    def enqueue(self,item):
        if self.top:
            item.next=self.top
            self.top=item
        else:
            self.top=item
    def dequeue(self):
        if not self.top.next:
            self.top=None
        elif self.top:
            current=self.top
            while current.next.next:
                current=current.next
            current.next=None
        else:
            print ("Empty Queue!")
    
    def peek(self):
        if self.top:
            return self.top.data
        print ("Queue Empty!")
    
    def display(self):
        if self.top:
            current=self.top
            while current:
                print ("(",current.data,")",end=" ")
                current=current.next
            print()
        else:
            print ("Queue Empty!")


##test array implementation:
q=Queue([1])
q.display()
print(q.peek())
print(q.is_empty())
print("adding 5 to the queue :")
q.enqueue(5)
q.display()
print("deleting the head of the queue:")
q.dequeue()
q.dequeue()
q.display()

##test linked list implementation :
N=Node(5)
N1=Node(4)
N2=Node(3)
Q=ListQueue(N)
print(Q.is_empty())

Q.enqueue(N1)
Q.enqueue(N2)
Q.display()
print(Q.peek())
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.display()
N3=Node()
Q.enqueue(N3)
Q.display()



