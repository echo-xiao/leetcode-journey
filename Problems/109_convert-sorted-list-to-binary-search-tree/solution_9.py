
class Solution:
    # 你的逻辑修正版
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # 1. Base Case: 空链表或单个节点
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        # 2. 找中点 (利用快慢指针，同时记录 pre 指针用于断链)
        slow, fast = head, head
        prev = None # 关键变量
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # 【关键动作】：断链
        # 把链表从中间切断，head 只代表左半部分了
        if prev:
            prev.next = None
        
        # 3. 构造根节点 + 递归
        root = TreeNode(slow.val) # 注意：要创建新的 TreeNode，不能直接用 ListNode
        root.left = self.sortedListToBST(head)      # 递归左边
        root.right = self.sortedListToBST(slow.next) # 递归右边
        
        return root