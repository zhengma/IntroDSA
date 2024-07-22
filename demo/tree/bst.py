"""
二叉搜索树 (Binary Search Tree, BST) 的Python实现的演示.

最初在上海科桥教育讲授《CAIE A level 计算机科学》(9618) 的课堂上编写.

主要教学目的:
1.  演示第23.07节 "二叉树" 的BST部分知识点的代码实现.
2.  复习如何在Python中实现第20.1.3节 "OOP" 所述的编程思想和作风,
    特别是理解: 多个类之间的关系 (继承, 聚合) 以及 "某方法被封装进哪个类更好"
3.  展现第24章《递归》所述思想和实践在BST中的威力

作者: 马正
组织: 渊学通教育广州分校, 上海科桥教育
创建日期: Oct. 10, 2023
最后修改日期: Dec. 26, 2023
Python版本: 3.12
"""

from typing import Optional, TypeVar, Generic
from binarytree import TreeNode

V = TypeVar("V")


class BSTNode(TreeNode, Generic[V]):
    """表示二叉搜索树 (Binary Search Tree, BST) 的一个节点, 
    继承自普通的二叉树节点类TreeNode
    """

    def __init__(self, value: V) -> None:
        super().__init__(value)
        self.count = 1
        # 如果待添加数据中具有完全相同的取值, 归为同一个节点, 用计数器记录

    def print(self) -> None:
        """重写TreeNode类中的print()方法, 以便处理同一数据多次出现的情况
        """
        for _ in range(self.count):
            print(self.val, end=' ')

    def __to_list__(self) -> list[V]:
        return [self.val] * self.count


class BST(Generic[V]):

    def __init__(self, data: Optional[list[V]]) -> None:
        """构造器, 可以选择在新建实例时以列表的形式填入初始数据.

        Args:
            data (list, optional): 初始数据, 默认为 None.
        """
        self.__root = None
        if data:
            for val in data:
                self.insert(val)

    def get_root(self) -> BSTNode:
        return self.__root

    def __loc_nonrecursive(self, key: V):
        """在当前BST中试图查找以key为取值的节点.

        如果BST中有这个取值的节点, 就返回它和它的上级节点
        (根节点的上级节点取为None)
        如果BST中没有这个取值的节点, 就返回'l'或'r', 
        以及它的上级节点 (即若要新添加key这个数据, 应该添在谁的下边) 
        """
        prev = None  # 上级节点一开始是None
        ptr = self.__root  # ptr指针指向当前盯着的节点, 一开始盯着根节点
        while ptr and ptr.val != key:  # 只要还没找到而且还没到叶节点
            prev = ptr  # 先转存上级节点
            if key < ptr.val:  # 如果key比当前节点的取值小
                if ptr.pleft:  # 如果有左节点
                    ptr = ptr.pleft  # 把目光转移到左节点
                else:
                    return 'l', prev  # 否则直接返回
            else:  # 既然还没找到, key不是小于ptr.val, 就一定是大于了
                if ptr.pright:
                    ptr = ptr.pright
                else:
                    return 'r', prev
        return ptr, prev  # 如果找到了, 返回两个节点

    def __loc(self, node: BSTNode[V], key: V) -> BSTNode[V]:
        if key == node.val:
            return node
        if key < node.val:
            return self.__loc(node.pleft, key) if node.pleft else None
        if key > node.val:
            return self.__loc(node.pright, key) if node.pright else None
        return None

    def search(self, key: V) -> int:
        """在BST里查找key

        Args:
            key: 待查找的值

        Returns:
            int: key在BST中的出现次数
        """
        ptr = self.__loc(self.__root, key)
        return ptr.count if ptr else 0

    def sorted(self) -> list:
        """把BST中所有数据按升序排列

        Returns:
            list: BST中所有数据按升序排列的列表
        """
        return self.__root.in_order()  # 其实就是中序遍历整棵BST


    def check_bst(self) -> list[V]:
        """把BST按平序输出, 直观地大致判断和我们的期望是否一致

        Returns:
            list: BST中所有值, 按平序排列
        """
        return self.__root.level_order()

    def __add(self, node: BSTNode[V], value: V) -> BSTNode[V]:
        if not node:
            return BSTNode[V](value)
        if value < node.val:
            node.set_left(self.__add(node.pleft, value))
        elif value > node.val:
            node.set_right(self.__add(node.pright, value))
        else:
            node.count += 1
        return node

    def insert(self, value: V) -> None:
        """
        在当前BST中添加一个取值为value的元素.

        Args:
            value: 待添加的值
        """
        self.__root = self.__add(self.__root, value)

    def insert_nonrecursive(self, value: V) -> None:
        """用非递归的办法, 在当前BST中添加一个取值为value的元素.

        Args:
            value: 待添加的值
        """
        if not self.__root:
            self.__root = BSTNode(value)  # 如果BST为空，则添加为根节点
        else:
            location, prev = self.__loc_nonrecursive(value)  # 找到目标节点
            if location == 'l':  # 待添加的值比目标节点小
                prev.add_left(BSTNode(value))
                # 添加为目标节点的左节点（loc方法保证了左节点为空）
            elif location == 'r':
                prev.add_right(BSTNode(value))  # 否则添加为右节点
            else:  # 若待添加的值在BST中已经有了
                location.count += 1  # 计数器 + 1

    def __del(self, node: BSTNode[V], key: V) -> BSTNode[V]:
        """
        递归地在以node为根节点的BST中查找并删除一个值. 
        若该值不存在, 则不改动BST

        属性:
            node (BSTNode): 一个BST的根节点, 该BST中某节点的值可能为待删除的值
            key (V): 待删除的取值

        返回:
            BSTNode: 删除后的BST的根节点
        """
        if key < node.val:  # 如果待删除节点可能在左子树
            # 如果左子树存在, 就在左子树里进行删除,
            # 然后更新左节点为删好之后的左子树根节点
            # 如果左子树不存在，就说明待删除的数据不在，那就什么都不做
            node.set_left(self.__del(node.pleft, key)
                          if node.pleft else None)
            return node  # 有改变也在左子树, 当前根节点肯定不动. 直接返回.
        if key > node.val:
            node.set_right(self.__del(node.pright, key)
                           if node.pright else None)
            return node
        # 到现在为止还没返回，就说明此刻的node就是待删除节点
        if node.count > 1:
            node.count -= 1  # 待删除的值多次出现, 只需出现次数 - 1 就好了
            return node
        if not node.pleft:  # 如果左节点为空
            temp = node.pright  # 返回其右节点 (左右节点皆空自然返回None)
            del node  # Python 不像 Java，不会自动垃圾回收
            return temp
        elif not node.pright:  # 若左节点非空但右节点为空
            temp = node.pleft  # 返回其左节点
            del node
            return temp
        # 最困难的就是待删除节点的左右子树都存在
        # 思路是: 首先从待删除节点的右子树中找一个最小的
        # 它的值一定大于待删除节点的左子树所有节点
        # (当然, 也可以从待删除节点的左子树中找一个最大的，原理类似)
        temp = node.pright
        while temp.pleft:
            # 找到一棵BST里最小节点的办法:
            # 从根节点出发, 只要还能往左就一路往左
            temp = temp.pleft
        # 这个节点的左子树原本为空, 现在把待删除节点的左子树接上去
        temp.set_left(node.pleft)
        temp = node.pright  # 把待删除节点用其右节点取代
        del node
        return temp

    def delete(self, key: V) -> None:
        self.__root = self.__del(self.__root, key)

    def delete_nonrecursive(self, key: V) -> None:
        """从BST中删除一个元素. 这是BST基本操作中最难的

        Args:
            key: 待删除的值
        """
        target, prev = self.__loc_nonrecursive(key)
        if not isinstance(target, BSTNode):
            print(f'The value {key} is not in the BST.  Nothing is deleted.')
        elif target.count > 1:
            target.count -= 1  # 待删除的值多次出现, 只需出现次数 - 1 就好了
        elif not target.pleft and not target.pright: # 如果是叶节点, 直接删除
            if target is prev.pleft:
                prev.pleft = None
            else:
                prev.pright = None
        elif not target.pright:  # 如果只有左节点
            # (因为到了elif这里, 不可能两个节点都没有，所以没有右节点就是只有左节点)
            # 把待删除节点的整个左子树变成上级节点的左子树
            prev.pleft = target.pleft
        elif not target.pleft:  # 如果只有右节点
            prev.pright = target.pright
        else:  # 最困难的就是待删除节点的左右子树都存在
            # 思路是: 从待删除节点的右子树中找一个最小的，取代待删除节点
            # 当然, 也可以从待删除节点的左子树中找一个最大的
            replacer_prev = target
            replacer = target.pright
            while replacer.pleft:
                # 找到一棵BST里最小节点的办法：
                # 从根节点出发, 只要还能往左就一路往左
                replacer_prev = replacer
                replacer = replacer.pleft
            target.val = replacer.val  # 最简单粗暴的取代办法
            replacer_prev.pleft = replacer.pright
            # 如果用于取代的节点还有右子树（左边肯定为空）
            # 就接为它的上级节点的左子树

    def left_rotate(self, node: BSTNode) -> BSTNode:
        if not node.pright:
            return node
        ptr = node.pright
        node.set_right(ptr.pleft)
        ptr.set_left(node)
        return ptr

    def right_rotate(self, node: BSTNode) -> BSTNode:
        if not node.pleft:
            return node
        ptr = node.pleft
        node.set_left(ptr.pright)
        ptr.set_right(node)
        return ptr

    def lr_whole(self) -> None:
        self.__root = self.left_rotate(self.__root)

    def rr_whole(self) -> None:
        self.__root = self.right_rotate(self.__root)
