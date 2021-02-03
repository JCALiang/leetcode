


    def deleteDuplicates(head):
        if not head:
            return head
        
        result = cur = head
        
        while head and head.next:
            
            while cur and (cur.val == head.val):
                cur =cur.next

            head.next = cur
            head = head.next
           
            
        return result
            
            