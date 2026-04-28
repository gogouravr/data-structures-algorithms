# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_tree_balanced = True
        def height(node=root):
            nonlocal is_tree_balanced
            if node is None:
                return 0
            
            height_of_left_subtree = height(node.left)
            height_of_right_subtree = height(node.right)
            if abs(height_of_left_subtree-height_of_right_subtree) > 1:
                is_tree_balanced = False

            return 1 + max(height_of_left_subtree,height_of_right_subtree)

        height()
        return is_tree_balanced

        