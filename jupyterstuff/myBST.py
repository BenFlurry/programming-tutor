class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def _key_traverse(self, node, level=0):
        if node is not None:
            self._key_traverse(node.right, level+1)
            print(' ' * 4 * level + '->', node.key)
            self._key_traverse(node.left, level+1)

    def _val_traverse(self, node, level=0):
        if node is not None:
            self._val_traverse(node.right, level+1)
            print(' ' * 4 * level + '->', node.value)
            self._val_traverse(node.left, level+1)

    def print_keys(self):
        if self.root is None:
            print("")
            return

        self._key_traverse(self.root)

    def print_values(self):
        if self.root is None:
            print("")
            return

        self._val_traverse(self.root, 0)


    def is_empty(self):
        if self.root is None:
            return None

    def put(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            return

        current = self.root
        while True:
            if current is None:
                print('issue')

            if current.key == key:
                current.value = value
                break

            if key < current.key:
                if current.left is None:
                    current.left = Node(key, value)
                    break

                current = current.left

            elif key > current.key:
                if current.right is None:
                    current.right = Node(key, value)
                    break

                current = current.right

    def get(self, key):
        if self.root is None:
            return None

        current = self.root
        while True:
            if current.key is None:
                return None

            if current.key == key:
                return current.value

            if key < current.key:
                current = current.left

            elif key > current.key:
                current = current.right

    # edgecase for when tree > val
    def floor(self, val):
        if self.root is None:
            return None

        tmpval = None

        current = self.root
        while True:
            if current.key == val:
                return current.key

            if current.key < val:
                if current.right is None:
                    return current.key

                tmpval = current.key
                current = current.right

            if current.key > val:
                if current.left is None:
                    if tmpval is None:
                        return None
                    return tmpval

                current = current.left

    def ceiling(self, val):
        if self.root is None:
            return None

        tmpval = None

        current = self.root
        while True:
            if current.key == val:
                return current.key

            if current.key > val:
                if current.left is None:
                    return current.key

                tmpval = current.key
                current = current.left

            if current.key < val:
                if current.right is None:
                    if tmpval is None:
                        return None
                    return tmpval

                current = current.right

    def maximum(self):
        if self.root is None:
            return None

        current = self.root
        while True:
            if current.right is None:
                return current.key
            current = current.right

    def minimum(self):
        if self.root is None:
            return None

        current = self.root
        while True:
            if current.left is None:
                return current.key
            current = current.left

    def to_list(self):
        if self.root is None:
            return None
        root = self.root
        self.traversed = []
        self.inorder_traverse(root)
        return self.traversed

    def inorder_traverse(self, root):
        if root:
            self.inorder_traverse(root.left)
            self.traversed.append(root.key)
            self.inorder_traverse(root.right)

    def delete(self, key):
        if self.root is None:
            return None

        current = self.root
        parent = current
        while True:
            if current is None:
                return

            if key == current.key:
                break

            if key < current.key:
                parent = current
                current = current.left

            elif key > current.key:
                parent = current
                current = current.right

        # if there is no child nodes from the deleted node
        if current.left is None and current.right is None:
            if current == self.root:
                self.root = None
            elif parent.left is current:
                parent.left = None
            else:
                parent.right = None

        # if there is a left node but no right node
        elif current.right is None:
            if current == self.root:
                self.root = current.left
            elif parent.left == current:
                parent.left = current.right
            elif parent.right == current:
                parent.right = current.right

        elif current.left is None:
            if current == self.root:
                self.root = current.right
            elif parent.left == current:
                parent.left = current.right
            elif parent.right == current:
                parent.right = current.right

        else:
            next = current.right
            while next.left is not None:
                next = next.left

            if parent.left == current:
                parent.left = next

            current.val = next.val
            self.delete(next.val)

b = BST()
arr = [(3,'a'), (2,'c'), (3.5,'z'), (3.25, 'j'), (2.5,'l')]
for key, value in arr:
    b.put(key, value)

for key, _ in arr:
    print(b.get(key))

print(b.maximum())
print(b.minimum())
print(b.ceiling(-1000))
print(b.to_list())
b.print_keys()
b.print_values()