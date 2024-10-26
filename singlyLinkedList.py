class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# function to traverse the singly linked list
def traverse(head):
    current=head
    pos=1
    while current is not None:
        print("pos-",pos," -> ",current.data)
        pos+=1
        current=current.next
    print ('secondLast')

def search(head,data):
    while head is not None:
        if head.data==data:
            return True
        head=head.next
    return False

def findLength(head):
    length=0
    while head is not None:
        length+=1
        head=head.next
    return(length)

# function to insert at the beginning of the SLL
def insertAtbeginning(head,value):
    newNode=Node(value)
    newNode.next=head
    return newNode

def insertAtEnd(head,value):
    newNode=Node(value)
    while head.next is not None:
        head=head.next
    head.next=newNode

def insertAtPositon(head,value,pos):
    if pos<1:
        print("invalid positon[1]")
        return head
    if pos==1:
        newNode=Node(value)
        newNode.next=head
        return newNode
    prev=head
    count=1
    while count<pos-1 and prev is not None:
        prev=prev.next
        count+=1
    if prev == None:
        print("invalid postion [2]")
        return head
    newNode=Node(value)
    newNode.next=prev.next
    prev.next=newNode
    return head

def deleteAtBeginning(head):
    return (head.next)

def deleteAtEnd(head):
    if head==None:
        return None
    if head.next==None:
        head=None
        return None
        
    secondLast=head
    while secondLast.next.next is not None:
        secondLast=secondLast.next
    secondLast.next=None
    return head

def deleteAtPos(head,pos):
    if pos<1:
        print("invalid postion[1]")
    prev=head
    count=1
    while count<pos-1 and prev is not None:
        prev=prev.next
        count+=1
    if prev==None:
        print("invalid postion[2]")
    prev.next=prev.next.next

    return(head)



head=None

head=insertAtbeginning(head,1)
head=insertAtbeginning(head,2)
head=insertAtbeginning(head,3)
head=insertAtbeginning(head,4)
traverse(head)
# print("serch:",search(head,1))
# print("length:",findLength(head))
# insertAtEnd(head,5)
# insertAtEnd(head,6)
# traverse(head)
# print("length:",findLength(head))
# head=insertAtPositon(head,10,3)
# head=deleteAtBeginning(head)
# head=deleteAtEnd(head)
# head=deleteAtEnd(head)
head=deleteAtPos(head,3)
traverse(head)
