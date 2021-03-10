class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linklist:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        NewNode = Node(data)
        if self.head == None:
            self.head = NewNode
            self.tail = NewNode
        else:
            self.tail.next = NewNode
            self.tail = NewNode

    def display(self):
        temp = self.head
        while(temp != None):
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


llist = linklist()
n = int(input('Enter the size of linklist:-'))
for i in range(n):
    llist.addNode(int(input()))

llist.display()

llist.reverse()
llist.display()
