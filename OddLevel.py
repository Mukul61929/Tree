class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_nodes_at_odd_levels(root, level=1):
    if root is not None:
        if level % 2 != 0:
            # If the current level is odd, print the node's value
            print(root.value, end=" ")

        # Recursively traverse the left and right subtrees
        print_nodes_at_odd_levels(root.left, level + 1)
        print_nodes_at_odd_levels(root.right, level + 1)

# Construct a binary tree
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

# Print nodes at odd levels in the binary tree
print("Nodes at odd levels:")
print_nodes_at_odd_levels(root)
