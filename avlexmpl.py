if __name__ == "__main__":
    avl = AVLTree()
    root = None

    # Inserting nodes
    values = [10, 20, 30, 40, 50, 25]
    for val in values:
        root = avl.insert(root, val)

    print("Inorder Traversal (Sorted):")
    avl.inorder_traversal(root)  # Output: 10 20 25 30 40 50

