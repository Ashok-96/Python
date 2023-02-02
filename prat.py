class node:
    data=''
    next=None
    def __init__(self,data):
        self.data=data
        self.next=None

n1=node(1)
n2=node(2)
n3=node(3)

head=n1
head.next=n2
head.next.next=n3

while head !=None:
    print(head.data)
    head=head.next