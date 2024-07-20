public class MergeSort {
    
  public static void mergeSort(int[] data, int start, int end) {
    // 注意：end 不作为“最后一个元素的编号”，而是最后一个元素的编号 + 1
    // 这样比较方便
    if (end - start > 1) { // start + 1 == end，是只有一个元素的base case，这时不需要做任何事
      int mid = start + (end - start) / 2; // 右半截的开头
      mergeSort(data, start, mid); // 把左半截排好序
      mergeSort(data, mid, end); // 把右半截排好序
      merge(data, start, mid, end); // 合并左右两截
    }
  }
    
  public static void merge(int[] data, int start, int mid, int end) {
    // 先新建两个array，分别存储左半截和右半截
    // 左右半截长度，如果Jessica考试时忘了结论，就找一组具体的数试一下
    int[] left = new int[mid - start];
    int[] right = new int[end - mid];
    // 把左右两个半截分别拷进去
    for (int i = 0; i < left.length; i++) {
      left[i] = data[i + start];
    }
    for (int i = 0; i < right.length; i++) {
      right[i] = data[i + mid];
    }
    // 准备好两个指针：
    int l = 0;
    int r = 0;
    // 直接把数据写回原本的 data 数组，所以还需要一个指针，决定写入位置
    int p = start;
    while (l < left.length || r < right.length) { // 只要两个半截的array没有都走完
      if ((l < left.length) && (r == right.length || left[l] <= right[r])) {
        // 从左半截拷一个元素的条件是：
        // 1. 左半截没有走完
        // 2. 要么右半截走完了，要么左边指针指的数字小于右边指针指的
        data[p] = left[l]; // 把左半截正在被指着的元素拷到原数组的待写入位置处
        l++; // 左半截的指针往右挪一格
      } else {
        // 只要两个半截没有都走完，而不从左边拷元素，就从右边拷
        data[p] = right[r];
        r++;
      }
      p++; // 无论从哪边拷元素，写入位置总往右挪一格
    }
  }
    
  public static void main(String[] args) {
    int[] arr = {8, 5, 2, 6, 4, 7, 1, 3};
    System.out.println("Before: ");
    for (int n : arr) {
      System.out.print(n);
      System.out.print('\t');
    }
    System.out.println("");
    mergeSort(arr, 0, arr.length);
    System.out.println("After: ");
    for (int n : arr) {
      System.out.print(n);
      System.out.print('\t');
    }
    System.out.println("");
  }
}