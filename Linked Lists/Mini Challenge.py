class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(5)
n2 = Node(10)
n3 = Node(15)
n4 = Node(20)
new_node = Node(12)

# link
n1.next = n2
n2.next = n3
n3.next = n4

# insert 12 after 10
new_node.next = n2.next
n2.next = new_node

# traverse
current = n1
while current:
    print(current.data)
    current = current.next