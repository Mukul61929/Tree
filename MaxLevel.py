from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_level_sum(root):
    if root is None:
        return 0

    max_sum = float('-inf')
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_sum = 0

        for _ in range(level_size):
            node = queue.popleft()
            current_sum += node.value

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        max_sum = max(max_sum, current_sum)

    return max_sum

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

# Find the maximum level sum in the binary tree
result = max_level_sum(root)
print("Maximum level sum in the binary tree:", result)
