""" 

https://leetcode.com/problems/path-sum/

"""


class Solution:

    def isLeaf(self, root):
        if root.left is None and root.right is None:
            return True
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        if root is None, re
        '''

        if root is None:
            return False

        if self.isLeaf(root):
            if targetSum == root.val:
                return True

            return False

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
