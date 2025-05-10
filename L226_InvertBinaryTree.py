# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left,root.right = root.right,root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        #Time Complexity (DFS) O(n)
        #Space Complexity O(h) as Call Stack opens for left nodes of tree downwards
        #iterations = height of tree = h