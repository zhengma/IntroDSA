from linkedlist import SinglyLinkedList


def test_init(tested_class):
   test_list = tested_class([1, 3, 4, 7, 9])
   str_output = f"""{'-'*20} Initialization {'-'*20}
The list is now: {test_list}
Its length is: {len(test_list)}
"""
   return str_output


def test_get(tested_class):
    test_list = tested_class([1, 3, 4, 7, 9])
    str_output = f"""{'-'*20} Get Elements and Slices {'-'*20}
The full list: {test_list}
The element of index 2 is: {test_list[2]}
The slice [2:4] is: {test_list[2:4]}
The slice [:4] is: {test_list[:4]}
The slice [2:] is: {test_list[2:]}
The slice [::2] is: {test_list[::2]}
Attempting to access [7]: {test_list[7]}
"""
    return str_output


def test_set(tested_class):
    test_list = tested_class([1, 2, 3, 4, 5, 6, 7, 8, 9])
    str_output = f"""{'-'*20} Set Elements and Slices {'-'*20}
The full list: {test_list}
"""
    test_list[3] = 10
    str_output += f'Set element [2] to 10: {test_list}\n'
    test_list[5] += 10
    str_output += f'Add 10 to element [5]: {test_list}\n'
    test_list[:2] = [15, 15]
    str_output += f'Set the first two elements to 15: {test_list}\n'
    return str_output


def test_insert(tested_class):
    test_list = tested_class([1, 3, 5, 7, 9])
    str_output = f"""{'-'*20} Insert Elements {'-'*20}
The full list: {test_list}
insert(0, 2), (2, 4), (7, 6) and (10, 8), the last one shall raise an exception.
The list should've become: 21435796 of length 8.
"""
    test_list.insert(0, 2)
    test_list.insert(2, 4)
    test_list.insert(7, 6)
    test_list.insert(10, 8)
    str_output += f'And it actually is: {test_list} of length {len(test_list)}\n'
    return str_output


def test_sort(tested_class):
    test_list = tested_class([2, 1, 4, 3, 5, 7, 9, 6])
    str_output = f"""{'-'*20} Sort Elements {'-'*20}
The unsorted list: {test_list}
The sorted list: {test_list.sort()}
    """
    return str_output


def test_pop(tested_class):
    test_list = tested_class([2, 1, 4, 3, 5, 7, 9, 6])
    str_output = f"""{'-'*20} Pop Elements {'-'*20}
The original list: {test_list}
pop(): {test_list.pop()}
After pop(): {test_list}
pop(1): {test_list.pop(1)}
After pop(1): {test_list}
Attempting pop(9): {test_list.pop(9)}
After attempting pop(9): {test_list}
And the length now is: {len(test_list)}
"""
    return str_output


def test_search(tested_class):
    test_list = tested_class([1, 3, 5, 7, 9])
    str_output = f"""{'-'*20} Search and Remove Elements {'-'*20}
The original list: {test_list}
index(5): {test_list.index(5)}
index(6): {test_list.index(4)}
remove(7): {test_list.remove(7)}
Attempting remove(8): {test_list.remove(8)}
After removal: {test_list} with a length {len(test_list)}
"""
    return str_output


def test_reverse(tested_class):
    test_list = tested_class([1, 3, 5, 7, 9])
    str_output = f"""{'-'*20} Reverse List {'-'*20}
The original list: {test_list}
The reversed list: {test_list.reverse()}
"""
    return str_output

def test_add(tested_class):
    test_list1 = tested_class([1, 3, 5])
    test_list2 = tested_class([2, 4, 6])
    str_output = f"""{'-'*20} Concatenate List {'-'*20}
The list #1: {test_list1}
The list #2: {test_list2}
The combined list: {test_list1 + test_list2}
"""
    return str_output

sections = [
    test_init, 
    test_get,
    test_set,
    test_insert,
    test_sort,
    test_pop,
    test_search,
    test_reverse,
    test_add
]

for section in sections:
    print(section(SinglyLinkedList))