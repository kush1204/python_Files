class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def Insertatbegin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_after(self,prev,new_data):
        if prev is None:
            print("given node must be present in the linked list")
            return
        new_node=Node(new_data)
        new_node.next=prev.next
        prev.next=new_node

    def append(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

if __name__=='__main__':
    ll=LinkedList()
    ll.Insertatbegin(40)
    ll.Insertatbegin(50)
    ll.append(10)
    ll.insert_after(ll.head.next.next,80)
    ll.print()


