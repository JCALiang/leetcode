    def detectCycle(head):
        
        if not head:
            return None
        
        fast = head.next
        slow = head
        
        while fast != slow:
            if not fast or not fast.next:
                return None
        
            fast= fast.next.next
            slow= slow.next
     
            
        slow = slow.next
        while head != slow:
            head = head.next
            slow=slow.next
    
        return slow