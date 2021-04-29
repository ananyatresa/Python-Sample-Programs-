#linked List
#Class to create nodes
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

#class to link nodes
class LinkedList:
    def __init__(self):
        self.head=None #Initial Empty linked list

    def traversal_LL(self):
        if self.head is None:
            print ("Linked List is empty")
        else:
            n=self.head
            while n is not None:
                print (n.data, "-->", end=" ")
                n=n.ref
    
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    
    def reversal(self,temp):
        if temp:
            self.reversal(temp.ref)
            print (temp.data,"-->",end=" ")
        else:
            return 




LL1=LinkedList()
LL1.add_end(100)
LL1.add_end(200)
LL1.add_end(300)
LL1.add_end(400)
print ("Linked List:")
LL1.traversal_LL()
print (" ")
print ("Reverse Linked List:")
LL1.reversal(LL1.head)



