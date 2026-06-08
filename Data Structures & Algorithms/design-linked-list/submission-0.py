class ListNode(object):
    def __init__(self, val=0, next=None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.dummyRight = ListNode(0)
        self.dummyLeft = ListNode(0)
        self.dummyLeft.next = self.dummyRight
        self.dummyRight.prev = self.dummyLeft
    def get(self , index: int) -> int:
        cur = self.dummyLeft.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.dummyRight and index == 0:
            return cur.val
        return -1
    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.dummyLeft.next, self.dummyLeft
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
    def addAtTail(self, val: int) -> None:
        node , next , prev = ListNode(val) , self.dummyRight, self.dummyRight.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.dummyLeft.next
        while cur and index > 0:
            cur = cur.next
            index -=1
        if cur and index == 0:
            node , next , prev = ListNode(val) , cur, cur.prev
            next.prev = node
            prev.next = node
            node.prev = prev
            node.next= next

    def deleteAtIndex(self, index: int) -> None:
        cur = self.dummyLeft.next
        while cur and index != 0:
            cur = cur.next
            index -=1
        if cur and cur != self.dummyRight and index == 0:
            next , prev = cur.next , cur.prev
            next.prev = prev
            prev.next = next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)