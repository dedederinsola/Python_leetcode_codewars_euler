#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        class Diameter:
            def __init__(self, diameter, height):
                self.diameter = diameter
                self.height = height
            
        def finddiameter(root: Optional[TreeNode]) -> Diameter:
            if not root:
                return Diameter(0, 0)
            
            leftData = finddiameter(root.left)
            rightData = finddiameter(root.right)

            currentDiameter = max(leftData.height + rightData.height, max(leftData.diameter, rightData.diameter))

            
            currentHeight = max(leftData.height, rightData.height) + 1

            return Diameter(currentDiameter, currentHeight)

        data = finddiameter(root)
        return data.diameter
        