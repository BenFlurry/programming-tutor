from myBST import BST

class ColourNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.is_red = True


# left leaning red-black binary search tree
class LLRBBST(BST):
    def __init__(self):
        super().__init__()
        self.root = None

    def put(self, key, val):
        if self.root is None:
            self.root = ColourNode(key, val)
            self.root.is_red = False

        # standard traversal adding nodes to stack so we can backtrack balancing the tree
        stack = []
        node = self.root
        while True:
            stack.append(node)
            if key == node:
                node.val = val
                return

            if key < node.key:
                if node.left is None:
                    node.left = ColourNode(key, val)
                    break
                node = node.left

            elif key > node.key:
                if node.right is None:
                    node.right = ColourNode(key, val)
                    break
                node = node.right

        # backtrack up the tree balancing it
        while len(stack) > 0:
            node = stack.pop()
            # rotate left if right node is red and left is black
            if node.right.is_red and not node.left.is_red:
                node = self._left_rotation(node)
            # rotate right if 2 consecutive left nodes are red
            if node.left.is_red and node.left.left.is_red:
                node = self._right_rotation(node)
            # colour swap if we end up having a 3 node
            if node.left.is_red and node.right.is_red:
                node = self._colour_flip(node)


    def _left_rotation(self, node):
        next = node.right
        node.right = next.left
        next.left = node
        next.is_red = node.is_red
        node.is_red = True
        return next

    def _right_rotation(self, node):
        next = node.left
        node.left = next.right
        next.right = node
        next.is_red = node.is_red
        node.is_red = True
        return next

    def _colour_flip(self, node):
        node.left.is_red = False
        node.right.is_red = False
        node.is_red = True
        return node




