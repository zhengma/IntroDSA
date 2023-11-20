def arithmetic(a: int, d: int, n: int) -> int:
    '''
    递归计算首项为a, 公差为d的等差数列的第n项
    
    n ≥ 1
    '''
    if n == 1:
        return a
    else:
        return arithmetic(a, d, n-1) + d


def fibonacci(n: int) -> int:
    '''
    递归计算斐波那契数列的第n项

    n ≥ 1
    '''
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_1(n: int) -> int:
    '''
    迭代计算斐波那契数列的第n项.

    递归是自顶向下的, 所以会有很多重复计算
    可以把斐波那契数列的前面各项放到一个list里, 直接查阅, 这样就不需要反复算一些前面的项了
    n≥1
    '''
    if n==1 or n==2:
        return 1
    else:
        sequence = [1, 1]
        for i in range(2, n): 
            # 注意sequence[i]其实是斐波那契数列的第(i+1)项，所以循环的最后，i = n-1 加入数列第n项
            sequence.append(sequence[-1] + sequence[-2]) # 每次把最后两项的和加入到末尾
        return sequence[-1] # 然后返回最后一个元素


def fibonacci_2(n: int) -> int:
    '''
    迭代计算斐波那契数列的第n项.
    
    如果只要第n项, 那么前面的项都不用保留
    只需要三个变量来储存即可
    '''
    if n==1 or n==2:
        return 1
    else:
        a = b = 1
        for i in range(2, n):
            c = a + b # 算出下一项
            a = b # 然后把各个变量的值往前挪一格，为下一次计算做准备
            b = c
    return c


def hanoi(n: int, start: str, via: str, end: str):
    """
    输出n层汉诺塔问题的解.
    
    每一行为一个步骤，格式为：'from -> to', 从哪个柱子取下最上面的一个圆片, 套到哪一个柱子
    
    参数:
        n (int): 层数
        start (str): 起始柱的名称, 刚开始所有圆片都串在这个柱子上
        via (str): 辅助柱的名称
        end (str): 目标柱的名称, 游戏结束时所有圆片都要串到这个柱子上
    """    
    if n == 1:
        print(f"{start} -> {end}")
    else:
        hanoi(n - 1, start, end, via) # 第一步：借助目标柱，把上面(n - 1)个圆片挪到辅助柱上
        print(f"{start} -> {end}") # 第二步，直接把起始柱上剩下的最大圆片一把挪到目标柱上
        hanoi(n - 1, via, start, end) # 第三步：借助现在已经空了的起始柱，把辅助柱上(n - 1)个圆片挪到目标柱


def main():
    print(arithmetic(2, 3, 5)) # 14
    print(fibonacci(10)) # 55
    print(fibonacci(20)) # 6765
    print(fibonacci_1(10)) # 55
    print(fibonacci_1(20)) # 6765
    print(fibonacci_2(10)) # 55
    print(fibonacci_2(20)) # 6765
    hanoi(4, 'a', 'b', 'c')


if __name__ == "__main__":
    main()