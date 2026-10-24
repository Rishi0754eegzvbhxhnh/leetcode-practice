class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # Check if leaf node
        if not root.left and not root.right:
            return targetSum == root.val

        return (
            self.hasPathSum(root.left, targetSum - root.val) or
            self.hasPathSum(root.right, targetSum - root.val)
        )