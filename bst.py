class TreeNode:
    """Binary Search Tree Node"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTBalancer:
    def __init__(self):
        self.nodes = []  # Stores in-order traversal elements

    def store_inorder(self, root):
        """Stores in-order traversal of BST in an array."""
        if not root:
            return
        self.store_inorder(root.left)
        self.nodes.append(root)
        self.store_inorder(root.right)

    def build_balanced_bst(self, start, end):
        """Builds a balanced BST from the sorted array."""
        if start > end:
            return None

        mid = (start + end) // 2
        root = self.nodes[mid]  # Select middle element as root
        
        root.left = self.build_balanced_bst(start, mid - 1)  # Left subtree
        root.right = self.build_balanced_bst(mid + 1, end)  # Right subtree
        
        return root

    def balance_bst(self, root):
        """Main function to convert BST to balanced BST."""
        self.nodes = []  # Reset the list
        self.store_inorder(root)  # Store elements in sorted order
        return self.build_balanced_bst(0, len(self.nodes) - 1)  # Rebuild balanced BST

    def inorder_traversal(self, root):
        """Prints the in-order traversal of BST."""
        if not root:
            return
        self.inorder_traversal(root.left)
        print(root.val, end=" ")
        self.inorder_traversal(root.right)

# Example Usage
if __name__ == "__main__":
    # Creating an unbalanced BST
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)
    root.right = TreeNode(15)
    root.right.right = TreeNode(20)

    print("Original Inorder BST:")
    balancer = BSTBalancer()
    balancer.inorder_traversal(root)  # Expected: 1 2 5 10 15 20
    print("\n")

    balanced_root = balancer.balance_bst(root)

    print("Balanced BST Inorder:")
    balancer.inorder_traversal(balanced_root)  # Expected: 1 2 5 10 15 20
