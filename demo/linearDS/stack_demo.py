def reverse_stack(old_stack: list) -> list:
    new_stack = []
    while old_stack:
        new_stack.append(old_stack.pop())
    return new_stack

stack = []
stack.append(8)
stack.append(5)
stack.append(2)
print(stack)
print(stack.pop())
print(stack)

stack = [8, 5, 2, 6]
print(stack)
print(reverse_stack(stack))