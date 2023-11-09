class ScoreReport: # Python 中类的声明: "class + 名字"

    def __init__(self, name: str, id: str):
        # 类的构造器是一个特殊的方法, 在新建实例的时候自动运行。
        # 因为Python的变量可以不经声明直接使用, 所以类的属性必须在构造器里明确写出来
        # 如果要强调一个函数是类的方法而不是孤立的函数, 函数的第一个参数必须是"self"
        # 后面要使用同一个类中其它的属性和方法, 也必须写成"self.属性或方法名"
        # 构造器还可以设置一些其它参数, 新建实例被运行的时候, 从外界读入一些数据, 填入属性
        self.name = name # 新建一个名叫name的属性, 并把外界给的相应字符串填进去
        # "self."开头的是类的属性, 右边的name是构造器作为一个方法的parameter
        self.id = id
        self.marks = {'English': 0, 'Math': 0, 'Physics': 0, 'CS': 0}
        # 虽然在新建成绩单的时候, 不用马上填分数, 但是也要把待填分数的属性初始化

    def calculate_average(self):
        self.average = sum(self.marks.values())/len(self.marks)
        # 随堂测试：写'/len(self.marks)', 而不直接写'/4', 有啥优点? 



class ScoreReport2: 

    def __init__(self, name: str, id: str):
        self.__name = name # Python中，如果想表示某个属性“外人最好不要直接乱动”，就在名字前面加两个下划线
        self.__id = id
        self.__marks = {'English': 0, 'Math': 0, 'Physics': 0, 'CS': 0}

    def get_mark(self, subject: str) -> int: # 读取属性返回给外界的method，称为getter
        try:
            return self.__marks[subject]
        except KeyError:
            print(f'No subject named \'{subject}\'!')
            return -1

    def set_mark(self, subject: str, new_mark: int): # 修改属性取值的method，称为setter
        try:
            if new_mark <= 100 and new_mark >= 0:
                self.__marks[subject] = new_mark
            else:
                raise ValueError("Marks are between 0 and 100!")
        except KeyError:
            print(f'No subject named \'{subject}\'!')
        except ValueError as e:
            print(e)

    def __calculate_average__(self): # 不希望其它对象直接调用的方法，前后各加两个下划线
        self.__average = sum(self.__marks.values())/len(self.__marks)

    def __no_private_method__(self): # 这个方法前后加了双下划线，看看能否从外界调用
        print('I have double hyphen front and rear, but I still get called from the outside!')

    def get_average(self):
        self.__calculate_average__()
        return self.__average


def main():
    pony = ScoreReport('Zheng', '05322001')
    justin = ScoreReport('Zhaomiao', '123')
    # 以上用ScoreReport这个类作为模板，新建了两个不同的，互相独立的实例

    print(f'The real name of Pony is {pony.name}.')
    print(f'The real name of Justin is {justin.name}.')
    # 可见两个对象都有name这项属性，但取值不同

    pony.marks['English'] = 89
    print(pony.marks)
    # 因为 marks 这个列表已经在__init__里新建了，所以可以往里面填入值

    pony.grade = 'A'
    print(pony.grade)
    try:
        print(justin.grade)
    except AttributeError:
        print('The object \'justin\' has no grade.')
    # Python中，一个类的实例新建之后，可以添加__init__之中没有提到的新属性
    # 但是同一个类的其它实例并不会因此多出这个新属性

    pony.calculate_average()
    print(pony.average)

    pony2 = ScoreReport2('Zheng', '05322001')
    pony2.set_mark('English', 88)
    print(pony2.get_mark('Chemistry'))
    print(pony2.get_mark('English'))
    try:
        print(pony2.__marks)
    except AttributeError as e:
        print(e)
    # Python会阻止开头带了双下划线的属性的访问

    pony.__no_private_method__()
    # 但是带了前后双下划线的方法还是可以访问

    pony.set_mark('Physics', 109) # data validation，阻止了超出范围的数值填入分数栏
    pony.set_mark('Physics', 90)
    print(pony.get_average())

if __name__ == "__main__":
    main()