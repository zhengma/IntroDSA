def merge(left: list, right: list) -> list:
    """把两个分别排好序的序列归并成一个完整的排好序的序列

    Args:
        left (list): 参与归并的列表之一. 完整列表的"左半截", 已经按升序排好
        right (list): 参与归并的列表之一, 完整列表的"右半截", 已经按升序排好

    Returns:
        list: 归并好的列表, 整个按升序排列
    """    
    merged = [] # 准备把元素一个个append到这里, 以便返回
    while left or right: 
        # 如果把list的名字当作一个boolean型变量一样使用. 规则是：
        # list如果是空的, 没有元素, 就是False, 有元素就True
        if left and (not right or (right and left[0] < right[0])):
            # 从左半截的开头取元素, 需要两个条件同时满足：
            # 1. 左半截必须非空.
            # 2. 右半截要么空了, 要么开头的元素比左半截开头的元素更大.
            merged.append(left.pop(0)) # 从左边的开头取元素, 添加到归并好的序列的末尾
        else:
            merged.append(right.pop(0)) # 否则就从右边的开头取元素
    return merged


def mergesort(lst: list) -> list:
    '''把参数提供的list用归并排序排好, 并返回排好序的list (原未排好序的list不动)
    '''
    if len(lst) <= 1:
        return lst # 只有一个元素就不需要排序了
    else:
        # 两个整数之间/, 如果商是小数, 则返回小数; 但如果是//, 永远返回商的整数部分
        mid = len(lst) // 2
        # 复习：lst[a:b]是从a号开头到b-1号结尾之间的一段, 
        # a如果省略, 默认为0 (从头开始) ; b如果省略, 默认为len (到尾结束) 
        left = mergesort(lst[:mid]) # 把元素编号从0到 mid - 1 的左半段排好序
        right = mergesort(lst[mid:]) # 把右半段排好序
        return merge(left, right) # 归并左右两段并返回


def main():
    test_list = [8, 5, 2, 6, 4, 7, 1, 3]
    print(mergesort(test_list))
    test_list2 = [3, 8, 2, 6, 1, 9, 4, 2, 5]
    print(mergesort(test_list2))

if __name__ == "__main__":
    main()