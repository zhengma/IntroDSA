package demo.tree;

import java.util.ArrayList;
import java.util.LinkedList;

public class BinaryTreeNode<T> {

  private T value;
  private BinaryTreeNode<T> left;
  private BinaryTreeNode<T> right;

  public BinaryTreeNode() {
    this.value = null;
  }

  public BinaryTreeNode(T value) {
    this.value = value;
  }

  public T get() {
    return this.value;
  }

  public ArrayList<T> asList() {
    ArrayList<T> lst = new ArrayList<T>();
    lst.add(this.value);
    return lst;
  }

  public void set(T value) {
    this.value = value;
  }

  public BinaryTreeNode<T> getLeft() {
    return this.left;
  }

  public BinaryTreeNode<T> getRight() {
    return this.right;
  }

  public void setLeft(BinaryTreeNode<T> leftNode) {
    this.left = leftNode;
  }

  public void setRight(BinaryTreeNode<T> rightNode) {
    this.right = rightNode;
  }

  public void preOrder(ArrayList<T> elmList) {
    elmList.addAll(this.asList());
    if (this.left != null) {
      this.left.preOrder(elmList);
    }
    if (this.right != null) {
      this.right.preOrder(elmList);
    }
  }

  public void inOrder(ArrayList<T> elmList) {
    if (this.left != null) {
      this.left.inOrder(elmList);
    }
    elmList.addAll(this.asList());
    if (this.right != null) {
      this.right.inOrder(elmList);
    }
  }

  public void postOrder(ArrayList<T> elmList) {
    if (this.left != null) {
      this.left.postOrder(elmList);
    }
    if (this.right != null) {
      this.right.postOrder(elmList);
    }
    elmList.addAll(this.asList());
  }
  
  public void levelOrder(ArrayList<T> elmList) {
    LinkedList<BinaryTreeNode<T>> queue = new LinkedList<BinaryTreeNode<T>>();
    queue.offer(this);
    BinaryTreeNode<T> current;

    while (!queue.isEmpty()) {
      current = queue.poll();
      if (current.getLeft() != null) {
        queue.offer(current.getLeft());
      }
      if (current.getRight() != null) {
        queue.offer(current.getRight());
      }
      elmList.addAll(current.asList());
    }
  }
}