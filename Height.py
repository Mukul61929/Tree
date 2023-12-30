class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_height(node):
    if node is None:
        return 0
    else:
        left_height = tree_height(node.left)
        right_height = tree_height(node.right)

        # Return the maximum of left and right subtree heights, plus 1 for the current node
        return max(left_height, right_height) + 1


if __name__ == "__main__":
    # Construct a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Calculate the height of the tree
    height = tree_height(root)

    print("Height of the tree:", height)
