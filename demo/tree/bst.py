from binarytree import TreeNode

class BSTNode(TreeNode):
    """表示二叉搜索树 (Binary Search Tree, BST) 的一个节点, 继承自普通的二叉树节点类TreeNode
    """
    
    def __init__(self, value):
        super().__init__(value)
        self.count = 1 # 如果待添加数据中具有完全相同的取值，归为同一个节点，用计数器记录

    def print(self): # 重写TreeNode类中的print()方法，以便处理同一数据多次出现的情况
        for i in range(self.count):
            print(self.val, end = ' ')
    
    def __to_list__(self):
        return [self.val] * self.count



class BST():
    
    def __init__(self, data: list = None):
        """构造器, 可以选择在新建实例时以列表的形式填入初始数据.

        Args:
            data (list, optional): 初始数据, 默认为 None.
        """
        self.__root = None
        if data:
            for val in data:
                self.add(val)

    def loc(self, key: int):
        """ 在当前BST中试图查找以key为取值的节点
            如果BST中有这个取值的节点, 就返回它和它的上级节点 (根节点的上级节点取为None)
            如果BST中没有这个取值的节点, 就返回'l'或'r', 
            以及它的上级节点 (即若要新添加key这个数据, 应该添在谁的下边) 
        """
        prev = None # 上级节点一开始是None
        ptr = self.__root # ptr指针指向当前盯着的节点, 一开始盯着根节点
        while ptr and ptr.val != key: # 只要还没找到而且还没到叶节点
            prev = ptr # 先转存上级节点
            if key < ptr.val: # 如果key比当前节点的取值小
                if ptr.pleft: # 如果有左节点
                    ptr = ptr.pleft # 把目光转移到左节点
                else:
                    return 'l', prev # 否则直接返回
            else: # 既然还没找到, key不是小于ptr.val, 就一定是大于了
                if ptr.pright:
                    ptr = ptr.pright
                else:
                    return 'r', prev
        return ptr, prev # 如果找到了，返回两个节点


    def search(self, key) -> int:
        """在BST里查找key

        Args:
            key: 待查找的值

        Returns:
            int: key在BST中的出现次数
        """
        location, _ = self.loc(key)
        if type(location) is BSTNode:
            return location.count
        else:
            return 0


    def sorted(self) -> list:
        """把BST中所有数据按升序排列

        Returns:
            list: BST中所有数据按升序排列的列表
        """
        return self.__root.in_order() # 其实就是中序遍历整棵BST


    def check_BST(self) -> list:
        """把BST按平序输出, 直观地大致判断和我们的期望是否一致

        Returns:
            list: BST中所有值, 按平序排列
        """
        return self.__root.level_order()


    def add(self, value):
        """在当前BST中添加一个取值为value的元素.

        Args:
            value: 待添加的值
        """
        if self.__root is None:
            self.__root = BSTNode(value) # 如果BST为空，则添加为根节点
        else:
            location, prev = self.loc(value) # 找到目标节点
            if location == 'l': # 待添加的值比目标节点小
                prev.add_left(BSTNode(value)) # 添加为目标节点的左节点（loc方法保证了左节点为空）
            elif location == 'r':
                prev.add_right(BSTNode(value)) # 否则添加为右节点
            else: # 若待添加的值在BST中已经有了
                location.count += 1 # 计数器 + 1


    def remove(self, key):
        """从BST中删除一个元素. 这是BST基本操作中最难的

        Args:
            key: 待删除的值
        """
        target, prev = self.loc(key)
        if type(target) is not BSTNode:
            print(f'The value {key} is not in the BST.  Nothing is deleted.')
        elif target.count > 1:
            target.count -= 1 # 待删除的值多次出现，只需出现次数 - 1 就好了
        elif not target.pleft and not target.pright: # 如果是叶节点，直接删除
            if target is prev.pleft:
                prev.pleft = None
            else:
                prev.pright = None
        elif not target.pright: # 如果只有左节点
            # (因为到了elif这里，不可能两个节点都没有，所以没有右节点就是只有左节点)
            prev.pleft = target.pleft # 把待删除节点的整个左子树变成上级节点的左子树
        elif not target.pleft: # 如果只有右节点
            prev.pright = target.pright
        else: # 最困难的就是待删除节点的左右子树都存在
            # 思路是：从待删除节点的右子树中找一个最小的，取代待删除节点
            # 当然，也可以从待删除节点的左子树中找一个最大的
            replacer_prev = target
            replacer = target.pright
            while replacer.pleft:
                # 找到一棵BST里最小节点的办法：从根节点出发，只要还能往左就一路往左
                replacer_prev = replacer
                replacer = replacer.pleft
            target.val = replacer.val # 最简单粗暴的取代办法
            replacer_prev.pleft = replacer.pright # 如果用于取代的节点还有右子树（左边肯定为空）
            # 就接为它的上级节点的左子树


def main():
    test_bst = BST([3, 8, 2, 6, 1, 9, 4, 9, 5])
    # The BST should look like:
    #       3
    #     2   8
    #    1   6 9
    #       4
    #        5
    print(test_bst.sorted())
    # 为了检查BST是否如我们的期望，可以level_order一下，结果应该是：328169945
    print(test_bst.check_BST())
    search_test = [3, 9, 10]
    for val in search_test:
        print(f'{val} appeared {test_bst.search(val)} times.')

    test_bst.remove(1) # 删除一个叶节点
    print(test_bst.check_BST()) # 现在应该是32869945
    test_bst.remove(3) # 删除整个的根节点
    print(test_bst.check_BST()) # 现在应该是4286995
    print(test_bst.sorted()) # 顺序仍然是对的

if __name__ == "__main__":
    main()