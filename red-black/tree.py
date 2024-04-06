class Node:
    def __init__(self, key, value, color='RED'):
        self.key = key
        self.value = value
        self.color = color
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def is_red(self, node):
        # Treat None nodes as black.
        if node is None:
            return False
        return node.color == 'RED'

    def rotate_left(self, node):
        """
    |               |
   node             x
   / \       ->    / \
  nl  x          node xr
     / \         / \  
    xl  xr      nl xl


        Arguments:
            node (Node): The node to rotate around

        Returns:
            Node: The new root of the subtree
        """
        # Rotate left around the given node.
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = 'RED'
        return x

    def rotate_right(self, node):
        """
    |           |
   node         x
   / \         / \
  x  nr   ->  xl node
 / \             / \
xl xr           xr  nr

        Arguments:
            node (Node): The node to rotate around

        Returns:
            Node: The new root of the subtree
        """
        # Rotate right around the given node.
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = 'RED'
        return x

    def flip_colors(self, node):
        # Flip colors of the node and its children.
        node.color = 'RED' if node.color == 'BLACK' else 'BLACK'
        if node.left is not None:
            node.left.color = 'RED' if node.left.color == 'BLACK' else 'BLACK'
        if node.right is not None:
            node.right.color = 'RED' if node.right.color == 'BLACK' else 'BLACK'

    def insert(self, key, value):
        # Public method to insert a key-value pair.
        self.root = self._insert(self.root, key, value)
        self.root.color = 'BLACK'  # Keep the root always black.

    def _insert(self, node, key, value):
        # Base case: insert new node.
        if node is None:
            return Node(key, value, 'RED')

        # Recursive insert into the correct subtree.
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value  # Update value if key already exists.

        # Check and fix any violations from this point upwards.
        return self.fix_violations(node)


    def fix_violations(self, node):
        # Fix right-leaning red links.
        if not self.is_red(node.left) and self.is_red(node.right):
            node = self.rotate_left(node)

        # Fix two consecutive left-leaning red links.
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)

        # Flip colors if both children are red.
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        return node

    def delete(self, key):
        # Public method to delete a node with the given key.
        if self.root is None:
            return

        # Ensure that the root is always black.
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = 'RED'

        self.root = self._delete(self.root, key)
        if self.root is not None:
            self.root.color = 'BLACK'

    def _delete(self, node, key):
        # Base case: key not found.
        if node is None:
            return None

        if key < node.key:
            if not self.is_red(node.left) and not self.is_red(node.left.left):
                node = self.move_red_left(node)
            node.left = self._delete(node.left, key)
        else:
            if self.is_red(node.left):
                node = self.rotate_right(node)
            if key == node.key and node.right is None:
                return None
            if not self.is_red(node.right) and not self.is_red(node.right.left):
                node = self.move_red_right(node)
            if key == node.key:
                successor = self.get_min(node.right)
                node.key = successor.key
                node.value = successor.value
                node.right = self._delete_min(node.right)
            else:
                node.right = self._delete(node.right, key)

        return self.fix_violations(node)

    def move_red_left(self, node):
        # Move a red link to the left.
        self.flip_colors(node)
        if self.is_red(node.right.left):
            node.right = self.rotate_right(node.right)
            node = self.rotate_left(node)
            self.flip_colors(node)
        return node

    def move_red_right(self, node):
        # Move a red link to the right.
        self.flip_colors(node)
        if self.is_red(node.left.left):
            node = self.rotate_right(node)
            self.flip_colors(node)
        return node

    def get_min(self, node):
        # Get the minimum node in the subtree rooted at the given node.
        while node.left is not None:
            node = node.left
        return node

    def _delete_min(self, node):
        # Delete the minimum node in the subtree rooted at the given node.
        if node.left is None:
            return None

        if not self.is_red(node.left) and not self.is_red(node.left.left):
            node = self.move_red_left(node)

        node.left = self._delete_min(node.left)
        return self.fix_violations(node)
