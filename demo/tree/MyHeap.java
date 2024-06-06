package demo.tree;

import java.util.*;

class MyHeap<E extends Comparable<E>> {
  private ArrayList<E> heap;

  public MyHeap() {
    heap = new ArrayList<E>();
  }

  public MyHeap(Collection<E> rawEs) {
    heap = new ArrayList<E>();
    heap.add(null);
    heap.addAll(rawEs);
    this.heapify();
  }

  public boolean isEmpty() {
    return heap.size() <= 1;
  }

  private int left(int index) {
    return (index << 1 < heap.size()) ? index << 1 : 0;
  }

  private int right(int index) {
    return ((index << 1) + 1 < heap.size()) ? (index << 1) + 1 : 0;
  }

  private void percolate_down(int i) {
    while (left(i) != 0) {
      if (right(i) != 0 
          && heap.get(left(i)).compareTo(heap.get(right(i))) < 0
          && heap.get(i).compareTo(heap.get(right(i))) < 0) {
        Collections.swap(heap, i, right(i));
        i = right(i);
      } else if (heap.get(i).compareTo(heap.get(left(i))) < 0) {
        Collections.swap(heap, i, left(i));
        i = left(i);
      } else {
        break;
      }
    }
  }

  public void heapify() {
    for (int index = (heap.size() + 1) >> 1; index > 0; index--) {
      percolate_down(index);
    }
  }

  public void insert(E newE) {
    heap.add(newE);
    int index = heap.size() - 1;
    while (index >= 2 && heap.get(index).compareTo(heap.get(index >> 1)) > 0) {
      Collections.swap(heap, index, index >> 1);
      index >>= 1;
    }
  }

  public E delete(int index) {
    Collections.swap(heap, index, heap.size() - 1);
    E removed = heap.remove(heap.size() - 1);
    percolate_down(index);
    return removed;
  }

  public E pop() {
    return delete(1);
  }

  public ArrayList<E> sort() {
    ArrayList<E> backup = new ArrayList<E>();
    backup.addAll(this.heap);
    ArrayList<E> sorted = new ArrayList<E>();
    while (!isEmpty()) {
      sorted.add(pop());
    }
    heap = backup;
    return sorted;
  }

  public void print() {
    int start = 1;
    int end;
    while (start < heap.size()) {
      end = (start << 1 < heap.size()) ? start << 1 : heap.size();
      System.out.println(heap.subList(start, end));
      start = end;
    }
  }

  public static void main(String[] args) {
    Integer[] rawData = {1, 3, 8, 2, 6, 9, 4, 2};
    MyHeap<Integer> testh = new MyHeap<Integer>(Arrays.asList(rawData));
    testh.print();
    testh.insert(12);
    testh.print();
    System.out.println(testh.delete(3));
    testh.print();
    System.out.println(testh.pop());
    testh.print();
    System.out.println(testh.sort());
    testh.print();

    Random rand = new Random();
    ArrayList<Integer> largeTestSet = new ArrayList<Integer>();
    for (int i = 0; i < 127; i++) {
      largeTestSet.add(rand.nextInt(1000));
    }
    MyHeap<Integer> largeTestHeap = new MyHeap<Integer>(largeTestSet);
    System.out.println(largeTestHeap.sort());
  }
}