#linked list basic
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        iterator = self.head
        linkedlist = ''
        while iterator:
            linkedlist += str(iterator.data) + '-->'
            iterator = iterator.next
        print(linkedlist)
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_start(5)
    ll.insert_at_start(89)
    ll.print()