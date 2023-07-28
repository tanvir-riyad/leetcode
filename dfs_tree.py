class TreeNode:
    def __init__(self, value) :
        self.value = value
        self.right = None
        self.left = None

def max_depth(root):
    if root is None:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return max(left_depth, right_depth) + 1

root = TreeNode(1)
root.left = TreeNode(10)
root.right = TreeNode(15)
root.left.left = TreeNode(56)
root.left.right = TreeNode(12)

print(max_depth(root))