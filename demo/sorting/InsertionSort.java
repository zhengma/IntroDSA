import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class InsertionSort {

  /**
   * 插入排序算法演示.

   * @param arr {@code int[]} 待排序的数组.  执行完毕后列表本身变为已排好序的.
   */
  public static void sort(int[] arr) {
    int size = arr.length;
    for (int p = 1; p < size; p++) {
      for (int i = 0; i < p; i++) {
        if (arr[p] <= arr[i]) {
          int temp = arr[p];
          for (int j = p - 1; j >= i; j--) {
            arr[j + 1] = arr[j]; 
          }
          arr[i] = temp;
          break;
        } 
      }
    }
  }

  public static void sort(List<Integer> lst) {
    int size = lst.size();
    for (int p = 1; p < size; p++) {
      for (int i = 0; i < p; i++) {
        if (lst.get(p) <= lst.get(i)) {
          lst.add(i, lst.remove(p));
        }
      }
    }
  }

  public static void main(String[] args) {
    int[] arr = { 3, 8, 2, 6, 2, 9, 4, 1, 9, 5 };
    System.out.println("Before: " + Arrays.toString(arr));
    sort(arr);
    System.out.println("After: " + Arrays.toString(arr));
    List<Integer> lst = new ArrayList<Integer>(Arrays.asList(
        8, 5, 2, 6, 4, 7, 1, 3));

    System.out.println("Before: " + lst);
    sort(lst);
    System.out.println("After: " + lst);
  }
}
