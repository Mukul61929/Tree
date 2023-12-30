class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_leaves(root):
    if root is not None:
        if root.left is None and root.right is None:
            # If the node is a leaf, print its value
            print(root.value)
        else:
            # Recursively traverse the left and right subtrees
            print_leaves(root.left)
            print_leaves(root.right)

# Construct a simple binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Print leaves of the binary tree
print("Leaves of the binary tree:")
print_leaves(root)
