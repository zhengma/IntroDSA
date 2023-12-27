package demo.tree;

import java.util.ArrayList;

class BstNode<T extends Comparable<T>> extends BinaryTreeNode<T> {

  private int count;

  public BstNode() {
    super();
    this.count = 0;
  }

  public BstNode(T value) {
    super(value);
    this.count = 1;
  }

  @Override
  public BstNode<T> getLeft() {
    return (BstNode<T>)super.getLeft();
  }

  @Override
  public BstNode<T> getRight() {
    return (BstNode<T>)super.getRight();
  }

  @Override
  public ArrayList<T> asList() {
    ArrayList<T> lst = new ArrayList<T>();
    for (int i = 0; i < this.count; i++) {
      lst.add(this.get());
    }
    return lst;
  }

  public int getCount() {
    return this.count;
  }

  public void inc() {
    this.count++;
  }

  public void dec() {
    this.count--;
  }

  public BstNode<T> leftRotate() {
    if (this.getRight() == null) {
      return null;
    }
    BstNode<T> ptr = this.getRight();
    this.setRight(ptr.getLeft());
    ptr.setLeft(this);
    return ptr;
  }

  public BstNode<T> rightRotate() {
    if (this.getLeft() == null) {
      return null;
    }
    BstNode<T> ptr = this.getLeft();
    this.setLeft(ptr.getRight());
    ptr.setRight(this);
    return ptr;
  }
  
}

class BstNodePointers<E extends Comparable<E>> {
  private BstNode<E> pointer;
  private int loc;
  // loc = 0, 1, 2 依次代表我们要找的位置是pointer本身、左节点、右节点

  public BstNodePointers(BstNode<E> ptr, int loc) {
    this.pointer = ptr;
    this.loc = loc;
  }

  public BstNode<E> ptr() {
    return this.pointer;
  }

  public int loc() {
    return this.loc;
  }
}

public class BinarySearchTree<E extends Comparable<E>> {
  
  private BstNode<E> root;

  public BinarySearchTree() {
    root = new BstNode<E>();
  }

  public BinarySearchTree(ArrayList<E> data) {
    root = null;
    for (E value: data) {
      insert(value);
    }
  }

  private BstNodePointers<E> locNoRecursive(E key) {
    BstNode<E> ptr = this.root;
    while (!ptr.get().equals(key)) {
      if (key.compareTo(ptr.get()) < 0) {
        if (ptr.getLeft() == null) {
          return new BstNodePointers<E>(ptr, 1);
        } else {
          ptr = ptr.getLeft();
        }
      } else {
        if (ptr.getRight() == null) {
          return new BstNodePointers<E>(ptr, 2);
        } else {
          ptr = ptr.getRight();
        }
      }
    }
    return new BstNodePointers<E>(ptr, 0);
  }

  private BstNode<E> loc(BstNode<E> node, E key) {
    if (key.equals(node.get())) {
      return node;
    } else if (key.compareTo(node.get()) < 0) {
      return (node.getLeft() != null) ? loc(node.getLeft(), key) : null;
    } else {
      return (node.getRight() != null) ? loc(node.getRight(), key) : null;
    }
  }

  public int searchNoRecursive(E key) {
    BstNodePointers<E> location = locNoRecursive(key);
    if (location.loc() != 0) {
      return 0;
    } else {
      return location.ptr().getCount();
    }
  }

  public int search(E key) {
    BstNode<E> ptr = loc(this.root, key);
    return (ptr != null) ? ptr.getCount() : 0;
  }

  public ArrayList<E> sorted() {
    ArrayList<E> sorted = new ArrayList<E>();
    this.root.inOrder(sorted);
    return sorted;
  }

  public ArrayList<E> check_BST() {
    ArrayList<E> checkList = new ArrayList<E>();
    this.root.levelOrder(checkList);
    return checkList;
  }

  public void insertNoRecursive(E value) {
    if (this.root == null) {
      this.root = new BstNode<E>(value);
    } else {
      BstNodePointers<E> location = locNoRecursive(value);
      if (location.loc() == 1) {
        BstNode<E> tempNode = new BstNode<E>(value);
        location.ptr().setLeft(tempNode);
      } else if (location.loc() == 2) {
        BstNode<E> tempNode = new BstNode<E>(value);
        location.ptr().setRight(tempNode);
      } else {
        location.ptr().inc();
      }
    }
  }

  private BstNode<E> add(BstNode<E> node, E value) {
    if (node == null) {
      return new BstNode<E>(value);
    }
    if (value.compareTo(node.get()) < 0) {
      node.setLeft(add(node.getLeft(), value));
    } else if (value.compareTo(node.get()) > 0) {
      node.setRight(add(node.getRight(), value));
    } else {
      node.inc();
    }
    return node;
  }

  public void insert(E value) {
    this.root = add(this.root, value);
  }

  private BstNode<E> del(BstNode<E> node, E key) {
    if (key.compareTo(node.get()) < 0) {
      node.setLeft((node.getLeft() != null) ? del(node.getLeft(), key): null);
      return node;
    }
    if (key.compareTo(node.get()) > 0) {
      node.setRight((node.getRight() != null) ? del(node.getRight(), key): null);
      return node;
    }
    if (node.getCount() > 1) {
      node.dec();
      return node;
    }
    if (node.getLeft() == null) {
      return node.getRight();
    } else if (node.getRight() == null) {
      return node.getLeft();
    }
    BstNode<E> temp = node.getRight();
    while (temp.getLeft() != null) {
      temp = temp.getLeft();
    }
    temp.setLeft(node.getLeft());
    return node.getRight();
  }

  public void delete(E key) {
    this.root = del(this.root, key);
  }

/*  public boolean remove(E key) {
    BstNodePointers<E> location = locNoRecursive(key);
    if (location.loc() != 0) {
      System.out.println("The value is not in the BST.  Nothing is deleted.");
      return false;
    }
    if (location.ptr().getCount() > 1) {
      location.ptr().dec();
      return true;
    }
  }*/

  public void leftRotate() {
    this.root = this.root.leftRotate();
  }

  public void rightRotate() {
    this.root = this.root.rightRotate();
  }
}
