class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __eq__(self, other):
        if isinstance(other, ListNode):
            return self.val == other.val and self.next == other.next
        else:
            return False


if __name__ == "__main__":
    headA = ListNode(10)
    headB = ListNode(10)
    print("""
    headA = ListNode(10)
    headB = ListNode(10)
    """)
    print(f"headA == headB ? {headA == headB}")
    print(f"id(headA) = {id(headA)}")
    print(f"id(headB) = {id(headB)}")
