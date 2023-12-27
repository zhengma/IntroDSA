package demo.tree;

import java.util.ArrayList;
// import demo.tree.*;

public class TreeTest {
  public static void main(String[] args) {
    String nodes = "ABCDEFGHIJKL";
    BinaryTreeNode<Character>[] testTree = new BinaryTreeNode[12];
    for (int i = 0; i < nodes.length(); i++) {
      testTree[i] = new BinaryTreeNode<Character>(nodes.charAt(i));
    }

    testTree[0].setLeft(testTree[1]);
    testTree[0].setRight(testTree[2]);
    testTree[1].setLeft(testTree[3]);
    testTree[1].setRight(testTree[4]);
    testTree[2].setLeft(testTree[5]);
    testTree[2].setRight(testTree[6]);
    testTree[3].setLeft(testTree[7]);
    testTree[3].setRight(testTree[8]);
    testTree[4].setLeft(testTree[9]);
    testTree[4].setRight(testTree[10]);
    testTree[5].setLeft(testTree[11]);
    BinaryTreeNode<Character> root = testTree[0];

    ArrayList<Character> pre = new ArrayList<Character>();
    root.preOrder(pre);
    System.out.println(pre);

    ArrayList<Character> in = new ArrayList<Character>();
    root.inOrder(in);
    System.out.println(in);

    ArrayList<Character> post = new ArrayList<Character>();
    root.postOrder(post);
    System.out.println(post);

    ArrayList<Character> lvl = new ArrayList<Character>();
    root.levelOrder(lvl);
    System.out.println(lvl);
  }
}
