from typing import Generic, TypeVar, Self

V = TypeVar("V")

class TreeNode(Generic[V]):
    """本类描述二叉树的一个节点

    Attributes:
        val: 节点存储的数据.
        pleft (TreeNode): 指向左节点的指针.
        pright (TreeNode): 指向右节点的指针.

    """

    val: V
    pleft: Self
    pright: Self

    def __init__(self, value: V):
        self.val = value
        self.pleft = None
        self.pright = None

    def set_left(self, leftnode: Self) -> None:
        self.pleft = leftnode

    def set_right(self, rightnode) -> None:
        self.pright = rightnode

    def print(self) -> None:
        print(self.val, end = ' ')

    def __to_list__(self) -> list[V]:
        return [self.val]

    def pre_order(self) -> list[V]:
        """返回二叉树中所有元素按前序遍历的结果

        Returns:
            list: 二叉树中所有元素, 按前序遍历的顺序
        """
        '''result= [] 
        result.append(self.val) # 先输出根节点
        if self.pleft: # 如果左节点不为空
            result += self.pleft.pre_order() # 前序遍历左子树
        if self.pright: # 如果右节点不为空
            result += self.pright.pre_order() # 前序遍历右子树
        return result'''
        # 充分看懂了上面的解法后，可以用以下办法写，简洁很多
        return (self.__to_list__()
            + (self.pleft.pre_order() if self.pleft else [])
            + (self.pright.pre_order() if self.pright else []))

    def in_order(self) -> list[V]:
        return ((self.pleft.in_order() if self.pleft else [])
            + self.__to_list__()
            + (self.pright.in_order() if self.pright else []))

    def post_order(self) -> list[V]:
        return ((self.pleft.post_order() if self.pleft else [])
            + (self.pright.post_order() if self.pright else [])
            + self.__to_list__())

    def level_order(self) -> list[V]:
        queue = [self]
        result = []
        while queue: # 只要queue还没空
            if queue[0].pleft:
                queue.append(queue[0].pleft) # 把队列开头一个节点的左节点加入队列末尾
            if queue[0].pright:
                queue.append(queue[0].pright) # 然后是右节点
            result += queue.pop(0).__to_list__()
        return result

    def depth(self) -> int:
        return (1 if not (self.pleft or self.pright)
                else max(self.pleft.depth() if self.pleft else 0,
                         self.pright.depth()if self.pright else 0) + 1)

class TreeNodeWithParent(TreeNode, Generic[V]):

    parent: Self

    def __init__(self, value):
        super().__init__(value)
        self.parent = None

    def set_left(self, leftnode):
        super().set_left(leftnode)
        leftnode.parent = self

    def set_right(self, rightnode):
        super().set_right(rightnode)
        rightnode.parent = self

    def ancestors(self) -> list[V]:
        result: list[V] = []
        ptr = self
        while ptr:
            result.append(ptr)
            ptr = ptr.parent
        return result

    def lca(self, other: Self) -> Self:
        a1 = self.ancestors()
        a2 = other.ancestors()
        ptr = a1.pop()
        result = None
        while ptr is a2.pop():
            result = ptr
            ptr = a1.pop()
        return result

def main():
    nodes: list[TreeNodeWithParent[str]] = []

    #            A
    #       /         \
    #      B           C
    #    /   \        / \
    #   D     E      F   G
    #  / \   / \    /
    # H   I J   K  L

    for s in 'ABCDEFGHIJKL':
        # ind:0123456789AB
        # nodes.append(TreeNode(s))
        nodes.append(TreeNodeWithParent(s))

    nodes[0].set_left(nodes[1])
    nodes[0].set_right(nodes[2])
    nodes[1].set_left(nodes[3])
    nodes[1].set_right(nodes[4])
    nodes[2].set_left(nodes[5])
    nodes[2].set_right(nodes[6])
    nodes[3].set_left(nodes[7])
    nodes[3].set_right(nodes[8])
    nodes[4].set_left(nodes[9])
    nodes[4].set_right(nodes[10])
    nodes[5].set_left(nodes[11])

    root = nodes[0]

    print(root.pre_order()) # ABDHIEJKCFLG
    print(root.in_order()) # HDIBJEKALFCG
    print(root.post_order()) # HIDJKEBLFGCA
    print(root.level_order()) # ABCDEFGHIJKL
    print(root.depth()) # 4
    a1 = nodes[8].ancestors()
    print([n.val for n in a1]) # IDBA
    print(nodes[8].lca(nodes[10]).val) # B

if __name__ == "__main__":
    main()
