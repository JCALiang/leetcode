
def deleteDuplicates( head):
    if not head or not head.next:
        return head
    
    
    sentinel = ListNode(0, head)
    pred = sentinel

    
    
    while head:
        if(head and head.next and (head.val == head.next.val)):
            while head and head.next and (head.val == head.next.val):
                head = head.next
            pred.next = head.next
        else:
            pred = pred.next
            

        head = head.next
            
    return sentinel.next