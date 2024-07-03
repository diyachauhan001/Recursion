class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sorted_lists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    if l1.data < l2.data:
        l1.next = merge_sorted_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_sorted_lists(l1, l2.next)
        return l2

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

l1 = Node(1)
l1.next = Node(3)
l1.next.next = Node(5)

l2 = Node(2)
l2.next = Node(4)
l2.next.next = Node(6)

print("List 1:")
print_list(l1)

print("List 2:")
print_list(l2)

merged_head = merge_sorted_lists(l1, l2)

print("Merged List:")
print_list(merged_head)
