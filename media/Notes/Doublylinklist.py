class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinklist:
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
            NewNode.prev = self.tail
            self.tail = NewNode

    def display(self):
        temp = self.head
        while(temp != None):
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def reverse(self):
        previous = None
        current = self.head
        while(current is not None):
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.head = temp.prev


Dllist = DoublyLinklist()
n = int(input("Enter the length of Linklist:-"))
for i in range(n):
    Dllist.addNode(int(input()))

Dllist.display()
Dllist.reverse()
Dllist.display()
