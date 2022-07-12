class Node(object):
    def __init__(self,data=0):
        self.prev=None
        self.next=None
        self.data=data
    def print_node(self):
        print("[data :",self.data,",previous :",self.prev,",next :",self.next,"]")
    
class LinkedList():
    def __init__(self,head=None):
        self.head=head
    
    def print_list(self):
        current=self.head
        while current!=None:
            current.print_node()
            current=current.next
    def insert_head(self,node):
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head.prev=node
            self.head=node
    def insert_tail(self,node):
        if self.head==None:
            self.head=None
        else:
            current=self.head
            while(current.next!=None):
                current=current.next
            node.prev=current
            current.next=node
    def find(self,val):
        if self.head==None:
            print(" head none :False")
        else:
            current=self.head
            while current!=None and current.data!=val:
                current=current.next
            if current==None:
                print("not found :False")
            elif current.data==val:
                print(" element found:True")
    def del_val(self,val):
        if self.head==None:
            print("Empty list, nothing to delete")
        elif self.head.data==val:
            self.head.next.prev=None
            self.head=self.head.next
        else:
            current=self.head
            while(current.next!=None and current.data!=val):
                current=current.next
            if current.next==None and current.data==val:
                current.prev.next=None
                
            elif current.data==val:
                (current.prev).next=current.next
                (current.next).prev=current.prev
            else:
                print("value not found in list, no items to delete")
                
                
####find method returns None which means none of the flows is executed, figure out why
            
            
            
            
            

node=Node(2)
node1=Node(1)
node2=Node(3)
node3=Node(5)
node4=Node(6)
# print("printing node")
# node.print_node()
# print("printing list before insert")
liste=LinkedList(node)

liste.insert_head(node1)
liste.insert_head(node3)
# liste.print_list()
liste.insert_tail(node2)
liste.insert_tail(node4)
# print("printing list after insert")
# liste.print_list()

# liste.find(3)
liste.del_val(6)
liste.print_list()

