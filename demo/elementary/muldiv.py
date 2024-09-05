"""
回答学生提问: "在一个没有乘除法指令的指令集 (比如'CAIE指令集')上,
能否只用加减和其它位运算达到乘除法的效果?"

也适宜于让学生自己分析以下代码为何能奏效.

作者: 马正
组织: 渊学通教育广州分校
创建日期: Apr. 1, 2024
最后修改日期: Sep. 1, 2024
Python版本: 3.12
"""

def mul_unsigned(a: int, b: int) -> int:
    """模拟在精简指令集上计算两个整数 (其中之一应为非负整数) 的积.

    运算指令只用到 ADD, AND, LSL 和 LSR.

    Args:
        a (int): 被乘数, 任意整数.
        b (int): 乘数, 须为非负整数.

    Returns:
        int: a * b 的结果.
    """
    product = 0
    while b > 0:
        if b & 1:
            product += a
        b >>= 1
        a <<= 1
    return product

def mul(a: int, b: int) -> int:
    """模拟在精简指令集上计算两个整数的积.

    运算指令只用到 ADD, AND, INC, LSL, LSR 和 NOT.

    Args:
        a (int): 被乘数, 可为任意整数.
        b (int): 乘数, 可为任意整数.

    Returns:
        int: a * b 的结果.
    """
    if b >= 0:
        return mul_unsigned(a, b)
    return ~mul_unsigned(a, ~b + 1) + 1

def div_unsigned(a: int, b: int) -> tuple[int, int]:
    """模拟在精简指令集上计算两个非负整数的商和余数.

    运算指令只用到 SUB, INC, LSL 和 LSR.

    Args:
        a (int): 被除数, 须为非负整数.
        b (int): 除数, 须为正整数.

    Returns:
        tuple[int, int]: (q, r) 分别为 a ÷ b 的商和余数.
            相当于 (a // b, a % b)
    """
    q = 0
    b_temp = b
    while b <= a:
        b <<= 1
    while (b ^ b_temp) != 0:
        b >>= 1
        q <<= 1
        if b <= a:
            a -= b
            q += 1
    return (q, a)

def div(a: int, b: int) -> tuple[int, int]:
    """模拟在精简指令集上计算两个整数的商和余数. 

    运算指令只用到 SUB, INC, LSL, LSR, NOT 和 XOR.

    Args:
        a (int): 被除数, 任意整数.
        b (int): 除数, 任意非零整数.

    Returns:
        tuple[int, int]: (q, r) 分别为 a ÷ b 按C/C++/Java等语言规则的商和余数
    """
    q, r = div_unsigned(a if a >= 0 else ~a + 1, b if b > 0 else ~b + 1)
    if a ^ b < 0:
        q = ~q + 1
    if a < 0:
        r = ~r + 1
    return (q, r)

def div_python(a: int, b: int) -> tuple[int, int]:
    """计算两个整数按 Python 规则的商和余数.
    
    在Python中, 若 b < 0, 则 {@code b < (a % b) <= 0}.
    无论如何, 仍总有 {@code a == b * (a // b) + (a % b)}.

    Args:
        a (int): 被除数, 任意整数.
        b (int): 除数, 任意非零整数.

    Returns:
        tuple[int, int]: (q, r) 分别为 a ÷ b 按Python规则的商和余数.
            相当于 (a // b, a % b)
    """
    q, r = div(a, b)
    q_offset, r_offset = div(r + b, b)
    return (q + q_offset - 1, r_offset)

print(f"(-14) x 11 = {mul_unsigned(-14, 11)}")
print(f"(-14) x 0 = {mul_unsigned(-14, 0)}")
print(f"0 x 11 = {mul_unsigned(0, 11)}")
# for divident in range(89):
#    print(f"{divident} ÷ 11 = {division(divident, 11)}")
print(f"81 ÷ 11 = {div_unsigned(81, 11)}")

print(f"(-14) x (-11) = {mul(-14, -11)}")
print(f"14 x (-11) = {mul(14, -11)}")

print(f"81 ÷ (-11) = {div(81, -11)}")
print(f"81 ÷ (-11) = {div_python(81, -11)} in Python")
