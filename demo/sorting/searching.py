def linear_search(lst: list, key) -> int:
    for i in range(len(lst)):
        if (key == lst[i]):
            return i
    return -1


def binary_search(lst: list, key: int) -> int:
    """对已经从小到大排好序的整数列表应用折半查找算法

    Args:
        lst (list): 一个列表. 其元素全部为整数, 并已经按升序排列.
        key (int): 待查找的数值.

    Returns:
        int: lst中的一个元素的编号, 其值与key相同. 
        如果lst中存在多个这样的元素, 返回第一个被找到的.
        如果lst中没有这样的元素, 返回-1.
    """    

    start = 0 # 当前查找范围的头一个元素的编号
    end = len(lst) # 当前查找范围的最后一个元素的编号
    while start < end:
        # 如果end反而比start要小，就说明待查找的部分长度为零了，没找到
        mid = (start + end) // 2
        # print(start, end, mid, lst[mid])
        # 这句是为了看清每次搜索范围的变化，实际编程时不用输出
        if key > lst[mid]:
        # x如果在list中，一定在右半截
            start = mid + 1 # 右半截的end还是原来的end，start变为mid + 1
            # 之所以要 +1，是因为我知道mid这里肯定找不到了，
            # 所以不需要再纳入搜索范围了。
            # 下面的 -1 同理
        elif (key < lst[mid]): # x如果在list中，一定在左半截
            end = mid # 左半截的start还是原来的start，end变为mid - 1
        else: # 既不大于又不小于，就是找到了一个
            return mid # 就返回这个的编号
    return -1 # 如果终究没找到，return -1


def binary_search_recursive(lst: list, key: int, start: int, end: int) -> int:
    """用递归实现折半查找算法

    Args:
        lst (list): 一个列表. 其元素全部为整数, 并已经按升序排列.
        key (int): 待查找的数值.
        start (int): 查找范围里第一个元素的编号.
        end (int): 查找范围里最后一个元素的编号 + 1.

    Returns:
        int: lst中的一个元素的编号, 其值与key相同. 
        如果lst中存在多个这样的元素, 返回第一个被找到的.
        如果lst中没有这样的元素, 返回-1.
    """    
    if start >= end:
        return -1
    mid = (start + end) // 2
    # print(start, end, mid, lst[mid])
    if key > lst[mid]:
        return binary_search_recursive(lst, key, mid + 1, end)
    elif key < lst[mid]:
        return binary_search_recursive(lst, key, start, mid)
    else:
        return mid

def main():
    short_list = [8, 5, 2, 6, 4, 7, 1, 3]
    # list_size = 20
    # max_n = 30
    # lst = []

    # for i in range(list_size):
    #     lst.append(int(random.random() * max_n + 1))

    long_list = [13, 4, 13, 8, 18, 18, 14, 27, 16, 4,\
                 14, 28, 26, 3, 14, 30, 8, 25, 27, 6]

    # 如果 x 只在 list 中出现一次，返回这次出现的编号
    lst = long_list.copy()
    print(linear_search(lst, 6))

    # 如果 x 在list中出现多次，返回第一次出现的编号
    # 在上面的代码中，这是因为：Python中一个function只能return一次
    # 所以找到第一次出现的位置并且return之后，后面的查找就不会再执行了
    print(linear_search(lst, 18))

    # 如果 x 在 list 中没有出现过，返回-1
    # 在上面的代码中，这是因为：如果for loop执行中查找到了，就已经return并结束function运行了
    # 所以如果for loop 执行完了还没找到，就说明没有，直接返回-1
    print(linear_search(lst, 31))

    orderedlst = long_list.copy()
    orderedlst.sort()
    print(orderedlst)

    print(binary_search(orderedlst, 6))
    print(binary_search_recursive(orderedlst, 28, 0, len(orderedlst)))


if __name__ == "__main__":
    main()