class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height_of_tree(root):
    if root is None:
        return 0
    return 1 + max(height_of_tree(root.left), height_of_tree(root.right))

def sum_of_perfect_binary_tree(root):
    height = height_of_tree(root)
    return 2**(height + 1) - 1


# Construct a perfect binary tree with three levels
#        1
#       / \
#      2   3
#     / \ / \
#    4  5 6  7
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Calculate the sum of all nodes in the perfect binary tree
result = sum_of_perfect_binary_tree(root)
print("Sum of all nodes in the perfect binary tree:", result)
