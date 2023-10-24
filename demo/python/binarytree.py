class TreeNode:
    """本类描述二叉树的一个节点

    Attributes:
        val: 节点存储的数据.
        pleft (TreeNode): 指向左节点的指针.
        pright (TreeNode): 指向右节点的指针.

    """        
    def __init__(self, value):
        self.val = value
        self.pleft = None
        self.pright = None

    def add_left(self, leftnode: TreeNode):
        self.pleft = leftnode

    def add_right(self, rightnode: TreeNode):
        self.pright = rightnode

    def print(self):
        print(self.val, end = ' ')

    def preorder(self):
        self.print()
        if self.pleft is not None:
            self.pleft.preorder()
        if self.pright is not None:
            self.pright.preorder()

    def inorder(self):
        if self.pleft is not None:
            self.pleft.inorder()
        self.print()
        if self.pright is not None:
            self.pright.inorder()

    def postorder(self):
        if self.pleft is not None:
            self.pleft.postorder()
        if self.pright is not None:
            self.pright.postorder()
        self.print()