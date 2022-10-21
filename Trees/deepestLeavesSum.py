'''
https://leetcode.com/problems/deepest-leaves-sum/
'''


def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
    '''

    A queue is created. A queue is a 2d array, each row is a level of the tree
    We'll append the all the children of the top level in the queue, and pop the top level.
    The last level remaining would consist of deepest leaves, we'll add those

    '''

    if root is None:
        return 0
    queue = [[root]]
    levelOrderTraversal = []

    while queue != []:
        newLevel = []
        for leaf in queue[0]:
            if leaf.left:
                newLevel.append(leaf.left)
            if leaf.right:
                newLevel.append(leaf.right)

        if newLevel != []:
            queue.append(newLevel)

        levelOrderTraversal.append([leaf.val for leaf in queue[0]])
        queue = queue[1:]

    return sum(levelOrderTraversal[-1])
