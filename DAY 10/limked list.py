class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None

n1=Node(5)
sll=SLL()
sll.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3