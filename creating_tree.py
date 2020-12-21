class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_children(self, node):
        self.children.append(node)


class Tree:
    def __init__(self, node):
        self.node = node

    def traverse(self, node, level):
        if node:
            print(f"{'-'*level} {node.data}")
            for child in node.children:
                self.traverse(child, level+1)


ceo = TreeNode("CEO")
cto = TreeNode("CTO")
cfo = TreeNode("CFO")
cmo = TreeNode("CMO")
coo = TreeNode("COO")
sa = TreeNode("SA")

ceo.add_children(cto)
ceo.add_children(cfo)
ceo.add_children(cmo)
ceo.add_children(coo)
cto.add_children(sa)

tree = Tree(ceo)
tree.traverse(tree.node, 0)