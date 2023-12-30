class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, value):
        self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)
        else:
            print(f"Value {value} already exists in the tree.")

    def inorder_traversal(self, start_node=None):
        if start_node is None:
            start_node = self.root
        traversal = []
        if start_node.left:
            traversal += self.inorder_traversal(start_node.left)
        traversal.append(start_node.value)
        if start_node.right:
            traversal += self.inorder_traversal(start_node.right)
        return traversal


if __name__ == "__main__":
    root_value = int(input("Enter the root value of the binary tree: "))
    tree = BinaryTree(root_value)

    while True:
        value = input("Enter a value to insert into the tree (or 'exit' to stop): ")
        if value.lower() == 'exit':
            break
        try:
            value = int(value)
            tree.insert(value)
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'exit'.")

    print("Inorder Traversal:", tree.inorder_traversal())
