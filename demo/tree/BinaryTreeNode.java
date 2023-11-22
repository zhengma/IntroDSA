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

  public void set(T value) {
    this.value = value;
  }

  public BinaryTreeNode<T> get_left() {
    return this.left;
  }

  public BinaryTreeNode<T> get_right() {
    return this.right;
  }

  public void set_left(BinaryTreeNode<T> leftNode) {
    this.left = leftNode;
  }

  public void set_right(BinaryTreeNode<T> rightNode) {
    this.right = rightNode;
  }

  public void preOrder(ArrayList<T> elmList) {
    elmList.add(this.value);
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
    elmList.add(this.value);
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
    elmList.add(this.value);
  }
  
  public void levelOrder(ArrayList<T> elemList) {
    LinkedList<BinaryTreeNode<T>> queue = new LinkedList<BinaryTreeNode<T>>();
    queue.offer(this);
    BinaryTreeNode<T> current;

    while (!queue.isEmpty()) {
      current = queue.poll();
      if (current.get_left() != null) {
        queue.offer(current.get_left());
      }
      if (current.get_right() != null) {
        queue.offer(current.get_right());
      }
      elemList.add(current.get());
    }
  }
}