class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def merge_sort(head):
    if head is None or head.next is None:
        return head

    # Split the linked list into two halves
    middle = find_middle(head)
    left_half = head
    right_half = middle.next
    middle.next = None

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    sorted_list = merge(left_half, right_half)
    return sorted_list

def find_middle(head):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    dummy = ListNode(0)
    current = dummy

    while left is not None and right is not None:
        if left.value < right.value:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next

    if left is not None:
        current.next = left
    if right is not None:
        current.next = right

    return dummy.next

# Example usage:
# Create a linked list
head = ListNode(3)
head.next = ListNode(1)
head.next.next = ListNode(4)
head.next.next.next = ListNode(2)

# Perform merge sort
sorted_head = merge_sort(head)

# Print the sorted linked list
current = sorted_head
while current is not None:
    print(current.value, end=" ")
    current = current.next
