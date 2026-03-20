class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

# link
n1.next = n2
n2.next = n3
n3.next = n4

# insert beginning
new_node = Node(5)
new_node.next = n1
n1 = new_node

# traverse
current = n1
while current:
    print(current.data)
    current = current.next