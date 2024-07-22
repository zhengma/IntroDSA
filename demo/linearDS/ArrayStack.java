/**
 * 演示如何用数组实现一个堆栈.
 * 不失一般性，堆栈的元素被限制在整型的基本类型.
 * 当学生学完泛型的基础知识点后, 可以尝试改写一个 {@code ArrayStack<E>} 的版本.

 * @author 马正
 */

public class ArrayStack {

  private static final int MAX_SIZE = 256;

  private int[] data = new int[MAX_SIZE];
  private int ptr; // 指向栈顶的指针. 下一个push进来的元素就写在data[ptr]这里
  
  public ArrayStack() {
    this.ptr = 0;
  }

  public boolean isEmpty() {
    return this.ptr == 0;
  }
  
  /**
   * 入栈.

   * @param val {@code int} 待入栈的值
   * @return {@code boolean} 取值为true当且仅当入栈成功.
   */
  public boolean push(int val) {
    if (ptr >= MAX_SIZE) {
      System.out.println("Stack is full!");
      return false;
    } else {
      this.data[ptr] = val;
      this.ptr++;
      return true;
    }
  }

  /**
   * 出栈.

   * @return {@code int} 若栈非空则返回弹出的值, 否则返回-1。
   */
  public int pop() {
    if (isEmpty()) {
      System.out.println("Stack is empty!");
      return -1;
    } else {
      this.ptr--;
      return this.data[ptr];
    }
  }
  /**
   * 返回栈顶的值, 但不弹出.

   * @return {@code int} 若栈非空则返回栈顶的值, 否则返回-1.
   */
  public int peek() {
    if (isEmpty()) {
      System.out.println("Stack is empty!");
      return -1;
    } else {
      return this.data[ptr];
    }
  }
  
  /**
   * 显示堆栈的全貌.
   */
  public String toString() {
    String s = "[";
    for (int i = 0; i < ptr - 1; i++) {
      s += String.valueOf(this.data[i]);
      s += ", ";
    }
    return s + String.valueOf(this.data[ptr - 1]) + "]";
  }

  /**
   * 测试一组数据.
   */
  public static void main(String[] args) {
    ArrayStack stack = new ArrayStack();
    System.out.print("Initially the stack is empty: ");
    System.out.println(stack);
    int[] testData = { 8, 5, 2, 6, 4 };
    for (int num : testData) {
      stack.push(num);
    }
    System.out.print("The stack now is: ");
    System.out.println(stack);
    System.out.println("Pop the top element: " + stack.pop());
    System.out.print("And the stack becomes: ");
    System.out.println(stack);

    ArrayStack stackReversed = new ArrayStack();
    while (!stack.isEmpty()) {
      stackReversed.push(stack.pop());
    }
    System.out.print("Stack in reverse order: ");
    System.out.println(stackReversed);
  }
}
