import java.util.*;

public class SelectionSort {
  
  public static void sort(int[] arr) {
    int n = arr.length;
    for (int boundary = 0; boundary < n - 1; boundary++) {
      int minIdx = boundary;
      for (int i = boundary + 1; i < n; i++) {
        if (arr[i] < arr[minIdx]) {
          minIdx = i;
        }
      }
      int temp = arr[minIdx];
      arr[minIdx] = arr[boundary];
      arr[boundary] = temp;
    }
  }

  public static void sort(List<Integer> lst) {
    int n = lst.size();
    for (int boundary = 0; boundary < n - 1; boundary++) {
      int minIdx = boundary;
      for (int i = boundary + 1; i < n; i++) {
        if (lst.get(i) < lst.get(minIdx)) {
          minIdx = i;
        }
      }
      Collections.swap(lst, boundary, minIdx);
    }
  } 

  public static void main(String[] args) {
    int arr[] = {3, 8, 2, 6, 2, 9, 4, 1, 9, 5};
    List<Integer> lst = new ArrayList<Integer>
        (Arrays.asList(8, 5, 2, 6, 4, 7, 1, 3));
    System.out.println("Before: " + Arrays.toString(arr));
    sort(arr);
    System.out.println("After: " + Arrays.toString(arr));
    System.out.println("Before: " + lst);
    sort(lst);
    System.out.println("After: " + lst);
  }
}
