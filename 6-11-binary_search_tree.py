class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            self.size += 1
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
                self.size += 1
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
                self.size += 1
            else:
                self._insert(value, cur_node.right_child)
        else:
            print(f'There is already a node with the value of {value}')

    def build_tree(self, num_nodes=50, max_val=1000):
        from random import randint
        for num in range(num_nodes):
            new_node = randint(0, max_val)
            self.insert(new_node)

    def print_tree(self, traversal_order='inorder'):
        if self.root == None:
            print(f'There is no root of this tree')
        elif traversal_order == 'preorder':
            print('Printing Pre-Order Traversal...')
            self._print_tree_preorder(self.root)
        elif traversal_order == 'inorder':
            print('Printing In-Order Traversal...')
            self._print_tree_inorder(self.root)
        elif traversal_order == 'postorder':
            print('Printing Post-Order Traversal...')
            self._print_tree_postorder(self.root)

    def _print_tree_preorder(self, cur_node):
        if cur_node != None:
            print(cur_node.value)
            self._print_tree_preorder(cur_node.left_child)
            self._print_tree_preorder(cur_node.right_child)

    def _print_tree_inorder(self, cur_node):
        if cur_node != None:
            self._print_tree_inorder(cur_node.left_child)
            print(cur_node.value)
            self._print_tree_inorder(cur_node.right_child)

    def _print_tree_postorder(self, cur_node):
        if cur_node != None:
            self._print_tree_postorder(cur_node.left_child)
            self._print_tree_postorder(cur_node.right_child)
            print(cur_node.value)

    def height(self):
        if self.root == None:
            return 0
        else:
            return self._height(self.root, 0)

    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        else:
            left_height = self._height(cur_node.left_child, cur_height + 1)
            right_height = self._height(cur_node.right_child, cur_height + 1)
            return max(left_height, right_height)

    def search(self, search_value):

    def _search(self, search_value, cur_node):
        






tree = BST()
tree.build_tree()
tree.print_tree()
tree.print_tree('preorder')
tree.print_tree('postorder')
print(f'Tree height: {tree.height()}')
print(tree.size)
