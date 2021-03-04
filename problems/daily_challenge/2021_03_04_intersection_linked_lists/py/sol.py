class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    if headA == None and headB == None:
        return None
    def length(head):
        current = head
        l = 0
        while current != None:
            l += 1
            current = current.next
        return l
    def nth(head, n):
        current = head
        for _ in range(n):
            current = current.next
        return current
    intersectionNode = None
    # I'd like to run from the tail of the singly linked list.
    lenA = length(headA)
    lenB = length(headB)
    #currentA = nth(headA, lenA-1)
    #currentB = nth(headB, lenB-1)
    indA = lenA - 1
    indB = lenB - 1
    commonNode = None
    currentA = nth(headA, indA)
    currentB = nth(headB, indB)
    #while currentA == currentB:
    while currentA.val == currentB.val:
        commonNode = currentA
        indA -= 1
        indB -= 1
        currentA = nth(headA, indA)
        currentB = nth(headB, indB)
    return commonNode

def construction(L):
    if len(L) == 0:
        head = 
    head = ListNode(L[0])

def testcase(k, listA, listB):

if __name__ == "__main__":
