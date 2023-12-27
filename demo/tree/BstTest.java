package demo.tree;

import java.util.Arrays;
import java.util.ArrayList;

public class BstTest {
  public static void main(String[] args) {
    ArrayList<Integer> lst = new ArrayList<Integer>
		  (Arrays.asList(3, 8, 2, 6, 1, 9, 4, 9, 5));
    BinarySearchTree testTree = new BinarySearchTree<Integer>(lst);
    System.out.println(testTree.check_BST());
    System.out.println(testTree.sorted());
    System.out.println("Left rotate: ");
    testTree.leftRotate();
    System.out.println(testTree.sorted());
    System.out.println(testTree.check_BST());
    System.out.println("Right rotate: ");
    testTree.rightRotate();
    System.out.println(testTree.sorted());
    System.out.println(testTree.check_BST());
  }

}