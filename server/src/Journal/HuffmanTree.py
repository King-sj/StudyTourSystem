class HuffmanTreeNode:
    def __init__(self, name, weight=0, parent=-1, lchild=-1, rchild=-1):
        self.name = name
        self.weight = weight
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild