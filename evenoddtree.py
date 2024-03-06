# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True  # Make sure to use True instead of true
        
        queue = deque([(root, 0)])
        lastChecked = {}
        
        while queue:
            node, level = queue.popleft()
            isLevelEven = level % 2 == 0

            if (isLevelEven and node.val % 2 == 0) or (not isLevelEven and node.val % 2 == 1):
                return False
            
            if level in lastChecked:
                if (isLevelEven and lastChecked[level] >= node.val) or (not isLevelEven and lastChecked[level] <= node.val):
                    return False

            lastChecked[level] = node.val

            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))
        
        return True