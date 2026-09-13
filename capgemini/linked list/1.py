#Reverse a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    current = head
    prev = None
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev

head = None
tail = None

n = int(input("How many index: "))
for i in range(n):
    data = int(input("Enter the value: "))
    new = Node(data)
    if head is None:
        head = new
        tail = new
    else:
        tail.next = new
        tail = new

current = head
print("Original: ")
while current:
    print(current.data,end="->")
    current = current.next
print("None")

head = reverse(head)

current = head

print("Reversed: ")
while current:
    print(current.data,end="->")
    current = current.next
print("None")