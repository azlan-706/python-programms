class TreeNode:
    """Binary Tree Node"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DoublyLinkedListNode:
    """Doubly Linked List Node"""
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BinaryTreeToDLL:
    def __init__(self):
        self.head = None  # Head of DLL
        self.prev = None  # Previous node in DLL
    
    def convert(self, root):
        """Converts a binary tree to a doubly linked list using in-order traversal."""
        if not root:
            return None
        
        # Recursively convert left subtree
        self.convert(root.left)

        # Process the current node
        if self.prev is None:
            self.head = root  # First node becomes head of DLL
        else:
            root.left = self.prev
            self.prev.right = root
        
        self.prev = root  # Move prev to current node

        # Recursively convert right subtree
        self.convert(root.right)

        return self.head  # Return head of DLL
    
    def print_dll(self, head):
        """Prints the doubly linked list from left to right."""
        curr = head
        while curr:
            print(curr.val, end=" <-> ")
            curr = curr.right
        print("None")

# Example Usage
if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    converter = BinaryTreeToDLL()
    head = converter.convert(root)
    converter.print_dll(head)  # Expected Output: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> None
