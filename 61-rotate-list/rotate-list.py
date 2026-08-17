
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head

       
        length = 1
        tail = head
        while tail.next:
            tail = tail.next   
            length += 1

        tail.next = head

        k = k % length
        steps_to_new_head = length - k

        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

   
        new_tail.next = None

        return new_head



def build_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


s = Solution()

head = build_list([1,2,3,4,5])
print(print_list(s.rotateRight(head, 2)))  

head = build_list([0,1,2])
print(print_list(s.rotateRight(head, 4)))  
