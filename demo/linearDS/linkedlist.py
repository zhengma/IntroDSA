"""单向链表 (Singly Linked List) 的Python实现的演示.

最初在讲授《CAIE A level 计算机科学》(9618) 的课堂上编写.
主要教学目的:
1.  演示第19.1.3节 "链表" 的知识点的代码实现.
2.  复习如何在Python中实现第20.1.3节 "OOP" 所述的编程思想和作风.
3.  复习第20.2.2节 "异常处理" 的相关理论知识在Python中的体现.
4.  补充讲解课外知识 "魔法方法" (magic methods): 
    "如何让我们编写好的链表用起来像Python自带的list一样舒服?"

作者: 马正
组织: 渊学通教育广州分校, 上海科桥教育
创建日期: Oct. 10, 2023
最后修改日期: Nov. 12, 2023
Python版本: 3.12
"""
from typing import Any, Self


class _LinkedListNode:
    """
    单向链表中的一个节点.

    属性:
        val: 节点存储的值.
        next: 指向下一个节点的指针
    """
    val: Any  # 鉴于绝大多数同学此时还没学到"泛型"这个知识点，这里没有用TypeVar
    next: Self

    def __init__(self, value: Any) -> None:
        self.val = value
        self.next = None


class SinglyLinkedList:
    """
    单向链表的实现.

    本实现尽可能模拟Python自带的列表 (list)的行为.  为此重新实现了Python的很多
    "魔法方法".

    属性:
        __head: 头指针.
        __tail: 尾指针. 单向链表通常不需要尾指针，而可以用 `next is None` 
        来判断是否到达末尾. 但是有尾指针，对添加 (append) 操作很有帮助.
        __ptr: 可以指向本链表任意链节的指针, 用于遍历等用途.
        __len: 链表此刻的长度，随增删而改变.
    """

    __head: _LinkedListNode
    __tail: _LinkedListNode
    __ptr: _LinkedListNode
    __len: int

    def __init__(self, data: list = None) -> None:
        """
        单向链表类的构造器. 可以读入一个Python列表来初始化.

        参数:
            data (列表, 可选): 创建链表时存入的初始值. 默认为 None.
        """
        self.__head = None
        self.__tail = None
        self.__len = 0
        if data:
            for item in data:
                self.append(item)

    def get_head(self) -> _LinkedListNode:
        """
        返回头指针.
        """
        return self.__head

    def get_tail(self) -> _LinkedListNode:
        """
        返回尾指针.
        """
        return self.__tail

    def clear(self) -> None:
        """
        清空整个链表.

        这是Python列表自带的方法之一.
        """
        self.__head = None
        self.__tail = None
        # 只需把头尾指针重置为None就好了，Python会自己回收链节的.

    def __len__(self) -> int:
        """
        返回链表长度.

        "魔法方法"之一.  比如x是某类的实例, len(x)自动调用该类的__len__()
        """
        return self.__len

    def __bool__(self) -> bool:
        """
        返回列表是否为非空.

        "魔法方法"之一.  比如x是某类的实例,
        `if x:` 这类场合自动调用该类的__bool__()

        返回:
            bool: 当且仅当链表非空时为True
        """
        return self.__len != 0

    def __locate__(self, index: int | slice) -> _LinkedListNode:
        """
        随机访问, 按编号访问链表中的一个元素.

        参数:
            index (int): 一个元素的编号.

        抛出:
            IndexError: 若元素编号越界.

        返回:
            指向该编号的元素的指针.
        """
        if index >= self.__len:
            raise IndexError(index)
        ptr = self.__head
        for _ in range(index):
            ptr = ptr.next
        return ptr

    def __slice__(self, indices: slice) -> Self:
        """
        按编号截取一个链表中的一个片段 (slice).

        截取片段时不会抛出异常, 只会返回空链表.

        参数:
            indices (slice): 片段的编号范围.

                一个slice型对象有三个只读属性: `start`, `stop`和`step`.
                比如[2:11:3]对应的slice型对象就是
                `start = 2`, `stop = 11`, `step = 3`. 
                [2:]对应的就是`start = 2`, `stop = None`, `step = None`.
                [::2]对应的就是`start = None`, `stop = None`, `step = 2`.
                其余类推.

        返回:
            Self: 一个新的链表, 其中每个元素的值是指针, 依序指向片段中各个链节.
        """
        # 未指定片段起点, 则默认为头一个元素
        start = indices.start if indices.start else 0
        # 未指定片段终点, 则默认为最后一个元素
        stop = indices.stop if indices.stop else self.__len
        # 未指定步长, 则默认为1
        step = indices.step if indices.step else 1
        sub_list = SinglyLinkedList()
        idx = start
        ptr = self.__locate__(start)
        while idx < stop:
            sub_list.append(ptr)
            for _ in range(step):
                # for循环不需要用到循环变量的值, 只是"把next重复若干次"
                # 此时可以在循环变量这里放一个_
                if ptr.next:  # 遍历到末端则跳出循环
                    ptr = ptr.next
                else:
                    break
            idx += step
        return sub_list

    def __getitem__(self, index: int | slice) -> Any:
        """
        截取链表中的一个元素或一个片段 (slice).

        "魔法方法"之一.  比如x是某类的实例, 诸如`x[2]`, `x[2:]`, `x[2:11:3]`
        等调用的就是该类的__getitem__()方法.

        参数:
            index (int | slice): 如果为`int`型, 表示单独一个元素的编号.
            如果为`slice`型, 表示一个片段.

        返回:
            Any: 如果indices为`int`型, 则返回该编号的元素的值.
            如果为`slice`型, 则返回一个新的链表, 里面是按要求截取的片段.
        """
        if isinstance(index, int):  # 若index为整型
            try:
                return self.__locate__(index).val  # 返回单独一个元素的值
            except IndexError as ie:  # 若出现下标越界异常，则提示
                print(f'Index {ie} out of bound!')
                return None  # 下标越界后返回空指针
        sub_list = SinglyLinkedList()
        ptrs = self.__slice__(index)
        for ptr in ptrs:
            sub_list.append(ptr.val)
        return sub_list

    def __setitem__(self, index: int | slice, newvalue: Any) -> bool:
        """
        修改链表中的一个或多个元素的值.

        参数:
            index (int | slice): 如果为`int`型, 表示单独一个元素的编号.
            如果为`slice`型, 表示一个片段.

            newvalue (Any): 新的取值. 如果index是单独的编号, 则newvalue是一个值.
            如果index是一个片段, 则newvalue是任何可遍历, 有len()的容器.

        抛出:
            ValueError: 如果index表示一个片段, 而len(newvalue)与片段长度不吻合

        返回:
            bool: 当且仅当修改成功时为True
        """
        if isinstance(index, int):
            try:
                self.__locate__(index).val = newvalue
                return True
            except IndexError as ie:
                print(f'Index {ie} out of bound!')
                return False
        ptrs = self.__slice__(index)  # 先把指向各个要修改的元素的指针整理到一起
        if len(ptrs) != len(newvalue):  # 若长度不吻合, 抛出异常
            raise ValueError(f'New values is of size {len(newvalue)} \
                but the slice is of size {len(ptrs)}')
        ptr = ptrs.get_head()
        for value in newvalue:  # 遍历newvalue (不管它是哪种容器)
            ptr.val.val = value  # 把新的值对号入座一个个写入
            # 注意, ptrs是一个"指针的列表"，它的每个元素的值是一个指向链节的指针
            # 所以要修改的是ptr.val.val
            ptr = ptr.next
        return True

    def __insert_head__(self, value: Any) -> bool:
        """
        在链表的开头插入新的元素.
        
        单向链表在指定元素前面插入元素是非常不便的,
        这是它相比于双向链表的一个重要缺点.
        在指定元素后面插入则方便得多.
        所以, 需要写两个方法, 分别处理"插入到开头"和"插入指定元素后面"

        参数:
            value (Any): 新元素的取值

        返回:
            bool: 当且仅当插入成功时为True
        """

        new_node = _LinkedListNode(value)  # 先创建链表节点
        if self.__head is None:  # 如果链表整个是空的
            self.__head = new_node  # 设新建的链节为头部元素
            self.__tail = self.__head  # 并把__tail也指向它
        else:
            new_node.next = self.__head  # 否则，原来的头部排在新链节后面
            self.__head = new_node  # __head 指向新元素
        self.__len += 1  # 链表长度++
        return True

    def __insert_after__(self, prev: _LinkedListNode, value: Any) -> bool:
        """
        在指定元素后面插入新的元素

        参数:
            prev (_LinkedListNode): 指向新元素的前一个链节的指针

            value (Any): 新元素的取值

        抛出:
            ValueError: 如果prev是空指针
            TypeError: 如果prev指向的不是单向链表的链节

        返回:
            bool: 当且仅当插入成功时为True
        """
        try:
            if not prev:
                raise ValueError
            if not isinstance(prev, _LinkedListNode):
                raise TypeError
            new_node = _LinkedListNode(value)
            # 想清接下来两行为啥要这么写, 以及为啥按这个顺序写
            new_node.next = prev.next
            prev.next = new_node
            if prev is self.__tail:
                self.__tail = new_node
            self.__len += 1
            return True
        except ValueError:
            print('Attempting to insert after a null node!')
            return False
        except TypeError:
            print('The previous node has to be provided as a reference!')
            return False

    def insert(self, index: int, value: Any) -> bool:
        """
        实现与Python自带列表的`.insert()`相同的功能

        参数:
            index (int): 插入至原链表中该编号链节的前面, 因此它也是新链节的编号

            value (Any): 新链节的取值.

        返回:
            bool: 当且仅当插入成功返回True
        """
        if index == 0:
            return self.__insert_head__(value)
        try:
            at = self.__locate__(index - 1)  # 先找到 index - 1 这个编号的链节
            # 因为新链节要插入到它的后面
            return self.__insert_after__(at, value)
        except IndexError as ie:
            print(f'Index {ie} out of bound!')
            return False

    def append(self, value: Any) -> bool:
        """
        实现与Python自带列表的`.append()`相同的功能

        参数:
            value (Any): 新元素的取值

        返回:
            bool: 当且仅当添加成功时为True
        """
        if self.__head is None:
            return self.__insert_head__(value)
        else:
            return self.__insert_after__(self.__tail, value)

    def pop(self, index: int = 0) -> Any:
        """
        实现与Python自带列表的`.pop()`相近的功能.

        区别: 不填index参数时默认pop第一个元素 (Python列表是pop最后一个元素)

        参数:
            index (int, optional): 需弹出的元素的编号. 默认为0.

        返回:
            Any: 弹出的元素的值.  若弹出失败, 返回None.
        """
        if self.__len == 0:
            return None
        try:
            if index == 0:
                temp = self.__head.val
                self.__head = self.__head.next
            else:
                target_prev = self.__locate__(index - 1)  # 找到前一个元素
                temp = target_prev.next.val  # 把要弹出的元素先用指针指着
                if target_prev.next is self.__tail:  # 如果要弹出最后一个元素
                    self.__tail = target_prev  # 还要修改 __tail 指针
                target_prev.next = target_prev.next.next  # 修改next来实现删除
            self.__len -= 1  # 不要忘记更新长度
            return temp
        except IndexError as ie:
            print(f'Index {ie} out of bound!')
            return None

    def index(self, key: Any) -> int:
        """
        实现与Python自带列表的`.index()`相同的功能

        参数:
            key (Any): 要查找的值

        返回:
            int: key第一次出现的元素的编号. 若链表中没有找到，返回-1
        """
        ptr = self.__head
        idx = 0
        while ptr.val != key:  # 复习顺序查找算法
            if ptr.next is None:
                return -1
            idx += 1
            ptr = ptr.next
        return idx

    def remove(self, key: Any) -> bool:
        """
        实现与Python自带列表的`.remove()`相同的功能

        参数:
            key (Any): 需要删除的元素的取值

        抛出:
            ValueError: 若取值为key的元素在链表中不存在

        返回:
            bool: 当且仅当删除成功时为True
        """
        try:
            idx = self.index(key)
            if idx < 0:
                raise ValueError(key)
            self.pop(idx)
            return True
        except ValueError as ve:
            print(f'\'{ve}\' does not exist in the list!')
            return False

    def copy(self) -> Self:
        """
        实现与Python自带列表的`.copy()`相同的功能

        返回:
            Self: 本链表的一个深度拷贝.
        """
        new_list = SinglyLinkedList()
        ptr = self.__head
        while ptr:
            new_list.append(ptr.val)
            ptr = ptr.next
        return new_list

    def reverse(self) -> Self:
        """
        实现与Python自带列表的`.reverse()`相同的功能

        返回:
            Self: 一个新的链表, 其中的元素顺序与本链表相反
        """
        new_list = SinglyLinkedList()
        ptr = self.__head
        while ptr:
            new_list.insert(0, ptr.val)
            ptr = ptr.next
        return new_list

    def __iter__(self) -> Self:
        """
        返回当前链表的一个迭代器 (iterator).

        "魔法方法"之一. 比如 `elems` 是某个容器类的实例, 执行 `for x in elems:`
        的时候, 就会先调用 `elems.__iter__()`

        返回:
            Self: 本实例的一个深度拷贝, 把__ptr置于开头
        """
        iterator = self.copy()
        iterator.__ptr = iterator.get_head()
        return iterator

    def __next__(self) -> Any:
        """
        返回当前链表的下一个元素.

        "魔法方法"之一. 比如 `elems` 是某个容器类的实例, 执行 `for x in elems:`
        先调用 `elems.__iter__()` 以后，就一次次调用 `elems.__next__()`,
        直到抛出 `StopIteration` 异常为止.

        抛出:
            StopIteration: 若到达链表的尾部.

        返回:
            Any: 下一个元素的值.
        """
        if not self.__ptr:
            raise StopIteration
        else:
            val = self.__ptr.val
            self.__ptr = self.__ptr.next
            return val

    def __add__(self, other: Any) -> Self:
        """
        链表和其它可迭代对象的拼接 (concatenation), 当前链表在前.

        "魔法方法"之一. 比如设`a`、`b`是两个对象, 执行 `a + b` 的时候,
        Python就会先尝试调用 `a.__add__(b)`

        参数:
            other (Any): 要拼接在当前链表后方的数据.
            不一定是链表, 只要可迭代 (实现了`__iter__`和`__next__`)就行.

        返回:
            Self: 一个新的链表, 前半截是当前链表, 后面接着`other`中的数据
        """
        combined = self.copy()
        for item in other:
            combined.append(item)
        return combined

    def __radd__(self, other: Any) -> Self:
        """
        链表和其它可迭代对象的拼接 (concatenation), 当前链表在后.

        "魔法方法"之一. 比如设`a`、`b`是两个对象, 执行 `a + b` 的时候,
        若调用 `a.__add__(b)` 失败, Python 就会尝试调用 `b.__radd__(a)`

        参数:
            other (Any): 要拼接在当前链表前方的数据.
            不一定是链表, 只要可迭代 (实现了`__iter__`和`__next__`)就行.

        返回:
            Self: 一个新的链表, 前半截是`other`中的数据, 后面接着当前链表的数据
        """
        combined = SinglyLinkedList()
        for item in other:
            combined.append(item)
        return combined + self

    def __str__(self) -> str:
        """
        把当前链表的内容转化为字符串输出.

        "魔法方法"之一. 比如设`x`是某个对象, 执行`str(x)`时就会返回`x.__str__()`
        `print(x)` 等需要用到字符串的时候也会自动调用`__str__()`

        返回:
            str: 当前链表的全部内容, 十个一行, 两个元素之间用三个空格隔开
        """
        _per_line = 10
        counter = 0
        string = ''
        for value in self:
            string += f'{value}   '
            counter += 1
            if counter == _per_line:
                string += '\n'
                counter = 0
        return string

    def __merge__(self, left: Self, right: Self) -> Self:
        """
        `self.merge()`的辅助函数, 用于归并排序的归并步骤.

        基本完全抄自 `mergesort.py`中的代码, 没怎么改.
        这就看出来实现了很多 "魔法方法" 带来的便利.

        参数:
            left (Self): 左半截的链表, 本身已排好序
            right (Self): 右半截的链表, 本身已排好序

        返回:
            Self: 归并后的完整链表, 整体排好序
        """
        merged = SinglyLinkedList()
        while left or right:
            if left and (not right or (right and left[0] < right[0])):
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        return merged

    def sort(self) -> Self:
        """
        实现与Python自带列表的`.sort()`相同的功能.

        Python自带列表的`.sort()`, 对于较长的列表用的也是归并排序.

        返回:
            Self: 当前列表从小到大排好序的结果.
        """
        if len(self) <= 1:
            return self
        mid = len(self) // 2
        left = self[:mid].sort()
        right = self[mid:].sort()
        return self.__merge__(left, right)
