import random

def bubble_sort(arr: list):
    """冒泡排序算法演示.

    Args:
        arr (list): 待排序的列表.  执行完毕后列表本身变为已排好序的.
    """
    n = len(arr)
    for i in range(n-1, 1, -1):
    # 对于每一轮“冒泡”，i是检查的最后一对的*右*边一个数的编号
    # 对于 a < b, range(b, a, -1)是从b倒数到(a+1)
    # Python中，n个元素的list，元素编号从0到n-1，
    # 所以，“从第(n-1)个元素倒数到第2个元素”就是range(n-2, 0, -1)
        for j in range(i):
        # j是当前检查的这一对的前一个元素，即每次比较编号为j和(j+1)的两个元素
        # 对于每一轮，j的值从0变化到i
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
        print(arr) # 检查每一轮排序的效果。真实排序时，可以注释掉这一句


def insertion_sort(arr: list):
    """插入排序算法演示.

    Args:
        arr (list): 待排序的列表.  执行完毕后列表本身变为已排好序的.
    """
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] >= arr[i]:
                arr.insert(j, arr.pop(i)) # 取出第i号元素，直接插入第j号元素的前边
                break # 一旦完成插入，直接结束 for 循环
        print(arr[:i+1], arr[i+1:], sep='   ')


def selection_sort(arr: list):
    """选择排序算法演示.

    Args:
        arr (list): 待排序的列表.  执行完毕后列表本身变为已排好序的.
    """
    n = len(arr)
    for i in range(n-1):
    # 每轮从第i号元素到第(n-1)号里寻找最小的
        min_index = i
        # 最终希望 max_index 是搜索范围里最小元素的编号，刚开始设它是i号元素
        for j in range(i+1, n): # 检查编号从i+1 到 n-1 的所有元素
            if arr[j] < arr[min_index]: # 如果找到一个更小的
                min_index = j # 就让 min_index 等于j，也就是搜索至今最小元素的编号
        # 接下来就要把最小元素提到前边了
        # 别的编程语言中，更快捷高效的可能是“把i与min_index”两个元素交换位置，
        # 但Python，直接pop然后insert更快
        arr.insert(i, arr.pop(min_index)) # 把最小元素摘出来，放到i号元素的前边，原来的i号元素变为i+1号元素了
        print(arr[:i+1], arr[i+1:], sep='   ')

if __name__ == "__main__":
    short_list = [8, 5, 2, 6, 4, 7, 1, 3]
    # list_size = 20
    # max_n = 30
    # lst = []

    # for i in range(list_size):
    #     lst.append(int(random.random() * max_n + 1))

    long_list = [13, 4, 13, 8, 18, 18, 14, 27, 16, 4,\
                 14, 28, 26, 3, 14, 30, 8, 25, 27, 6]

    # 可以把 short_list 换成 long_list，
    # 或者把bubble_sort 换成 insertion_sort 或 selection_sort
    # 查看和比较效果
    lst = short_list.copy()
    bubble_sort(lst)
