#Build Tree from Preorder Sequence
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.idx = -1
    def build_tree(self, nodes):
        self.idx += 1
        if nodes[self.idx] == -1:
            return None
        new_node = Node(nodes[self.idx])
        new_node.left = self.build_tree(nodes)
        new_node.right = self.build_tree(nodes)
        return new_node
nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
tree = BinaryTree()
root = tree.build_tree(nodes)
print(root.data)