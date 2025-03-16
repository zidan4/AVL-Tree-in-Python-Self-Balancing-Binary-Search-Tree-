
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    # Get the height of a node
    def get_height(self, node):
        return node.height if node else 0
    
    # Calculate balance factor
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Right rotation (for left-heavy trees)
    def rotate_right(self, node):
        new_root = node.left
        temp = new_root.right
        
        new_root.right = node
        node.left = temp
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        
        return new_root

    # Left rotation (for right-heavy trees)
    def rotate_left(self, node):
        new_root = node.right
        temp = new_root.left
        
        new_root.left = node
        node.right = temp
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        
        return new_root

    # Insert into the AVL Tree
    def insert(self, root, data):
        if not root:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        # Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Check balance factor
        balance = self.get_balance(root)

        # Left Heavy (Right Rotation)
        if balance > 1 and data < root.left.data:
            return self.rotate_right(root)
        
        # Right Heavy (Left Rotation)
        if balance < -1 and data > root.right.data:
            return self.rotate_left(root)
        
        # Left-Right Case
        if balance > 1 and data > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        
        # Right-Left Case
        if balance < -1 and data < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
        return root

    # Inorder Traversal (sorted output)
    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=" ")
            self.inorder_traversal(root.right)
