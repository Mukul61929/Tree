class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_subtrees_with_sum(root, x):
    if root is None:
        return 0

    # Recursive function to check the sum of the subtree rooted at a node
    def is_sum_subtree(node, target_sum):
        if node is None:
            return 0

        left_sum = is_sum_subtree(node.left, target_sum)
        right_sum = is_sum_subtree(node.right, target_sum)

        current_sum = node.value + left_sum + right_sum

        if current_sum == target_sum:
            # If the subtree sum equals x, increment the count
            return 1

        return 0

    # Recursive traversal of the tree
    left_count = count_subtrees_with_sum(root.left, x)
    right_count = count_subtrees_with_sum(root.right, x)

    # Check if the subtree rooted at the current node sums up to x
    current_count = is_sum_subtree(root, x)

    # Return the total count
    return left_count + right_count + current_count

# Construct a binary tree
#        5
#       / \
#      3   1
#     / \ / \
#    4  2 6  7
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Set the target sum
target_sum = 5

# Count the number of subtrees with sum equal to the target sum
result = count_subtrees_with_sum(root, target_sum)
print("Number of subtrees with sum equal to", target_sum, ":", result)
