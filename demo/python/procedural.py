# 任务: 找到2~100的所有质数, 并显示出来, 十个一行.
# 质数的判断方法：对于自然数n, 如果从2到根号n的所有数都没法整除它, 就是质数了.

# 非过程化的写法
def main_noprocedural():
    output_counter = 0
    for n in range(2, 101):
        upper = int(n ** 0.5) + 1 # 最高检查到根号n
        isprime = True # 一开始是True, 查到能被整除就是false
        for d in range(2, upper):
            if n % d == 0:
                isprime = False
        if isprime:
            print(n, end = '\t')
            output_counter += 1
            if output_counter >= 10:
                print('\n')
                output_counter = 0

# 缺点：所有的功能都搅在一起, 难以阅读理解, 而且万一出错也很难纠错. 

# 面向过程的思路：
# 把任务分解为“找到质数”和“输出质数”两个环节, 分别写成procedure (Python中统一称为function). 而在主代码里只是调用这两个过程. 
# “寻找一定范围里所有质数”可以拆分出一个子任务：给定n, 判断它是不是质数 True/False

def isprime(n: int) -> bool:
    upper = int(n ** 0.5) + 1
    for d in range(2, upper):
        if n % d == 0:
            return False
    return True

def find_primes(start: int, end: int) -> list:
    primes = []
    for n in range(start, end + 1):
        if isprime(n):
            primes.append(n) # 注意这里append也是Python自己已经写好了的procedure，这里就直接调用了
    return primes

def printing(lst: list, per_line: int):
    output_counter = 0
    while lst: # 只要lst还没全部输出
        print(lst.pop(0), end = '\t')
        output_counter += 1
        if output_counter >= per_line:
            print('\n')
            output_counter = 0

def main_procedural():
    printing(find_primes(2, 100), 10)

if __name__ == "__main__":
    # main_noprocedural()
    main_procedural()