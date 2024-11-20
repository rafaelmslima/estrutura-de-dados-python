class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree():
    def __init__(self,data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')

    def postOrder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postOrder_traversal(node.left)
        if node.right:
            self.postOrder_traversal(node.right)
        print(node)

if __name__ == "__main__":
    tree = BinaryTree()
    n1 = Node('I')
    n2 = Node('N')
    n3 = Node('S')
    n4 = Node('C')
    n5 = Node('R')
    n6 = Node('E')
    n7 = Node('V')
    n8 = Node('A')
    n9 = Node('5')
    n10 = Node('')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2

    print(tree.root)
    print(tree.root.left)
    print(tree.root.right)
    tree.simetric_traversal()
    print()