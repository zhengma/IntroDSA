class BinarySearch {

  public static int binarySearchRecursion(int[] nums, int target, int start, int end) {
    // nums: 已经从小到大排好序的array
    // 任务：从nums的编号介于 start 和 end 的元素中查找 target 这个数字
    // 如果找到了，返回编号；如果没找到，返回-1
    if (start > end) {
      return -1; // 如果待查找序列的长度为0甚至为负数，就是没找到
    } else {
      int mid = (start + end) / 2; // mid 是待查找的这段的中点
      System.out.println("Looking at: " + nums[mid]);
      // 这是让Jessica看清：搜索过程中检查了哪几个数字
      if (target == nums[mid]) {
        return mid; // 如果mid这个位置恰好是待查找的数字，直接返回这个编号
      } else if (target < nums[mid]) {
        // 如果目标数字比mid这里的数字要小，对左半截进行搜索
        // 左半截的起点还是整段的起点，终点是 mid 的左边一格
        return binarySearchRecursion(nums, target, start, mid - 1);
      } else {
        // 如果目标数字比mid这里的数字要小，对右半截进行搜索
        return binarySearchRecursion(nums, target, mid + 1, end);
      }
    }
  }
    
  public static int binarySearch(int[] nums, int target) {
    // 由于没有自己调用自己，所以parameter中不需要指定头尾
    int start = 0;
    int end = nums.length - 1;
    int mid;
    while (start <= end) { // 只要搜索范围长度大于零，
      // 每次如果没找到，就通过修改 start 和 end 缩小范围
      mid = (start + end) / 2;
      if (target == nums[mid]) {
        return mid; // 找到就返回
      } else if (target < nums[mid]) {
        end = mid - 1; // target较小，start不动，end 变为中点左边，相当于取左半截
      } else {
        start = mid + 1; // target 较大，end不动，start 变为中点右边，取右半截
      }
    }
    return -1; // 始终没找到，返回-1
  }
    
  public static void main(String[] args) {
    int[] testarr = {2, 3, 5, 7, 11, 13, 17, 19, 23};
    System.out.println(binarySearchRecursion(testarr, 6, 0, testarr.length - 1));
    System.out.println(binarySearch(testarr, 6));
  }
}