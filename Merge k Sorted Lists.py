class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            lists.append(self.merge(lists.pop(0),lists.pop(0)))   
        return lists[0]
        
    def merge(self,l1,l2):
        node = ListNode()
        ret = node

        while l1 and l2:
            if l1.val > l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return ret.next
