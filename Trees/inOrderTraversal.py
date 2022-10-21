"""
https://leetcode.com/problems/binary-tree-preorder-traversal/
https://leetcode.com/problems/binary-tree-inorder-traversal/
https://leetcode.com/problems/binary-tree-postorder-traversal/

 """


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        return [root.val]+self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
