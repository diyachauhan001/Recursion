class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(node):
    if node is None or node.next is None:
        return node
    
    rest = reverse_linked_list(node.next)
    
    node.next.next = node
    node.next = None
    
    return rest

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original List:")
print_list(head)

reversed_head = reverse_linked_list(head)

print("Reversed List:")
print_list(reversed_head)
