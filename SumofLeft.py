class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_of_left_leaves(root, is_left=False):
    if root is None:
        return 0

    if root.left is None and root.right is None and is_left:
        # If the node is a left leaf, return its value
        return root.value

    # Recursively calculate the sum for left and right subtrees
    left_sum = sum_of_left_leaves(root.left, True)
    right_sum = sum_of_left_leaves(root.right, False)

    return left_sum + right_sum

# Construct a binary tree
#        3
#       / \
#      9  20
#         / \
#        15  7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Calculate the sum of left leaves in the binary tree
result = sum_of_left_leaves(root)
print("Sum of left leaves:", result)
