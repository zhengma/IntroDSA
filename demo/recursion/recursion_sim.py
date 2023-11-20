"""
手动模拟编译器实现递归调用的原理

为《CAIE A level 计算机科学》(9618) 编写.

主要教学目的:
1. 演示第 19.2.2节 《编译器是如何实现递归的》中相关的考点
2. 展示 "编译器能自动妥善处置递归调用" 一事给程序员带来的极大便利
3. 复习堆栈的性质

作者: 马正
组织: 渊学通教育广州分校, 上海科桥教育
创建日期: Nov. 20, 2023
最后修改日期: Nov. 20, 2023
Python版本: 3.12
"""


def factorial_recursion_sim(n: int) -> int:
    """
    模拟编译器对 "递归求非负整数的阶乘" 的函数分步骤拆解的大致原理.

    复习: 递归写法是:
        `if n == 0: return 1 else return n * factorial(n-1)`
        

    参数:
        n (int): 需要求阶乘的非负整数

    返回:
        int: n! 的计算结果
    """
    ret = None  # 刚开始没有返回值
    stack = []  # 刚开始堆栈为空
    arg = n  # 刚开始函数的实参值设为n
    while not ret or stack:  # 循环到返回值出来，且堆栈腾空为止
        if ret:  # 如果已经算完了某一层的(k-1)!
            arg = stack.pop()  # 弹出上一层的参数 k
            ret *= arg  # 计算 k * (k-1)! 作为返回值
        # 如果ret == None, 还没开始算，就仍然处于递归调用的环节
        elif arg == 0:  # base case
            ret = 1
        else:
            stack.append(arg)  # 当前参数压入堆栈
            arg -= 1  # 把当前的参数 - 1, 然后从头开始执行
    return ret


def hanoi_recursion_sim(n: int, start: str, via: str, end: str) -> None:
    """
    模拟编译器对 "递归解决汉诺塔问题" 的函数分步骤拆解的大致原理.

    复习: 汉诺塔的base case 是 `n = 1`.
    `n > 1`时的递归写法分三行, 以下给每行加了编号:
        `0: hanoi(n - 1, start, end, via)`
        `1: print(start -> end) `
        `2: hanoi(n - 1, via, start, end)`

    参数:
        n (int): 层数
        start (str): 起始柱的名称, 刚开始所有圆片都串在这个柱子上
        via (str): 辅助柱的名称
        end (str): 目标柱的名称, 游戏结束时所有圆片都要串到这个柱子上
    """
    # 函数在某时刻的状态主要包括 "运行到了哪一步" 和 "各内部变量包括参数的值"
    # 这里把它们汇总在一个dict中. 其中'pc'记录运行到了哪一步,
    # 得名于《汇编语言》一章中的 "Program Counter register"
    status = {'pc': 0, 'n': n, 'start': start, 'via': via, 'end': end}
    stack = []

    # 循环到最外层运行结束
    while not (status['n'] == n and status['pc'] == 3):
        if status['n'] == 1:  # base case
            print('{start} -> {end}'.format(**status))
            if stack:  # 若堆栈非空（不加这个条件，n = 1时会出错）
                status = stack.pop()  # base case 运行结束, 弹出之前的状态
                status['pc'] += 1  # 并进入下一步
            else:
                break
        else:  # 否则开始递归
            match status['pc']:  # 看运行到了哪一步
                case 0:  # 0: hanoi(n - 1, start, end, via)
                    stack.append(status)  # 此刻的状态压入堆栈
                    # 构建新的状态, pc设到第0步
                    new_status = {'pc': 0, 'n': status['n'] - 1,
                                  'start': status['start'],
                                  'via': status['end'],
                                  'end': status['via']}
                    # 把当前状态改为新状态 (相当于递归调用并传入新的一组实参)
                    status = new_status
                case 1:  # 1: print(start -> end)
                    print('{start} -> {end}'.format(**status))
                    status['pc'] += 1  # 执行1号语句后, 步数+1
                case 2:  # 2: hanoi(n - 1, via, start, end)
                    stack.append(status)
                    new_status = {'pc': 0, 'n': status['n'] - 1,
                                  'start': status['via'],
                                  'via': status['start'],
                                  'end': status['end']}
                    status = new_status
                case 3:  # 到达这次调用的末尾
                    status = stack.pop()  # 把外层调用的状态弹出堆栈
                    status['pc'] += 1  # 这时执行完了外层的0号或2号语句, 步数+1


if __name__ == "__main__":
    print(factorial_recursion_sim(7))
    hanoi_recursion_sim(4, 'a', 'b', 'c')
