class Solution:
    def isValidBST(self, root):
        def helper(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (helper(node.left, low, node.val) and
                    helper(node.right, node.val, high))
        
        return helper(root)
