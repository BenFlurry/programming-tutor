class Node:
    def __init__(self, key):
        pass

class RedBlackTree:
    def __init__(self):
        pass

    def is_red(self, node):
        """
        Returns true if a node is red, or none

        Arguments:
            node (Node): The node to check

        Returns:
            bool: True if the node is red, False otherwise
        """

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
        pass

    def flip_colors(self, node):
        """
        Flip the colors of the node and its children

        Arguments:
            node (Node): The node to flip

        Returns:
            None
        """
        pass

    def insert(self, key, value):
        """
        Public method to insert a key-value pair

        Arguments:
            key (int): The key to insert
            value (any): The value to insert

        Returns:
            None
        """
        pass

    def _insert(self, node, key, value):
        """
        Traverse the tree to find the correct place to insert the new node
        Call fix_violations to fix any violations

        Arguments:
            node (Node): The root of the subtree to insert into
            key (int): The key to insert
            value (any): The value to insert

        Returns:
            Node: The new root of the subtree
        """
        pass

    def fix_violations(self, node):
        """
        Rotate left if right child is red and left is black (left leaning)
        Rotate right if 2 consecutive left red nodes
        Colour flip if both children are red

        Arguments:
            node (Node): The root of the subtree to fix

        Returns:
            Node: The new root of the subtree
        """
        pass


