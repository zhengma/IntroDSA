from binarytree import TreeNode

class ExpressionTree():
    """ 结合CIE A2 16.3节《编译原理》的内容，
        将正常书写的表达式 (只含标识符和常见运算符) 拆解,
        构成表达式二叉树 (expression binary tree), 
        并输出为逆波兰记法 (RPN) 
    """
    
    def __init__(self, expression: str):
        self.__root = self.make_tree(self.expression_lexical(expression))

    def expression_lexical(self, s_raw: str) -> list:
        """词法分析器

        Args:
            s_raw (str): 一个字符串, 内容为一条表达式, 
            只包含三种东西：
            1. 由字母数字和下划线组成的标识符
            2. 常见运算符 +-*/%
            3. 小括号
            所有空格都会在预处理时被删去

        Returns:
            list: 字符串中所有词法单元组成的列表，按书写顺序排列
                小括号内的表达式作为嵌套的子列表存储
        Examples:
        > expression_lexical('(a + b) * (c + d) * e')
        [['a', '+', 'b'], '*', ['c', '+', 'd'], '*', 'e']
        """
        OPERATORS = '+-*/%'
        LEFT_PAR = '('
        RIGHT_PAR = ')'
        tokens = []
        s = s_raw.replace(" ", "")
        index = 0
        while index < len(s):
            if s[index] in OPERATORS:
                tokens.append(s[index])
                index += 1
            elif s[index].isalnum() or s[index] == '_':
                end_id = index + 1
                while end_id < len(s) and (s[end_id].isalnum() or s[end_id] == '_'):
                    end_id += 1
                tokens.append(s[index:end_id])
                index = end_id
            elif s[index] == LEFT_PAR:
                layers = 1
                for matching_par in range(index+1, len(s)):
                    if s[matching_par] == LEFT_PAR:
                        layers += 1
                    if s[matching_par] == RIGHT_PAR:
                        layers -= 1
                    if layers == 0:
                        break
                if s[matching_par] != RIGHT_PAR:
                    print('Parenthesis unmatch!')
                else:
                    tokens.append(self.expression_lexical(s[index+1:matching_par]))
                    index = matching_par + 1
            else:
                print('Invalid symbol!')
                return []
        return tokens

    def priority(self, op: str) -> int:
        if op in '*/%':
            return 0
        else:
            return 1
    
    def subtree(self, ops: list, items: list) -> TreeNode:
        root = TreeNode(ops.pop())
        root.pright = items.pop()
        root.pleft = items.pop()
        return root

    def make_tree(self, tokens: list) -> TreeNode:
        OPERATORS = '+-*/%'
        items = []
        ops = []
        while tokens:
            if type(tokens[0]) is list:
                items.append(self.make_tree(tokens.pop(0)))
            elif tokens[0] not in OPERATORS:
                items.append(TreeNode(tokens.pop(0)))
            else:
                while len(ops) > 0 and self.priority(tokens[0]) > self.priority(ops[-1]):
                    items.append(self.subtree(ops, items))
                ops.append(tokens.pop(0))
        while len(items) > 1:
            items.append(self.subtree(ops, items))
        return items[0]
    
    def RPN(self):
        return self.__root.post_order()

def main():
    test_expr = ExpressionTree('a - b * c + d * e')
    print(test_expr.RPN())
    test_expr2 = ExpressionTree('(a - b) * (c + d) / e')
    print(test_expr2.RPN())

if __name__ == "__main__":
    main()