from typing import TypeVar

V = TypeVar("V")

class Heap:

    heap: list[V]

    def __init__(self, original: list[V]):
        self.heap = [None] + original.copy()
        self.heapify()

    def isempty(self) -> bool:
        return len(self.heap) <= 1

    def left(self, index: int) -> int:
        if index * 2 >= len(self.heap):
            return None
        return index * 2

    def right(self, index: int) -> int:
        if index * 2 + 1 >= len(self.heap):
            return None
        return index * 2 + 1

    def swap(self, i1: int, i2: int) -> None:
        temp = self.heap[i1]
        self.heap[i1] = self.heap[i2]
        self.heap[i2] = temp

    def percolate_down(self, index: int) -> None:
        while self.left(index):
            if (self.right(index) and
                self.heap[self.left(index)] < self.heap[self.right(index)] and
                self.heap[index] < self.heap[self.right(index)]):
                self.swap(index, self.right(index))
                index = self.right(index)
            elif self.heap[index] < self.heap[self.left(index)]:
                self.swap(index, self.left(index))
                index = self.left(index)
            else:
                break

    def heapify(self) -> None:
        for index in range((len(self.heap)+1)//2, 0, -1):
            self.percolate_down(index)

    def print(self) -> None:
        layer_border = 1
        while layer_border < len(self.heap):
            print(self.heap[layer_border:2 * layer_border])
            layer_border *= 2

    def insert(self, new: V) -> None:
        self.heap.append(new)
        index = len(self.heap) - 1
        while index >= 2 and self.heap[index] > self.heap[index // 2]:
            self.swap(index, index // 2)
            index //= 2

    def delete(self, index: int) -> V:
        self.swap(index, len(self.heap) - 1)
        removed = self.heap.pop()
        self.percolate_down(index)
        return removed

    def pop(self) -> V:
        return self.delete(1)

testh = Heap([1, 3, 8, 2, 6, 9, 4, 2])
testh.print()
testh.insert(12)
testh.print()
print(testh.delete(3))
testh.print()
print(testh.pop())
testh.print()

sorted_list = []
while not testh.isempty():
    sorted_list.append(testh.pop())
print(sorted_list)
