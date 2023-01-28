class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.headval=None
    def display(self):
        n=self.headval
        while n is not None:
            print(n.data)
            n=n.next
list1=linkedlist()

n1=Node(1)
n2=Node(2)
list1.headval=n1
list1.headval.next=n2
list1.display()