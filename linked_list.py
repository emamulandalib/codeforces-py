class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = node

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            p = None
            n = self.head
            while n is not None and n.data != data:
                p = n
                n = n.next
            p.next = n.next if n else None


    def view(self):
        res = []
        n = self.head
        while n is not None:
            res.append(n.data)
            n = n.next
        return res

ll = LinkedList()
ll.insert(1)
ll.insert(1)
ll.insert(10)
ll.insert(5)

ll.delete(1)
ll.delete(4)
ll.delete(5)

ll.insert(6)

print(ll.view())
